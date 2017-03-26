from setuptools import setup, find_packages

setup(
    name='django-mail',
    version='0.1',
    description='Autoresponder and emails queue with django-celery.',
    long_description='',
    author='Alexander Pokatilov',
    author_email='wreckah@ya.ru',
    packages = find_packages(),
    install_requires = ['django', 'django-celery'],
)
