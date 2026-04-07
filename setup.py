from setuptools import setup, find_packages

setup(
    name="osint-seek-inteligence",
    version="1.0.0",
    description="Suite unificada de OSINT para Termux",
    author="makikas",
    packages=find_packages(),
    py_modules=["cli"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "osint-seek=cli:main",
        ],
    },
)
