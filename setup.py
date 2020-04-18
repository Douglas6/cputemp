import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cputemp",
    version="0.1.0",
    author="",
    author_email="",
    description="A static site generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Douglas6/cputemp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'dbus-python',
        'gpiozero'
    ]
)
