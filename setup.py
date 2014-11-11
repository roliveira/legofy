#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='legofy',
    version='1.0',
    author='Rodolfo Oliveira',
    author_email='hi@roliveira.me',
    packages=['legofy'],
    scripts=['bin/img2lego.py'],
    url='https://github.com/oliveirarodolfo/legofy.git',
    license='MIT',
    description='Leg godt your picture with Python!.',
    long_description=readme(),
    install_requires=['numpy', 'matplotlib'],
)
