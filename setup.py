# Pip_Package_Practice/setup.py
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sklearnfast', 
    version='0.0.14',
    description='fastsklearn is a package that makes it easy to test different models on different datasets. ',
    author='rhcproc',
    author_email='rhcproc@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rhcproc/sklearnfast",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages= ['sklearnfast'],
    python_requires=">=3.7",
    )
