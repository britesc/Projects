 from setuptools import setup

 setup(
   name='Projectionist',
   version='0.0.0',
   author='J2 Casa',
   author_email='apps@j2casa.com',
   packages=['Projectionist', ''],
   scripts=['[]','[]'],
   url='',
   license='LICENSE.txt',
   description='A Multi Priject Setup and Configuration Tools',
   long_description=open('README.txt').read(),
   install_requires=[
       "PySide6 >= 6.0.0",
       "darktheme",
   ],
)