from distutils.core import setup

setup(
    name='blingjson',
    version='0.1.1',
    author='Jessica Sachs',
    author_email='jess@sheeptest.com',
    packages=['blingjson'],
    scripts=['bin/example.py','bin/blingy_example.py'],
    url='http://pypi.python.org/pypi/blingjson/',
    downloadUrl='https://github.com/jessicasachs/blingjson/tarball/0.1.1',
    license='LICENSE.txt',
    description='Module for colorful JSON syntax highlighting. With emoji bling.',
    install_requires=[
        "Pygments==2.0.2",
        "emoji==0.1.0",
        "termcolor==1.1.0",
        "wsgiref==0.1.2"
    ],
)