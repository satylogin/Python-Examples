from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="satylogin.ptree",
    version="0.1.0",
    url="https://github.com/satylogin/Python-Examples/python-tree",
    author="Satyarth Agrahari",
    author_email="satylogin@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Utility Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    install_requires=[
        "termcolor>=1.0,<2.0",
    ],
    extras_require={
        "dev": ["check-manifest"],
        "test": ["pytest", "coverage"],
    },
    entry_points={
        "console_scripts": [
            "ptree=ptree.cli:main",
        ],
    },
)
