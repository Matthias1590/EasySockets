from setuptools import setup


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="easysockets",
    version="1.0.0",
    description="A Python module that allows you to create and use simple sockets.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Matthias1590/EasySockets",
    author="Matthias Wijnsma",
    author_email="matthiasx95@gmail.com",
    license="MIT",
    python_requires=">=3.6",
    packages=["easysockets"],
)
