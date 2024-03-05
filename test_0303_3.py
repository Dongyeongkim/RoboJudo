import gym
import gym_examples

# Specify the render mode at environment creation for visualization
env = gym.make("gym_examples/Ant-v0", render_mode='human')

observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()  # Take a random action
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()

    env.render()  # This line might be optional depending on the version of gymnasium

env.close()
