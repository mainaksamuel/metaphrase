#!/usr/bin/env python3

from setuptools import setup, find_packages


with open('requirements.txt', 'r') as r:
    requirements = r.read().split('\n')

setup(
    name='metaphrase',
    description='A CLI language translation app',
    version='1.0.0',
    author='mainaksamuel',
    author_email='mainasamkaranja@gmail.com',
    python_requires='>=3.9.5',
    packages=find_packages(),
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        metaphrase=metaphrase.__init__:main
    ''',
)
