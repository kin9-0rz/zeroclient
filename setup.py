import os.path

from setuptools import find_packages, setup
from zeroclient import __VERSION__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="zeroclient",

    version=__VERSION__,

    description=(""),
    # long_description=read('README.rst'),

    url="https://github.com/mikusjelly/zero-client",

    author="mikusjelly",
    author_email="mikusjelly@gmail.com",

    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],

    keywords="",

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
    ],

    zip_safe=False,
    # entry_points={
    #     'console_scripts': [
    #         'textwizard=TextWizard:main'
    #     ]
    # }
)
