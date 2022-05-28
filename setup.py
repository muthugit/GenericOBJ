import setuptools
from setuptools import find_packages

build_version = "1.0.0"

if __name__ == "__main__":
    with open("README.md", "r") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="generic_obj", # Replace with your own username
        version=build_version,
        author="Muthupandian",
        author_email="contact@muthupandian.in",
        description="Generic object for any purpose",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/muthugit/GenericOBJ",
        # packages=setuptools.find_packages(),
        packages=['generic_obj'],
        project_urls={
            "Documentation": "https://github.com/muthugit/GenericOBJ/wiki/What-is-GenericOBJ",
            "Author": "https://muthupandian.in"
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )