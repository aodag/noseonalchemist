from setuptools import setup, find_packages
import os

readme = open(os.path.join(os.path.dirname(__file__), "README.txt")).read()

setup(name="noseonalchemist",
    author="Atsushi Odagiri",
    author_email="aodagx@gmail.com",
    description="nose plugin for reporting about commit counts on SQLAlchemy",
    long_description=readme,
    version="0.1",
    url="https://github.com/aodag/noseonalchemist",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "nose",
    ],
    test_suite="noseonalchemist",
    entry_points="""
    [nose.plugins.0.10]
    commitreport=noseonalchemist:CommitReportPlugin
    """,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Topic :: Software Development :: Testing",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],

)
