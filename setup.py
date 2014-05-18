from setuptools import setup, find_packages

PACKAGE = 'sessionprofile'

setup(
        name='sessionprofile',
        version='1.0.3',
        packages=find_packages('django'),
        package_dir = {'': 'django'},

        platforms=['any'],
)
