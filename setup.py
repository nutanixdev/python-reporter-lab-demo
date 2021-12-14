from setuptools import setup, find_packages

with open('readme.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='python-reporter',
    version='1.0',
    description='Use the Prism Central API to get Nutanix environment info.',
    long_description=readme,
    author='<your_name_here>',
    author_email='<your_email_address_here>',
    install_requires=[
        'requests',
        'urllib3'
    ],
    packages=find_packages('.'),
    package_dir={'': '.'}
)
