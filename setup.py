from setuptools import setup, find_packages


setup(
    name='leo',
    version='1.0',
    description='dict.leo.org',
    long_description='Leo Dictionary',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='leo',
    author='Tobias Rueetschi',
    author_email='tr@brief.li',
    url='https://github.com/keachi/pyleo',
    license='GPLv3',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
        'python-vlc',
    ],
    extras_require={
    },
    entry_points="""
    [console_scripts]
    leo=leo:main
    train=train:main
    """
)