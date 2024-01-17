from setuptools import setup,find_packages

from __init__ import __version__

setup(
    name='gondola',
    version=__version__,
    url='',
    author='rokdd',
    author_email='rokdd@gmx.ch',
    py_modules=find_packages(),
)