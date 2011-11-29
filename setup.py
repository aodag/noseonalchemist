from setuptools import setup, find_packages

setup(name="noseonalchemist",
    packages=find_packages(),
    install_requires=[
        "nose",
    ],
    entry_points="""
    [nose.plugins.0.10]
    commitreport=noseonalchemist:CommitReportPlugin
    """,
)
