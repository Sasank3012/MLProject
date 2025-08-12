from setuptools import setup, find_packages
import os
from typing import List

hyphen_e_dot = "-e ."

def read_requirements(file_path: str = 'requirements.txt') -> List[str]:
    """Read the requirements from a requirements.txt file."""
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n', '') for req in requirements if req and not req.startswith('#')]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements


setup(
    name='mlproject',
    version='0.1',  # Update this to your project's version
    packages=find_packages(),
    install_requires=read_requirements(),
    description='A machine learning project for Azure ML',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'mlproject=mlproject.main:main',  
        ],
    },
    author='Sasank Ponnapalli',
)

