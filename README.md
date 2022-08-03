# Py Style Flattener

## Introduction
This module is useful to move all the css from style tags to inline style attribute
Makes use of pyquery and regex (due to stdlib's re module not supporting recursion)
Keeps all the @font-face but removes everything else

### Installation

```bash
pip install py_style_flattener
```

### Usage

It can be used from cli:
```bash
$ py-style-flattener INPUT OUTPUT
```
(note that INPUT and OUTPUT can be either paths or stdin/stdout)

Or as a python module

```python
>>> import py_style_flattener
>>> # using files, you need to open them before.
>>> py_style_flattener.using_files(INPUT, OUTPUT)
>>> # using plain strings
>>> OUTPUT = dpy_style_flattener.using_strings(INPUT)
```

### Current limitations:

- doesn't fetch remote style
- cannot set pseudo elements (limitation inherited from cssselect used by pyquery)
- only takes care of @media screen{} avoiding all other media queries


## Contributing

### build & release
```bash
pip install build
python -m build
```
