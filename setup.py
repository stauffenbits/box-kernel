import setuptools
from distutils.core import setup

with open('README') as f:
    readme = f.read()

setup(
    name='box_kernel-stauffenbits',
    version='1.6',
    packages=setuptools.find_packages(),
    description='Simple box kernel for Jupyter',
    long_description=readme,
    author='Joshua M. Moore',
    author_email='moore.joshua@pm.me',
    url='https://github.com/stauffenbits/box_kernel',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
