import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='ranked_pages',
    version='1.0.0',
    author="mouadziani",
    author_email="mouad.ziani1997@gmail.com",
    description="Get list of ranked pages's links of a specific website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mouadziani/shodan-finder-demo",
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
    packages=['ranked_pages'],
    include_package_data=True,
    zip_safe=False,
    install_requires=required
)
