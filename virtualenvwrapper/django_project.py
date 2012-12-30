#!/usr/bin/env python
"""
Create a Django project with virtualenvwrapper
"""

import logging
import subprocess
import os

log = logging.getLogger('virtualenvwrapper.django')


def template(args):
    project = args[0]
    template_arg = ''
    DJANGO_TEMPLATE = os.getenv('DJANGO_TEMPLATE', '')
    if DJANGO_TEMPLATE != '':
        requirements_file = os.path.join(DJANGO_TEMPLATE, 'requirements.txt')
        subprocess.check_call([
            'pip',
            'install',
            '-r',
            requirements_file
        ])
        template_arg = '--template=%s' % DJANGO_TEMPLATE

    subprocess.check_call([
        'django-admin.py',
        'startproject',
        project,
        template_arg
    ])
