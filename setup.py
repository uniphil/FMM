from setuptools import setup

readme = open('README.txt').read()
setup(name='FMM',
      version='0.1',
      author='Philip Schleihauf',
      author_email='uniphil@gmail.com',
      license='Public Domain',
      description='Numerical Computations',
      long_description=readme,
      py_modules=['fmm'])
