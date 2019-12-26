import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hkjournalist",
    version="0.0.4",
    author="Xinyi",
    author_email="wolixinyi@gmail.com",
    description="Custom Auto Report Generator for Python Program",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/li-xin-yi/HK-journalist",
    packages=setuptools.find_packages(),
    package_data={'configuration':['hkjournalist/configuration/*']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires = ['tabulate',
                        'pandas',
                        'pandoc',
                        'matplotlib',
                        ]
)
