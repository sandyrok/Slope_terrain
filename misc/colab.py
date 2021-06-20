


"""
import gym
env = gym.make("CartPole-v1")
observation = env.reset()
for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  observation, reward, done, info = env.step(action)

  if done:
    observation = env.reset()
env.close()

"""



















import gym
import numpy as np
import matplotlib.pyplot as plt








env = gym.make("CartPole-v0")
env.reset()
prev_screen = env.render(mode='rgb_array')

for i in range(5000):
  action = env.action_space.sample()
  obs, reward, done, info = env.step(action)
  screen = env.render(mode='rgb_array')


  if done:
    env.reset()

env.close()


