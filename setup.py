from setuptools import find_namespace_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

import codecs
import os.path

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name="gondola",
    version=get_version("gondola/__init__.py"),
    url="https://github.com/rokdd/gondola",
    author="rokdd",
    author_email="rokdd@gmx.ch",
    packages=find_namespace_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        #for logging
        #"pprint"
        ],
    # install_requires=["gondola[]"],
    extras_require={
        "loggers": ["pprint"],
    },
)
