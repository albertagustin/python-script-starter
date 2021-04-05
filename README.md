# Python Script Starter

A simple starter for a python script that I use for my projects that integrates pytest and the ability to install as a command line utility.

## Setup

1. Install python & pipenv

2. Install python environment/pkgs and enable the shell

   ```bash
   pipenv install --dev

   pipenv shell
   ```

3. Run the tests

   ```bash
   pytest tests/

   # OR
   python setup.py test

   >>
    running pytest
    running egg_info
    writing src/my_script.egg-info/PKG-INFO
    writing dependency_links to src/my_script.egg-info/dependency_links.txt
    writing entry points to src/my_script.egg-info/entry_points.txt
    writing top-level names to src/my_script.egg-info/top_level.txt
    reading manifest file 'src/my_script.egg-info/SOURCES.txt'
    writing manifest file 'src/my_script.egg-info/SOURCES.txt'
    running build_ext
    ================================================================================================= test session starts =================================================================================================
    platform darwin -- Python 3.9.2, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
    rootdir: /Users/albertagustin/git/albertagustin/python-script-starter
    collected 1 item

    tests/unit/test_myscript.py .
   ```

4. Install, run the script as an editable cmd line utility

   ```bash
   pipenv install -e .

   my-script

   >>
    Hello World!
   ```
