from setuptools import setup

setup(name="Gaussian_Elimination_Libraries",
      version="1.1",
      packages=['uGauss'],#called uGauss because it's a super small AND scalable version to ANY variable amount (e.g: 3 term elim, 4 term, 5 term, 150003 terms...)
      install_requires=['numpy>=2.2.5'],
      author="YusufA442",
      author_email="yusuf365820@gmail.com",
      license='Creative Commons Attribution-Noncommercial-Share Alike license',
      long_description=open('readme.txt').read())