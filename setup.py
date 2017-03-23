#from distutils.core import setup
from setuptools import setup


setup(
    name = 'selenium_components',
    packages = ['selenium_components'], # this must be the same as the name above
    version = '0.1',
    description = 'Page objects for common components',
    author = 'Jernej Makovsek',
    author_email = 'jernej.makovsek@gmail.com',
    url = 'https://github.com/defactto/selenium-components', # use the URL to the github repo
    download_url = 'https://github.com/defactto/selenium-components/archive/0.1.tar.gz',
    keywords = ['testing', 'selenium', 'utils', 'webdriver', 'components', 'selenium-components'], # arbitrary keywords
    license = 'Apache 2.0',
    install_requires=['selenium', 'selenium-utils'],
    classifiers = [
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',


        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],
)