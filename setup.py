#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup  # type: ignore

setup_requirements: list[str] = []

setup(
    name="saxo_openapi",
    version="0.2.0",
    description="SAXO Bank OpenAPI REST-API access with integrated OAuth2 authentication",
    long_description="",
    author="nohikomiso",
    author_email="",
    url="https://github.com/nohikomiso/saxo-openapi",
    packages=find_packages(include=["saxo_openapi", "saxo_openapi.*"]),
    include_package_data=True,
    install_requires=[
        "requests",
        # 認証サブモジュール (saxo_openapi.auth) の依存関係
        "Flask",
        "pydantic>=2.0",
        "httpx",
        "websockets",
        "loguru",
    ],
    python_requires=">=3.13",
    zip_safe=False,
    keywords="saxo_openapi",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
    ],
)
