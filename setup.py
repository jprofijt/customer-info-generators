from setuptools import setup, find_packages

setup(
    name="customer_info_generator_jprofijt", 
    version="0.0.11",
    author="Jouke Profijt",
    description="package containing a few generators to generate random customer data",
    url="https://github.com/jprofijt/customer-info-generators",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLV3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)