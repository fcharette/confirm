#!/usr/bin/env python
import os
from setuptools import setup

LONG_DESC = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
      name="confirm",
      version="0.1.0",
      description="Simple Python configuration file management.",
      long_description=LONG_DESC,
      author="Louis-Bertrand Varin",
      author_email="louisbvarin@gmail.com",
      packages=['confirm',],
      install_requires=['PyYAML>=3.0',],
      classifiers=[
          'Programming Language :: Python',
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Topic :: Utilities',
      ],
     )