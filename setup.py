# -*- coding: utf-8 -*-
# pub (c) Ian Dennis Miller

import re
import os
from setuptools import setup
from distutils.dir_util import copy_tree


# from https://github.com/flask-admin/flask-admin/blob/master/setup.py
def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


file_text = read(fpath('pub/__meta__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


setup(
    version=grep('__version__'),
    name='pub',
    description="Pub is a self-publishing framework.",
    packages=[
        "pub",
    ],
    scripts=[
        "bin/pub",
    ],
    long_description=read('Readme.rst'),
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    author=grep('__author__'),
    author_email=grep('__email__'),
    url=grep('__url__'),
    install_requires=read('requirements.txt'),
    license='MIT',
    zip_safe=False,
)

venv_path = os.environ.get("VIRTUAL_ENV")
if venv_path:
    copy_tree("skel", os.path.join(venv_path, "share/skel"))
else:
    print("This was not installed in a virtual environment.")
    print("I won't install the skel files until later.")