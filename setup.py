from setuptools import setup

setup(
    name='game_of_life',
    version='0.1',
    py_modules=['life_driver', 'model'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        game_of_life=life_driver:main
    ''',
)