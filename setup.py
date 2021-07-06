import os
from importlib.machinery import SourceFileLoader

from pkg_resources import parse_requirements
from setuptools import find_packages, setup


module_name = 'app'

# Module may not be installed or installed another version,
# so loading __init__.py with machinery.
module = SourceFileLoader(
    module_name, os.path.join(module_name, '__init__.py')
).load_module()


def load_requirements(fname: str) -> list:
    requirements = []
    with open(fname, 'r') as fp:
        for req in parse_requirements(fp.read()):
            extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
            requirements.append(
                '{}{}{}'.format(req.name, extras, req.specifier)
            )
    return requirements


setup(
    name=module_name,
    version=open('VERSION').read().strip(),
    description=module.__doc__,
    long_description=open('README.md').read(),
    platforms='all',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7.3',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    python_requires='>=3.7',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            f'tbot = {module_name}.__main__:main',
        ]
    },
    include_package_data=True
)
