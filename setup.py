#!/usr/bin/env python

PROJECT = 'virtualenvwrapper.django_template'
VERSION = '0.1'

from setuptools import setup, find_packages


try:
    long_description = open('README', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,
    description='virtualenvwrapper plugin to create a template Django application',
    long_description=long_description,
    author='Chris Proto',
    url='http://chrispro.to/projects/virtualenvwrapper-django-template',
    author_email='chroto24@gmail.com',
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: BSD License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 'Framework :: Django',
                 ],
    platforms=['Any'],

    provides=['virtualenvwrapper.django'],
    requires=['virtualenv',
              'virtualenvwrapper (>=2.9)',
              ],
    namespace_packages=['virtualenvwrapper'],
    packages=find_packages(),
    entry_points={
        'virtualenvwrapper.project.template': [
            'django=virtualenvwrapper.django_project:template',
        ],
    },

    zip_safe=False,
)
