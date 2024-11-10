from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1.0",
    description="A simple interactive math quiz game",
    author="Sadia Afrin Mou",
    author_email="sadia.afrin.mou@fau.de",  # Your email
    url="https://github.com/sadia-afrin-mou/dsss_homework_2",  # URL to the project's homepage
    license="Apache License 2.0",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz",
        ],
    },
)