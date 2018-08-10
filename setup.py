# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



# Import modules
from setuptools import setup, find_packages
from os import path


# Variables
here = path.abspath(path.dirname(__file__))
with open("{}/README.md".format(here), "r") as file:
    long_description = file.read()


# Setup
setup(
    name='karmia',
    version='0.1.0',  # Required
    description='Karmia framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/fujimakishouten/karmia-python',
    author='Kazuma Fujimaki',
    author_email='fujimaki-k@fujimakishouten.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='development karmia',
    packages=find_packages(exclude=['.idea', '.venv', 'test']),
    install_requires=['regex'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    test_suite='test'
)



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:
