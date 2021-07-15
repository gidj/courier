#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Gideon VanRiette",
    author_email='gideon@postscript.io',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Your friend who delivers messages on schedule",
    entry_points={
        'console_scripts': [
            'courier=courier.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='courier',
    name='courier',
    packages=find_packages(include=['courier', 'courier.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/gidj/courier',
    version='0.1.0',
    zip_safe=False,
)
