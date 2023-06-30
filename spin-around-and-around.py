import gym
import minerl
import logging
import coloredlogs
coloredlogs.install(logging.DEBUG)

env = gym.make("MineRLBasaltBuildVillageHouse-v0")
obs = env.reset()

done = False
while not done:
    ac = env.action_space.no_op()
    # Spin around to see what is around us
    ac["camera"] = [0, 3]
    obs, reward, done, info = env.step(ac)
    env.render()
env.close()