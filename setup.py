import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mypypackage",
    version="0.0.1",
    author="Joao Vicente",
    url="https://github.com/joaovicente/mypypackage",
    description="Example for how to package a Python library",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "art"
    ],
    python_requires='>=3.6',
)