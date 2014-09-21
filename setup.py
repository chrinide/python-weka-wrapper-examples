# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# setup.py
# Copyright (C) 2014 Fracpete (fracpete at gmail dot com)

from setuptools import setup


setup(
    name="python-weka-wrapper-examples",
    description="Examples for the python-weka-wrapper library.",
    url="https://github.com/fracpete/python-weka-wrapper-examples",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python',
    ],
    license='GNU General Public License version 3.0 (GPLv3)',
    package_dir={
        '': 'src'
    },
    packages=[
        "wekaexamples",
        "wekaexamples.core",
        "wekaexamples.plot"
    ],
    version="0.1.0",
    author='Peter "fracpete" Reutemann',
    author_email='fracpete at gmail dot com',
    install_requires=[
        "python-weka-wrapper>=0.1.11",
    ],
)