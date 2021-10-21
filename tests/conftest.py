import os

import django


def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.django_settings')
    django.setup()
