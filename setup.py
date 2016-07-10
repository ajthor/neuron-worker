
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

requirements = [
    'docker',
    'zmq'
]

setup(
    name='Neuron-worker',
    version='0.0.1',
    description='Neuron application for running processes.',
    long_description=readme,
    author='Adam Thorpe',
    author_email='adam.thorpe.g@gmail.com',
    url='https://github.com/ajthor/neuron-worker',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requirements
)
