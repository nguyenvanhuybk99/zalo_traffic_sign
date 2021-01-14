import numpy
from distutils.core import setup
#from distutils.extension import Extension
from Cython.Build import cythonize
from setuptools import Extension

extensions = [
    Extension(
        "nms", 
        ["nms.pyx"],
        extra_compile_args=["-Wno-cpp", "-Wno-unused-function"]
    )
]

setup(
    name="coco",
    ext_modules=cythonize(extensions),
    include_dirs=[numpy.get_include()]
)