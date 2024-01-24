import os

from setuptools import setup, find_packages


def parse_requirements(req_file):
    with open(req_file) as fp:
        _requires = fp.read()
    return _requires


NAME = "pellipop"
VERSION = "0.4.3"

# Get dependencies from requirement files
SETUP_REQUIRES = ['setuptools', 'setuptools-git', 'wheel']
INSTALL_REQUIRES = parse_requirements('requirements.txt')
LONG_DESCRIPTION = ""

with open(os.path.join(os.path.dirname(__file__), 'readme.md'), 'r') as f:
    LONG_DESCRIPTION = f.read()


def setup_package():
    metadata = dict(name=NAME,
                    version=VERSION,
                    license='MPL-2.0 license',
                    install_requires=INSTALL_REQUIRES,
                    long_description=LONG_DESCRIPTION,
                    long_description_content_type='text/markdown',
                    setup_requires=SETUP_REQUIRES,
                    entry_points={
                        'console_scripts': [
                            'pellipop = pellipop.gui:main',
                            'pellipop-cli = pellipop.cli:main'
                        ]
                    },
                    packages=find_packages())

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
