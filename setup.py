try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
setup(
    name='sv2bed',
    version='0.0.1',
    author='Danny Antaki',
    author_email='dantaki@ucsd.edu',
    packages=['sv2bed'],
    scripts=['sv2bed/sv2bed'],
    url='https://github.com/dantaki/sv2bed',
    license='LICENSE',
    long_description=open('README').read(),
)
