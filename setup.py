from setuptools import setup, find_packages

setup(
    name='automata',
    version='0.2.4',
    packages=find_packages(),
    entry_points={"console_scripts": ["automata = main:main"]},
)
