from setuptools import setup, find_packages

setup(
    name='django-robots-txt',
    version='1.0.0',
    description='A Django package to manage robots.txt dynamically.',
    author='Reza Bayat',
    author_email='mrrezabayat@gmail.com',
    url='https://github.com/reza-bayat/django-robots-txt',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'Django>=3.0',
    ],
)