# -*- coding: utf-8 -*-

from io import open
from setuptools import setup, find_packages


setup(
    name='httpstatus35',
    version='0.0.1',
    description='Python 3.5 http.HTTPStatus backported to 3.4 and 2.7',
    long_description=open('README.rst', encoding='utf-8').read(),
    author='Nikita Grishko',
    author_email='gr1n@protonmail.com',
    url='https://github.com/Gr1N/httpstatus35',
    download_url='https://pypi.python.org/pypi/httpstatus35/',
    license='MIT',
    packages=find_packages(exclude=(
        'tests.*',
        'tests',
        'example',
    )),
    extras_require={
        'py2x': [
            'enum34',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    )
)
