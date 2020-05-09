import codecs
import os
import sys
import kdn

try:
	from setuptools import setup, find_packages
except:
	from distutils.core import setup

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'),'r',encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = "kdn-sdk",
    version = kdn.__version__,
    description = "KDN Python SDK",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    classifiers =
	[
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
		'Topic :: Scientific/Engineering :: Astronomy',
		'Topic :: Scientific/Engineering :: GIS',
		'Topic :: Scientific/Engineering :: Mathematics',
		'Intended Audience :: Science/Research',
		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
    ],
    keywords = "kdn sdk",
    author = "blackcat",
    author_email = "kfx2007@163.com",
    url ="https://github.com/block-cat/kdn-sdk",
    license = "GNU",
    packages = find_packages(),
    include_package_data= True,
    install_requires=[
        'requests',
    ],
    package_data={
        "":['kdn/data/express.csv']
    },
    setup_requires=[
        'requests',
    ],
    zip_safe= True,
)