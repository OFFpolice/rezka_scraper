# setup.py

from setuptools import setup, find_packages

setup(
    name='rezka_scraper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'beautifulsoup4',
    ],
    description='RezkaScraper — это библиотека на Python для асинхронного поиска контента (аниме, фильмов, сериалов и мультфильмов) на сайте Rezka.',
    author='OFFpolice',
    author_email='offpolice2077@gmail.com',
    url='https://github.com/OFFpolice/rezka_scraper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
