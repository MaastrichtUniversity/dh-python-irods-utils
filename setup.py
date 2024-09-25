import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dh-python-irods-utils",
    version="1.2.1",
    author="DataHub",
    author_email="author@example.com",
    description="This is where we store all the python helper functions for iRODS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaastrichtUniversity/dh-python-irods-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7",
    tests_requires=["pytest", "pytest-dotenv"],
)
