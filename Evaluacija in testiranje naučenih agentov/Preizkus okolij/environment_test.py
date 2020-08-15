import gym

import time

import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('../')

# env_name = 'MountainCarExtended-v0'
# env_name = 'MountainCar-v0'
# env_name = 'CartPole-v1'
# env_name = 'CartPole-v2'
env_name = 'CartPole-v3'
# env_name = 'CartPole-v4'
# env_name = 'CartPole-v5'

env = gym.make(env_name, mode='test', seed=462388, use_keyboard=True)

env.reset()

for e in range(10000):
    env.render()
    # env.step(env.action_space.sample())
    # env.step(0)
    env.step(1)
    # env.step(2)
    # print(f'state = {env.state}')
    # env.step(e % 2)
    # time.sleep(0.5)

env.close()
