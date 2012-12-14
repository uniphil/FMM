from setuptools import setup

readme = open('README.txt').read()
setup(name='FMM',
      version='0.12',
      author='Philip Schleihauf',
      author_email='uniphil@gmail.com',
      license='Public Domain',
      description='Numerical Computations',
      long_description=readme,
      ulr='https://github.com/uniphil/FMM',
      py_modules=['fmm'])
