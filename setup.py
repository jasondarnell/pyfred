import os
from setuptools import setup

dir_path = os.path.dirname(os.path.abspath(__file__))

description = """pyfred"""
package_name = "pyfred"
requirements = open(os.path.join(dir_path, "requirements.txt")).read()
test_requirements = open(os.path.join(dir_path, "test_requirements.txt")).read()
version = open(os.path.join(dir_path, "VERSION")).read().strip()

def package_files():
    paths = []
    for (path, directories, filenames) in os.walk(package_name):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

setup(
    name=package_name,
    version=version,
    description=description,
    install_requires=requirements,
    extras_require={
        'test':  test_requirements,
    },
    packages=[package_name],
    package_data={'': package_files()},
    entry_points={

    },
    author="Jason Darnell",
    email="jasdarnell@gmail.com",
    license="MIT",
    url=""
)
