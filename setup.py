#!/usr/bin/env python

PROJECT = 'virtualenvwrapper.django_template'
VERSION = '0.2'

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
    package_data={
        'virtualenvwrapper': [
            'django_project_template/*.txt',
            'django_project_template/static/.gitkeep',
            'django_project_template/redirects/.gitkeep',
            'django_project_template/README.md',
            'django_project_template/media/.gitkeep',
            'django_project_template/manage.py',
            'django_project_template/app/*.py',
            'django_project_template/app/templates/*.html',
            'django_project_template/app/templates/*.txt',
            'django_project_template/app/templates/mail/*.html',
            'django_project_template/app/public/assets/css/*.css'
            'django_project_template/app/public/assets/js/*.js'
            'django_project_template/app/public/assets/ico/*.ico'
            'django_project_template/app/public/assets/ico/*.png'
        ]
    },
    entry_points={
        'virtualenvwrapper.project.template': [
            'django=virtualenvwrapper.django_project:template',
        ],
    },

    zip_safe=False,
)
