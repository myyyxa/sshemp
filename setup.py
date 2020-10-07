from os.path import join, dirname

from setuptools import setup, find_packages

setup(
    name='sshemp',
    version='1',
    packages=find_packages(),
    author='myyyx',
    author_email='myyyxa@gmail.com',
    maintainer='',
    maintainer_email='',
    description='simple smart house esp32 micropython',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    url='https://github.com/myyyxa/sshemp',
    download_url='',
    classifiers='',
    platforms='',
    keywords='',
    license='free',
    optional=True,
    include_package_data=True,
    install_requires='requirements.txt',
    test_suite='tests',)
