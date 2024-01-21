from setuptools import setup,find_namespace_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gondola',
    version="0.1.14",
    url='',
    author='rokdd',
    author_email='rokdd@gmx.ch',
    #py_modules=find_namespace_packages(),
    packages=find_namespace_packages(),
       long_description=long_description,
    long_description_content_type="text/markdown",
)