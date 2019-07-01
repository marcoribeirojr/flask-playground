# _*_ coding: utf-8 _*_

#Third
from setuptools import find_packages, setup

__version__ = '0.0.1'
__description__ = 'API Flask'
__long_description__ = 'API utilizando Flask'

__author__ = 'Marco Ribeiro Jr'
__author_email__ = 'contato@marcoribeirojr.com.br'

__url__='https://github.com/marcoribeirojr/flask-playground.git'

setup(
        name='api',
        version=__version__,
        author=__author__,
        author_email=__author_email__,
        packages=find_packages(),
        licence='MIT',
        description=__description__,
        long_description=__long_description__,
        url=__url__,
        keywords='API,Python',
        include_package_data=True,
        zip_safe=False,
        classifiers=[
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'Operating System :: OS Independent',
            'Topic :: Software Development',
            'Environment :: Web Environment',
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
        ],
)







