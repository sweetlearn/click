from setuptools import setup, find_packages

setup(
    name='yourpackage',
    version='0.1',
    packages=find_packages(),
    py_modules=["colors"],
    include_package_data=True,
    install_requires=[
        "click",
        # Colorama is only required for Windows.
        "colorama",
    ],
    entry_points="""
        [console_scripts]
        colors=colors:cli
        # yourscript=yourpackage.scripts.yourscript:cli
    """,
)
