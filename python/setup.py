import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simtools",
    version="0.0.1",
    author="Alan O'Connell",
    author_email="",
    description="SimTools using VUnit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/paoconnell/simtools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
