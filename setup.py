import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.py', '*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.blawx',
      version='0.0.1',
      description=('A module to allow docassemble interviews to run Blawx code on the Blawx Reasoner over API.'),
      long_description=u'# docassemble-blawx\r\nA module for connecting Docassemble interviews to Blawx.com\r\n\r\n## Installation\r\nGo into the packages section of your docassemble server and enter the github address for\r\nthis package.  See the [docassemble documentation](https://docassemble.org/docs)\r\nfor details.\r\n\r\n## Usage\r\n1. Include docassemble.blawx as a module in your interview.\r\n```\r\nmodules:\r\n  - docassemble.blawx\r\n```\r\n2. Create a object with the type Blawx in your interview.\r\n```\r\nobjects:\r\n  - reasoner: Blawx\r\n```\r\n3. Save your Blawx source code to a file, and upload that file to the static folder of \r\n   your docassemble server.\r\n   See the [docassemble documentation](https://docassemble.org/docs) for details.\r\n4. Call the ask() method of the Blawx object you created.\r\n```\r\n  answer = reasoner.ask(\'filename.blawx\')\r\n```\r\n5. Use the output of the ask() method to read the answer from the Blawx.com Reasoner.\r\n\r\n## The Docassemble Data Structure\r\nWhen you use this module, the interview data is sent to the Blawx Reasoner, where it is\r\nconverted for use in Blawx Code.  The docassemble interview data will be converted\r\ninto a "data dictionary", with "data" as the name of the root object.\r\n\r\nFor example, if you have a variable named "foo", that will appear in Blawx as an object\r\nnamed "data", with a data property named "foo", set to the value of "foo".\r\n\r\nNested objects, such as docassemble\'s DAList and elements, will be represented as\r\nnested data dictionaries. Only the root of the dictionary is a named object.\r\n\r\n## The Blawx Response Structure\r\nBlawx\'s response is in the following format:\r\n```\r\n{\r\n  \'main\': \'Yes\' (or \'No\'),\r\n  \'answers\': {\r\n    \'1\': {\r\n      \'variable\': value,\r\n      ...\r\n    }\r\n    ...\r\n  }\r\n}\r\n```\r\nIf the query is a yes/no query, only \'main\' will be returned. If the query is a search\r\nand no results are returned, only \'main\' will be returned with a value of \'No\'.\r\nIf it is a search and there are results, \'main\' and \'answers\' will be included.\r\n\r\n  \r\n\r\nSee the Blawx.com documentation for more information on how to write Blawx code that is\r\nable.',
      long_description_content_type='text/markdown',
      author='Jason Morris',
      author_email='jason@roundtablelaw.ca',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/blawx/', package='docassemble.blawx'),
     )

