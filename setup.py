from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='pyoai',
    version='2.5.1b0',
    author='Infrae',
    author_email='info@infrae.com',
    url='http://www.infrae.com/download/oaipmh',
    classifiers=["Development Status :: 4 - Beta",
                 "Programming Language :: Python",
                 "License :: OSI Approved :: BSD License",
                 "Topic :: Software Development :: Libraries :: Python Modules",
                 "Environment :: Web Environment"],
    description=None,
    long_description=None,
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    zip_safe=False,
    license='BSD',
    keywords='OAI-PMH xml archive',
    install_requires=['lxml', 'six'],
)
