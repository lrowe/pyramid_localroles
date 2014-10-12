import os.path
from setuptools import setup, find_packages

here = os.path.dirname(__file__)
try:
    with open(os.path.join(here, 'README.txt')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()
except IOError:
    README = CHANGES = ''  # tox

requires = [
    'pyramid',
]


setup(
    name='pyramid_localroles',
    version='0.1',
    description='Local roles authorization policy for Pyramid',
    long_description=README + '\n\n' + CHANGES,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    author='Laurence Rowe',
    author_email='laurence@lrowe.co.uk',
    url='http://github.com/lrowe/pyramid_localroles',
    license='MIT',
    install_requires=requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
