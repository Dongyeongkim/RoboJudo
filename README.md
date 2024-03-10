# RoboJudo

1.  https://www.gymlibrary.dev/content/environment_creation/

2.  git clone https://github.com/Farama-Foundation/gym-examples
    cd gym-examples
    <!-- python -m venv .env -->
    <!-- if you use miniconda, you should replace bin by Sripts -->
    pip install -e .
3.  before doing pip install -e . ,
    - add the ant_env.py in the gym-examples/gym-examples/envs/
    - add the line "from gym_examples.envs.ant_env import AntEnv" in the file __init__.py which located in the gym-examples/gym-examples/envs/
    - add these lines
    "register(
        id="gym_examples/Ant-v0",
        entry_point="gym_examples.envs:AntEnv",
        max_episode_steps=1000,
        reward_threshold=6000.0,
    )"
    in the file __init__.py which located in the gym-examples/gym-examples
4.  Caution: if you have any directory which named by Korean,
    you will face the XML PARSER error
5.  you need to add the xml file


    
