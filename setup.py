import os
from setuptools import setup, find_packages

def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''
setup(
    name='norilog',
    version = '1.0.0',
    description = 'The NOrilog web application',
    long_description = read_file('README.rst'),
    author = '<あなたの名前>',
    author_email='<あなたのメールアドレス>',
    url ='https://github.com/<あなたのGithubアカウント>/norilog/',
    classifiers = [
        'Development Status :: 4 -Bata',
        'Framework :: Flask '
        'License :: OSI approved :: BSD License',
        'Programing Language :: Python',
        'Programing Language :: Python :: 3.6',
    ],
    packages = find_packages(),
    include_package_data = True,
    keywords = ['web', 'norilog'],
    license = 'BSD License',
    install_requires = [
     'Flask',
    ],
    entry_points="""
        [console_scripts]
        norilog = norilog:main
    """,
)
