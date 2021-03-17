import setuptools

REQUIRED = ["numpy", "pandas"]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dockerassignment212", # Replace with your own username
    version="0.0.1",
    author="singparvi",
    description="A collection of Data Science functions for Unit 3 Assignment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/singparvi/lambdatasingparvi",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    python_requires=">=3.6",
)