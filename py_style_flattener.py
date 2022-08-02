"""
py_style_flatter.py
 2022 Castix <castix@autistici.org>
LICENSE: GPLv3+
USAGE: python py_style_flattener.py INPUT OUTPUT
This module is useful to move all the css from style tags to inline style attribute
Makes use of pyquery and regex (due to stdlib's re module not supporting recursion)
Keeps all the @font-face but removes everything else
Current limitations:
- doesn't fetch remote style
- cannot set pseudo elements (limitation inherited from cssselect used by pyquery)
- only takes care of @media screen{} avoiding all other media queries
"""

from sys import argv
import re
import regex
from pyquery import PyQuery as pq


with open(argv[1], 'r') as f:
    d = pq(f.read())


# using recursive regex. unavailable on standard re module
selector_re = regex.compile(
    r'([\w @\-#.\+:\s]+)([{](?>[^{}]+|(?2))*[}])',
    flags=regex.MULTILINE | regex.V1,
)
prop_value = regex.compile(
    r'([\w-:]+):([^;}]*;base64,[^;}]*|[^;}]*)(?2)',
    flags=regex.MULTILINE | regex.V1,
)


def extract_css(string: str) -> dict:
    return {
        ___match[0].strip(): ___match[1].strip()
        for ___match in prop_value.findall(string)
    }

def generate_css(new_style: dict) -> str:
    return '; '.join([
        ': '.join(list(new_style.items())[i])
        for i in range(len(new_style))
    ]) + ';'


for style in d('style'):
    # TODO: handle src attr
    
    # stripping out commments
    style.text = re.sub(r'\/\*.*\/', '', style.text, flags=re.S)

    css = {}
    for _match in selector_re.findall(style.text):
        if '@media screen' == _match[0].strip():
            print('media screen processing')
            for __match in selector_re.findall(_match[1]):
                css[__match[0].strip()] = extract_css(__match[1].strip())
        elif '@font-face' == _match[0].strip():
            font_css = extract_css(_match[1].strip())
            if '@font-face' not in css.keys():
                css['@font-face'] = {}
            css['@font-face'][font_css['font-family']] = font_css
        elif _match[0].strip().startswith('@'):
            print('skipped', _match[0].strip())
        else:
            css[_match[0].strip()] = extract_css(_match[1].strip())

    print(css)

    # now manipulate using pyquery
    style.clear()
    
    for selector, new_style in css.items():
        print(selector)
        if any([pseudo in selector for pseudo in (':after', ':before', '::selection', '::-moz-selection')]):
            print('pseudo elements unsupported')
            continue
        if selector == '@font-face':
            if not style.text:
                style.text = ''
            for font in new_style.values():
                style.text += '\n@font-face{\n' + generate_css(font) + '\n}\n'
            continue
        old_style = d(selector).attr('style')
        # parse the old style if present
        if old_style:
            old_style = {
                ___match[0].strip(): ___match[1].strip()
                for ___match in prop_value.findall(old_style)
            }
            # inline style takes precedence
            new_style.update(old_style)
        new_style_str = generate_css(new_style)
        d(selector).attr('style', new_style_str)


with open(argv[2], 'w') as f:
    f.write(str(d))
