name = 'sour-cereal'
version = '2.0.0a'

author = 'Carlos Alberto Duarte Pinto'
author_email = 'carlos.adpinto@gmail.com'

keywords = ['abstraction', 'data extraction', 'data sources', 'interface',
            'etl', 'pep-249']

description = (
    'Utility library for writing data extractors that comply with PEP-249'
)

url = 'https://github.com/CarlosAdp/sour-cereal'

download_url = url + f'/archive/v{version}.tar.gz'

install_requires = [
    'open-close-mixin>=1.0.0'
]

classifiers = [
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Operating System :: OS Independent',
    'Topic :: Utilities',
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers'
]

license = 'MIT'
