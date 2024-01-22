from setuptools import setup, find_namespace_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gondola",
    version="0.1.14",
    url="",
    author="rokdd",
    author_email="rokdd@gmx.ch",
    packages=find_namespace_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        #for logging
        "pprint"
        ],
    # install_requires=["gondola[]"],
    # extras_require={
    #    "PDF": ["ReportLab>=1.2", "RXP"],
    # },
)
