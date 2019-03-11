from setuptools import setup

setup(
    name='plantpredict',
    version='0.6.0',
    description='Python 2.7 SDK for PlantPredict (https://ui.plantpredict.com).',
    url='http://github.com/storborg/funniest',
    author='Stephen Kaplan, Performance & Prediction Engineer at First Solar, Inc.',
    author_email='',
    license=None,
    packages=['plantpredict'],
    install_requires=[
        'requests',
        'pandas'
    ],
    zip_safe=False
)
