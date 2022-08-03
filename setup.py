from setuptools import setup
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


install_requires = [
    'pyquery>=1.4.3',
    'regex>=2022.7.25',
]
extras_require = {'testing': ['pytest', 'pytest-cov', 'pytest-randomly', 'flake8']}


setup(
    name='py_style_flattener',
    version='0.0.3',
    description='Manipulate HTML by moving <style> to style=".',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CastixGitHub/py_style_flattener',
    project_urls={
        'Bug Reports': 'https://github.com/CastixGitHub/py_style_flattener/issues',
        'Source': 'https://github.com/CastixGitHub/py_style_flattener',
    },
    author='castix',
    author_email='castix@autistici.org',
    # packages=find_packages(where='src'),
    # package_dir={"py_style_flattener": "src"},
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    keywords=['html', 'style', 'css', 'parser', 'regex'],
    entry_points={
        'console_scripts': [
            'py-style-flattener = py_style_flattener.py_style_flattener:main',
        ]
    },
    python_requires='>=3.6',
    zip_safe=False,
)
