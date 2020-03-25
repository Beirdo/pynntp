from setuptools import setup

setup(
    name='pynntp',
    version='0.8.5',
    description='NNTP Library (including compressed headers) - Python3 compatible',
    author='Byron Platt / Gavin Hurlbut',
    author_email='gjhurlbu@gmail.com',
    license='GPL3',
    url='https://github.com/Beirdo/pynntp',
    packages=['nntp'],
    install_requires=['dateutils'],
)
