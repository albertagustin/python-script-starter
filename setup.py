from setuptools import setup

setup(name='my-script',
      version='0.1',
      description='Base Python Script',
      url='https://github.gapinc.com/aagusti/base-python-script',
      author='Albert Agustin',
      author_email='albert_agustin@gap.com',
      license='MIT',
      package_dir={'': 'src'},
      packages=['myscript'],
      setup_requires=["pytest-runner"],
      tests_require=["pytest"],
      zip_safe=False,
      entry_points={
          'console_scripts': ['my-script=myscript.command_line:main']
      })
