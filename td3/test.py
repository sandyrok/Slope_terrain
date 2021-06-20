import td3
import tensorflow as tf
import gym
import core as core
import sys, os


import inspect

# Importing the libraries
import os
import numpy as np
import gym
import gym_sloped_terrain.envs.stoch2_pybullet_env as e
from gym import wrappers
import time
import multiprocessing as mp
from multiprocessing import Process, Pipe
import argparse
import math
#Utils
from utils.logger import DataLog
from utils.make_train_plots import make_train_plots_ars
import random
#Registering new environments
from gym.envs.registration import registry, register, make, spec


#Rendering

import matplotlib.pyplot as plt
#from IPython import display as ipythondisplay




#Stoch 2 Test imports
import pybullet as p 
import numpy as np
PI = math.pi
# Setting the Hyper Parameters
import math
PI = math.pi


register(id='Stoch2-v0',entry_point='gym_sloped_terrain.envs.stoch2_pybullet_env:Stoch2Env', kwargs = {'gait' : 'trot', 'render': False, 'action_dim': 20, 'stairs': 0} )

env_fn = lambda : gym.make('Stoch2-v0')
#l = [[20],[40],[60],[20,20],[100],[200],[300]]
#l = [[40],[60],[20,20],[100],[200],[300]]
l = [[20,20]]
logger_kwargz = dict(output_dir='path/to/output_dir', exp_name='experiment_name')	
for x in l:
 td3.td3(env_fn,actor_critic=core.mlp_actor_critic,ac_kwargs=dict(hidden_sizes=x),gamma=0.99,seed=0,steps_per_epoch=5000, max_ep_len=400,epochs=50,logger_kwargs=logger_kwargz) 
