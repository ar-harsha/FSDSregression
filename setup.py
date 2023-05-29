from setuptools import find_packages, setup
from typing import List

ignore_this = '-e .'

def get_requirements(path:str) -> List[str]:
    requirements = []
    with open(path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if ignore_this in requirements:
            requirements.remove(ignore_this)
    return requirements


setup(
    name="Regressionproj",
    version="0.0.1",
    author="HAR",
    author_email="harsha999ar@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)