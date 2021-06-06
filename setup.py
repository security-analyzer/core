import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='security_analyzer',
    version='1.0.0',
    author="mouadziani",
    author_email="mouad.ziani1997@gmail.com",
    description="A large scale web crawler for to take an overview about security of Moroccan sites ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mouadziani/shodan-finder-demo",
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
    packages=['src'],
    include_package_data=True,
    zip_safe=False,
    install_requires=required
)
