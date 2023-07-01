import gym
import minerl
import logging
import coloredlogs
coloredlogs.install(logging.DEBUG)

env = gym.make("MineRLTreechop-v0")
obs = env.reset()


done = False
while not done:
    ac = env.action_space.no_op()
    # Spin around and jump to see what is around us
    ac["camera"] = [0, 3]
    ac["jump"] = [1]
    obs, reward, done, info = env.step(ac)
    env.render()
env.close()


# other ---

# odict_keys(['ESC', 'attack', 'back', 'camera', 'drop', 'forward', 'hotbar.1', 'hotbar.2', 'hotbar.3', 'hotbar.4', 'hotbar.5', 'hotbar.6', 'hotbar.7', 'hotbar.8', 'hotbar.9', 'inventory', 'jump', 'left', 'pickItem', 'right', 'sneak', 'sprint', 'swapHands', 'use'])
# print(env.action_space.no_op().keys())
