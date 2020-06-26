from setuptools import setup, find_packages

setup(
    name="InventoryGen",
    author="Julien Esseiva",
    description="Tool to generate inventory files for the BnL Namalysator.",
    version="0.1",
    packages=find_packages(),
    scripts=["bin/inventorygen"],
    install_requires=[
        "PyYAML>=5.3.1"
    ]
)
