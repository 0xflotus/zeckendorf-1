"""
Setup for zeckendorf package.
"""
from inspect import cleandoc

import setuptools

import zeckendorf

description = cleandoc(zeckendorf.__doc__)
with open('README.rst', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='zeckendorf',
    version='0.0.2',
    description=description,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/omaitzen/zeckendorf',
    author='Owen Maitzen',
    author_email='owenmaitzen@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
