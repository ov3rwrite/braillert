from setuptools import setup, find_packages

requirements = [
    "rich ~= 12.4.4",
    "pillow ~= 9.1.1",
    "colorama ~= 0.4.4"
]


setup(
    name="braillert",
    version="2.0.1",
    packages=find_packages("src"),
    package_dir={'': "src"},
    include_package_data=True,
    author="ov3rwrite",
    author_email="ilyabelykh123@gmail.com",
    install_requires = requirements,
    url="https://github.com/ov3rwrite/braillert",
    license="MIT",
    entry_points = {
        'console_scripts': [
            'braillert = braillert.main:main',
        ],
    }
)
