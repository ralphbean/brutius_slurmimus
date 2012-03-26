from setuptools import setup, find_packages
import sys, os

import brutius_slurmimus
long_description = brutius_slurmimus.__doc__

version = '0.1.1'

setup(name='brutius_slurmimus',
      version=version,
      description="Parse-and-return slurm commands.  Don't use this.  Use pyslurm instead.",
      long_description=long_description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Ralph Bean',
      author_email='ralph.bean@gmail.com',
      url='http://github.com/ralphbean/brutius_slurmimus',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
