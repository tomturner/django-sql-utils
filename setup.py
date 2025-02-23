from setuptools import setup, find_packages


def read_file(name):
    try:
        with open(name) as fd:
            return fd.read()
    except IOError:
        return ''


setup(
    name='django-sql-utils',
    version='0.7.0',
    description='Improved API for aggregating using Subquery',
    long_description=read_file('README.rst'),
    url='https://github.com/martsberger/django-sql-utils',
    download_url='https://github.com/martsberger/django-sql-utils/archive/0.6.1.tar.gz',
    author='Brad Martsberger',
    author_email='bmarts@lumere.com',
    license='MIT',
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    packages=find_packages(),
    install_requires=['django>=1.11', 'sqlparse']
)
