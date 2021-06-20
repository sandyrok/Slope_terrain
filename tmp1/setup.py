
from setuptools import setup

setup(name='gym_stoch2_sloped_terrain',
      version='0.0.1',
      python_requires= '~=3.6',
      install_requires=['gym~=0.17.2','pybullet','sklearn','matplotlib','fabulous','dataclasses','tensorflow>=1.8.0,<2.0',
        'mpi4py']  # And any other dependencies foo needs
)
