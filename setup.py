import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="xivapi",
    version="0.1.0",
    author="Elton H.Y. Chou",
    author_email="plscd748@gmail.com",
    license="MIT",
    description="xivapi library",
    keywords='xivapi ffxiv ff14 xiv eorzea',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EltonChou/xivapi-python",
    packages=setuptools.find_packages(),
    install_requires=['request'],
    python_requires='>=3.6.0',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Bug Reports': 'https://github.com/EltonChou/xivapi-python/issues',
        'Source': 'https://github.com/EltonChou/xivapi-python',
        'Thanks!': 'https://xivapi.com',
    },
)
