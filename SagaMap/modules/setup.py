# -*- coding: utf-8 -*-
from distutils.core import setup, Extension

setup(
    name="calculeia",
    version="1.0",
    author="Aron de Castro",
    author_email="aron.castro.coelho@gmail.com",
    ext_modules=[Extension(
        "calculeia",
        sources=['calculeia.c']
    )]
)

setup(
	name="heightmap",
	version="1.0",
	author="Aron de Casrto",
	author_email="aron.castro.coelho@gmail.com",
	ext_modules=[Extension(
		'heightmap',
		sources=['heightmap.c']
	)]
)
