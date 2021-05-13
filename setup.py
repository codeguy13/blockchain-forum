from setuptools import find_packages, setup
import os

setup(name='blockforum',
      version='0.0.1',
      py_modules=['blockchain', './blockchain/interface', 'p2p'],
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      )
