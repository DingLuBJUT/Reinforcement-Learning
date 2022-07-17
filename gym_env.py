"""
https://blog.paperspace.com/getting-started-with-openai-gym/
"""

import gym
import time
import warnings
warnings.filterwarnings('ignore')

step_nums = 100
env = gym.make("MountainCar-v0")
env.reset()
for i in range(step_nums):
    action = env.action_space.sample()
    obs, reward, done, _ = env.step(action)
    env.render(mode = 'human')
    time.sleep(0.5)
    if done:
        env.reset()
env.close()
