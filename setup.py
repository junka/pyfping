from setuptools import setup

setup(
        name="pyfping",
        version="1.0.0",
        description="fping-like python application",
        author="Wan Junjie",
        author_email="wan.junjie@foxmail.com",
        packages=["pyfping"],
        package_dir={'pyfping':'./'},
        entry_points={
            'console_scripts':[
                'pyfping=pyfping.pyfping:main',
            ]
        },
        python_requires=">=3.5",
)