#!/usr/bin/env python

import os
import re
import sys

from codecs import open

from setuptools import setup, find_packages

packages = [
    'deleteolddata',
]

version = ''
with open('deleteolddata/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='delete-old-data',
    version=version,
    description='Tool for deleting old folders from hourly log record',
    long_description=readme,
    author="Shaun O'Keefe",
    author_email='shaun.okeefe.0@gmail.com',
    url='https://github.com/shaunokeefe/deletealldata',
    license='Apache 2.0',
    classifiers=(
        'Development Status :: 2 - Pre-alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ),
    entry_points={
        'console_scripts': [
            'delete-old-data = deleteolddata.cli:delete_old_data',
        ],
    },
    packages=find_packages(exclude=['tests*']),
    test_suite='test',
    install_requires=['click'],
    tests_require=['mock'],
)
