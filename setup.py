
from setuptools import setup, find_packages

version = '1.0'

setup(
    name="alerta-rest",
    version=version,
    description='Alerta rest plugin',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    py_modules=['alerta_rest'],
    zip_safe=True,
    entry_points={
        'alerta.plugins': [
            'rest = alerta_rest:RestPublisher'
        ]
    }
)
