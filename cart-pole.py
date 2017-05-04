import gym
env = gym.make('CartPole-v0')
for i_episode in range(1):
    #reset: returns an initial observation 
    observation = env.reset()
    for t in range(10):
        env.render()
        print(observation)
        action = env.action_space.sample()
        #step() function returns 4 values
        #observation:[object] environment-specific object representing
        #             the observation of the environement
        #reward:[float] amounto of reward achieved by the previous action
        #done:[boolean] True--episode terminates, reset the environment 
        #info: [dict] diagnostic info for debugging 
        observation, reward, done, info = env.step(action)
        print "observation", observation
        print "reward", reward
        print "done", done
        print "info", info 
        print "t", t
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break