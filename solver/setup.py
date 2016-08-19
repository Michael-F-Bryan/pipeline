from setuptools import setup

setup(
        name='solver',
        author='Michael F Bryan',
        author_email='michaelfbryan@gmail.com',
        version='0.1.0',
        license='MIT',

        packages=['solver'],

        install_requires=[
            'pytest',
            'sympy',
            ],
        )
