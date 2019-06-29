from setuptools import setup, find_packages
import re
from os import path

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()
  
this_directory = path.abspath(path.dirname(__file__))
readme = ''
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCR = f.read()

extras_require = {
    'voice': ['PyNaCl==1.3.0'],
    'docs': [
        'sphinx==1.7.4',
        'sphinxcontrib-asyncio',
        'sphinxcontrib-websupport',
    ]
}

setup(name='team-game',
      author='TFI',
      url='https://github.com/tfi-nerds/team-game',
      project_urls={
        "Documentation": "https://team-game.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/tfi-nerds/team-game",
      },
      version= '1.4',
      packages = ['tfidotabot', 'tfidotabot.ext.commands', 'tfidotabot.ext.tasks', 'tfidotabot.src'],
      package_data = {'tfidotabot.ref': ['abilities.json','heroes.json','items.json','meta.json']},
      license='GPL-3.0',
      description='A python wrapper for the Discord and DOTA 2 API',
      long_description=readme,
      long_description_content_type="text/x-rst",
      include_package_data=True,
      install_requires=requirements,
      extras_require=extras_require,
      python_requires='>=3.5.3',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
