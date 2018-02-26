from distutils.core import setup

with open("README.md") as readme:
    long_description = readme.read()

try:
    import pypandoc
    long_description = pypandoc.convert(long_description, 'rst', 'markdown')
except(IOError, ImportError):
    pass

VERSION = '0.1.0'

setup(
    name='asyncmock',
    py_modules=['AsyncMock'],
    version=VERSION,
    url='https://github.com/potentbanana/asyncmock',
    download_url='https://github.com/potentbanana/asyncmock/archive/v%s.zip' % VERSION,
    keywords=['python', 'mock', 'async'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development'
    ],
    long_description=long_description,
    license='Apache License',
    author='potentbanana',
    author_email='potentbanana@nerdcorn.com',
    description='A dead simple mock for unit tests async coroutines.'
)
