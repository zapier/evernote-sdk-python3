import os
from setuptools import setup, find_packages


# Load version number from Thrift-Compiler-generated .py file
constants_path = os.path.join(os.path.dirname(__file__), "evernote",
                              "edam", "userstore", "constants.py")

with open(constants_path) as constants_file:
    constants = constants_file.read().split("\n")
    for x in [x for x in constants if x.startswith('EDAM_VERSION')]:
        exec(x)


def read_from_same_directory(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as open_file:
        content = open_file.read()
    return content


ZAPIER_POST_VERSION = "post2"
setup(
    name='evernote3',
    version="{major}.{minor}.0.{post_version}".format(
        major=EDAM_VERSION_MAJOR,
        minor=EDAM_VERSION_MINOR,
        post_version=ZAPIER_POST_VERSION,
    ),
    author='Evernote Corporation',
    author_email='api@evernote.com',
    url='http://dev.evernote.com',
    description='Evernote SDK for Python3',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2'
        'Programming Language :: Python :: 3'
    ],
    license='BSD',
    install_requires=[
        'oauthlib',
        'requests_oauthlib',
        'six',
    ],
)
