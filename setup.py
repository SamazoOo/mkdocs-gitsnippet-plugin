import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='mkdocs-gitsnippet-plugin',
    version='1.2.0',
    description='Mkdocs plugin that allow to inject snippet or all markdown content from a given remote git repository.',
    long_description=read('README.md'),
    keywords='mkdocs python markdown snippet git',
    url='https://github.com/SamazoOo/mkdocs-gitsnippet-plugin',
    author='Samuel Comino',
    author_email='samuel.covi@gmail.com',
    license='MIT',
    python_requires='>=2.7.9,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=['mkdocs>=0.17', 'gitpython'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': ['gitsnippet = gitsnippet.plugin:GitSnippetPlugin']
    })
