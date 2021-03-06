from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="dj",
    version="0.0.1",
    author="Dhannu Junnu",
    author_email="cloudhound08@gmail.com",
    description="A package for DataPlatform management",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/cloudhound08/dj/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)