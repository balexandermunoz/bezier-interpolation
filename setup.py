from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="bezier-interpolation",
    version="0.0.2",
    author="Brayan Munoz",
    author_email="balexander.munoz@udea.edu.co",
    description="A Python library for generating smooth curves between given points using cubic and quadratic Bezier interpolation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/balexandermunoz/bezier-interpolation",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        "numpy >= 1.26.0",
    ],
    extras_require={
        "devel": [
            "wheel",
        ]
    }
)
