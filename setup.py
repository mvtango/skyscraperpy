import setuptools
from skyscraper.version import Version


setuptools.setup(name='skyscraper',
                 version=Version('0.0.1').number,
                 description='Python Client for Skyscraper framework',
                 long_description=open('README.md').read().strip(),
                 author='Martin Virtel',
                 author_email='mv@datenfreunde.de',
                 url='https://github.com/mvtango/skyscraperpy',
                 py_modules=['skyscraper'],
                 install_requires=['requests','simplejson'],
                 license='Apache License',
                 zip_safe=False,
                 keywords='Skyscraper Scraping Monitoring',
                 classifiers=['Packages', ])
