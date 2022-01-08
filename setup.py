# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


MINIMAL_DESCRIPTION = '''Samila is a generative art generator written in Python, Samila let's you create arts based on many thousand points. The position of every single point is calculated by a formula, which has random parameters. Because of the random numbers, every image looks different.'''


def get_requires():
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return MINIMAL_DESCRIPTION


setup(
    name='samila',
    packages=['samila'],
    version='0.4',
    description='Generative ART',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Sepand Haghighi',
    author_email='info@4r7.ir',
    url='https://github.com/sepandhaghighi/samila',
    download_url='https://github.com/sepandhaghighi/samila/tarball/v0.4',
    keywords="generative-art art nft file nft-storage",
    project_urls={
        'Source': 'https://github.com/sepandhaghighi/samila',
        'Tracker': 'https://github.com/sepandhaghighi/samila/issues',
        'Discord': 'https://discord.com/invite/94bz5QGZWb',
    },
    install_requires=get_requires(),
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Games/Entertainment',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: 3D Modeling',
        'Topic :: Multimedia :: Graphics :: 3D Rendering',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    license='MIT',
    include_package_data=True
)
