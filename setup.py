import os.path

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="zeroclient",

    version='1.0.0',

    description=(""),
    # long_description=read('README.rst'),

    url="https://github.com/mikusjelly/zero-client",

    author="mikusjelly",
    author_email="mikusjelly@gmail.com",

    license="Apache 2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache License",
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
