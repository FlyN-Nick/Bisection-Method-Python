import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bisection-method-flyn-nick", 
    version="1.0.1",
    author="Nicholas Assaderaghi",
    author_email="nickassader@gmail.com",
    description="An implementation of the bisection method in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FlyN-Nick/Bisection-Method-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords="bisection method"
)