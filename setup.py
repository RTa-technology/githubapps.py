
import re

import setuptools

version = ''
with open('githubapps/__init__.py') as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

requirements = []
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()


with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='githubapps.py',
    version=version,
    license='MIT',
    description='This is a wrapper for the Github Apps API.',
    long_description_content_type='text/markdown',
    url='https://github.com/RTa-technology/githubapps.py',
    author='RTa-technology',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
