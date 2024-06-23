from setuptools import setup, find_packages

setup(
    name='production_optimization',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pulp==2.6.0',
        'pytest==8.2.2',
        'flake8==6.0.0'
    ],
    entry_points={
        'console_scripts': [
            'run_optimization=production_optimization.main:run_optimization',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
