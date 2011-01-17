# -*- coding: utf-8 -*-
#quckstarted Options:
#
# sqlalchemy: True
# auth:       sqlalchemy
# mako:       False
#
#

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='eventstreamexamples',
    version='0.1',
    description='Examples on how to use server-side events with Turbogears/Pylons',
    author='Niklas Hambüchen',
    author_email='nh2@deditus.de',
    #url='',
    install_requires=[
        "TurboGears2 >= 2.1",
		"gunicorn >= 0.12.0",
		"gevent >= 0.13.1",
        ],
    setup_requires=["PasteScript >= 1.7"],
    paster_plugins=['PasteScript', 'Pylons', 'TurboGears2'],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    package_data={'eventstreamexamples': [
                                 'templates/*/*',
                                 'public/*/*']},

    entry_points="""
    [paste.app_factory]
    main = eventstreamexamples.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
