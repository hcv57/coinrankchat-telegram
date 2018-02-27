from setuptools import setup

setup(
    name='coinrankchat-telegram',
    packages=['coinrankchat.telegram'],
    include_package_data=True,
    install_requires=[
        'boto3',
        'elasticsearch-dsl',
        'requests',
        'requests-cache',
        'telethon==0.17.2.1'
    ]
)
