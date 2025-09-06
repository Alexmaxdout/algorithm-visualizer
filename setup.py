from setuptools import setup, find_packages

setup(
    name="algorithm_visualizer",
    version="0.1.0",
    author="Alexander Maxwell",
    author_email="alexmaxdout@outlook.com",
    description="An interactive tool to visualize classic algorithms (sorting, searching, graph traversal).",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alexmaxdout/algorithm-visualizer",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "matplotlib>=3.7.0",
        "pygame>=2.5.0",
        "numpy>=1.25.0"
    ],
    entry_points={
        "console_scripts": [
            "visualizer=visualizer:main",  # Assuming your src/visualizer.py has a main() function
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
