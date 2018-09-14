from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='yiyuLibs',
      version='0.1',
      description='Yiyu\'s collection of Python utility code',
      url='http://unknown',
      author='Yiyu Jia',
      author_email='yiyu.jia@BostonInfoPro.com',
      license='private',
      packages=['yiyuUtil'],
      install_requires=[
          'pandas',
      ],
      zip_safe=False)
