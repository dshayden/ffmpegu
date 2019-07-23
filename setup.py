from setuptools import setup

def readme():
  with open('README.rst') as f:
    return f.read()

setup(name='ffmpegu',
  version='0.2',
  description='Data handling utilities',
  long_description=readme(),
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
  keywords='ffmpeg utility',
  url='',
  author='David S. Hayden',
  author_email='dshayden@mit.edu',
  license='MIT',
  packages=['ffmpegu'],
  install_requires=['numpy', 'du'],
  include_package_data=True,
  zip_safe=False)
