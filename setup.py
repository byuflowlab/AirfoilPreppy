#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup  # , find_packages


setup(
    name='AirfoilPrep.py',
    version='0.2.0',
    description='Airfoil preprocessing for wind turbine applications',
    author='S. Andrew Ning',
    author_email='andrew.ning@nrel.gov',
    package_dir={'': 'src'},
    py_modules=['airfoilprep'],
    install_requires=['pyXLIGHT.py>=0.1'],
    license='Apache License, Version 2.0',
    dependency_links=['https://github.com/Ry10/pyxlight/tarball/pyXLIGHT#egg=pyXLIGHT.py-0.1'],
    zip_safe=False
)