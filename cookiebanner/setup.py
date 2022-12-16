# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, 'README.rst')) as f:
    long_desc = f.read()

requires = ['Sphinx>=0.6']

setup(
    name='sphinxcontrib-cookiebanner',
    version='0.1',
    license='BSD',
    author='Danny Diaz',
    author_email='ddiaz@firstinspires.org',
    description='Sphinx extension cookiebanner',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
