from distutils.core import setup

setup(
    name='blingjson',
    version='0.1.0',
    author='Jessica Sachs',
    author_email='jess@sheeptest.com',
    packages=['blingjson'],
    scripts=['bin/example.py','bin/blingy_example.py'],
    url='http://pypi.python.org/pypi/blingjson/',
    license='LICENSE.txt',
    description='',
    long_description=open('README.md').read(),
    install_requires=[
        "Pygments==2.0.2",
        "emoji==0.1.0",
        "termcolor==1.1.0",
        "wsgiref==0.1.2"
    ],
)