from setuptools import setup

setup(name='base-python-script',
      version='0.1',
      description='Base Python Script',
      url='https://github.gapinc.com/aagusti/base-python-script',
      author='Albert Agustin',
      author_email='albert_agustin@gap.com',
      license='MIT',
      packages=['src.base_python_script'],
      setup_requires=["pytest-runner"],
      tests_require=["pytest"],
      zip_safe=False)
