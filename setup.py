import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = '0.0.2'
AUTHOR_NAME = 'Adam Erispaha'
AUTHOR_EMAIL = 'aerispaha@gmail.com'

install_requires = [
    'numpy',
    'pandas',
    ]

setup(name='raintools',
      version=VERSION,
      description='Tools for manipultaing and analyzing rainfall data.',
      author=AUTHOR_NAME,
      url='https://github.com/aerispaha/rain_tools',
      author_email=AUTHOR_EMAIL,
      packages=find_packages(exclude=('tests')),
      install_requires=install_requires,
      long_description=read('README.rst'),
      platforms="OS Independent",
      license="MIT License",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.7",
      ]
)
