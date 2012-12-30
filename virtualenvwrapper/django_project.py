#!/usr/bin/env python
"""
Create a Django project with virtualenvwrapper
"""

import logging
import subprocess
import os

log = logging.getLogger('virtualenvwrapper.django')


def get_data(path):
    ROOT = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(ROOT, path)


def template(args):
    project = args[0]
    default_project_path = get_data('django_project_template')
    DJANGO_TEMPLATE = os.getenv('DJANGO_TEMPLATE', default_project_path)
    requirements = os.path.join(DJANGO_TEMPLATE, 'requirements.txt')
    pip_args = [
        'pip',
        'install'
    ]
    if os.path.exists(requirements):
        pip_args.extend(['-r', requirements])
    else:
        pip_args.append('Django')
    subprocess.check_call(pip_args)
    subprocess.check_call([
        'django-admin.py',
        'startproject',
        '--template=%s' % DJANGO_TEMPLATE,
        project,
        '.'
    ])
    subprocess.check_call([
        'python',
        'manage.py',
        'syncdb'
    ])
    subprocess.check_call([
        'python',
        'manage.py',
        'migrate'
    ])
    subprocess.check_call([
        'python',
        'manage.py',
        'runserver_plus'
    ])
