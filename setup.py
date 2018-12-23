from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("learn_mnist.py", annotate = True)
)
