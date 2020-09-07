from setuptools import find_packages, setup

setup(
    name="automata",
    version="0.3.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["automata = main:main"]},
)
