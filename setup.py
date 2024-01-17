from setuptools import setup,find_packages

from gondola import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gondola',
    version=__version__,
    url='',
    author='rokdd',
    author_email='rokdd@gmx.ch',
    py_modules=find_packages(),
       long_description=long_description,
    long_description_content_type="text/markdown",
)