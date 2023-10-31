# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cleo',
 'cleo.commands',
 'cleo.commands.completions',
 'cleo.descriptors',
 'cleo.events',
 'cleo.exceptions',
 'cleo.formatters',
 'cleo.io',
 'cleo.io.inputs',
 'cleo.io.outputs',
 'cleo.loaders',
 'cleo.testers',
 'cleo.ui']

package_data = \
{'': ['*']}

install_requires = \
['crashtest>=0.4.1,<0.5.0', 'rapidfuzz>=3.0.0,<4.0.0']

setup_kwargs = {
    'name': 'cleo',
    'version': '2.1.0',
    'description': 'Cleo allows you to create beautiful and testable command-line interfaces.',
    'author': 'Sébastien Eustace',
    'author_email': 'sebastien@eustace.io',
    'maintainer': 'Branch Vincent',
    'maintainer_email': 'branchevincent@gmail.com',
    'url': 'https://github.com/python-poetry/cleo',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
