from setuptools import setup


setup(
    name='elasticsearch_loader',
    version='0.1',
    py_modules=['elasticsearch_loader'],
    url='',
    license='',
    description='',
    install_requires=[
        'elasticsearch',
        'click',
        'futures',
    ],
    entry_points={
        'console_scripts': [
            'elasticsearch_loader = elasticsearch_loader:cli',
        ]
    }
)
