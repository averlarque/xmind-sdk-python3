#!/usr/env/bin python

from setuptools import setup, find_packages

setup(
    name="xmind",
    version="0.1a.0",
    packages=find_packages(),

    install_requires=["distribute"],

    author="Woody Ai",
    author_email="woody@xmind.net",
    description="The offical XMind python SDK",
    license="MIT",
    keywords="XMind, SDK, mind mapping",
    url="https://github.com/xmindltd/xmind-sdk-python"
)
