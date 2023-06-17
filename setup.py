from distutils.core import setup
import py2exe

# to build, `python setup.py py2exe`
setup(
    console=['main.py'],
    name='AP YAML Combiner',
    scripts=['main.py'],
)
