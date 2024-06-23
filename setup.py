from setuptools import setup, find_packages

setup(
    name='production_optimization',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pulp',
    ],
    entry_points={
        'console_scripts': [
            'run_optimization=production_optimization.main:main',
        ],
    },
)
