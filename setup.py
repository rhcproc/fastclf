# Pip_Package_Practice/setup.py
from setuptools import setup, find_packages
from os.path import dirname, join as pjoin

with open("README.md", "r") as fh:
    long_description = fh.read()

meta = {}
with open(pjoin('sklearnfast', '__version__.py')) as f:
    exec(f.read(), meta)


setup(
    name=meta['__title__'],
    license=meta['__license__'],
    version=meta['__version__'],
    author=meta['__author__'],
    author_email=meta['__contact__'],
    url=meta['__url__'],
    description=meta['__description__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.5",
    install_requires=[
        'pandas',
        'scikit-learn',
    ],
)
