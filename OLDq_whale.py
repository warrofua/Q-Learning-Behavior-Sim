import random
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# Initialize Q-table
'''The Q-table is initialized with behaviors (Feeding, Exploring, etc.) as keys and their values set to 0. 
The Q-table essentially maps behaviors to "values" that indicate how good each behavior is, given the current state.'''
behaviors = ["Feeding", "Exploring", "Socializing", "Resting"]
Q = {behavior: 0 for behavior in behaviors}

# Parameters
alpha = 0.5 # learning rate (how fast organism modifies future behaviors in response to rewards, 0.1 = slow, 0.9 = fast)
gamma = 0.9  # discount factor (how much the organisms "weighs" future rewards vs. immediate rewards, immediate = 0.1, future = 0.9)
epsilon = 0.7  # exploration rate (how "focused" the organism is, or do they not really care for rewards.  0.1 = aloof, 0.9 = adept)

# Initial counts and time-series
behavior_counts = {behavior: 0 for behavior in behaviors}
state_time_series = []
behavior_time_series = []

# Time
start_time = datetime.now()
current_time = start_time
end_time = start_time + timedelta(weeks=1)
time_increment = timedelta(hours=3)

# States
'''This line initializes the internal states (hunger, boredom, etc.) of the whale randomly. 
These states influence the behavior of the whale.'''
states = {'Hunger': random.random(), 'Boredom': random.random(), 'Loneliness': random.random(), 'Tiredness': random.random()}

# Reward function
def get_reward(behavior, states):
    return {
        "Feeding": states['Hunger'],
        "Exploring": states['Boredom'],
        "Socializing": states['Loneliness'],
        "Resting": states['Tiredness']
    }[behavior]

# Update state function
def update_states(behavior, states):
    for state in states:
        states[state] += random.uniform(.01, 0.1)
        states[state] = max(0, states[state])

    if behavior == "Feeding":
        states['Hunger'] -= random.uniform(0.01, 0.5)
    elif behavior == "Exploring":
        states['Boredom'] -= random.uniform(0.01, 0.5)
    elif behavior == "Socializing":
        states['Loneliness'] -= random.uniform(0.01, 0.5)
    elif behavior == "Resting":
        states['Tiredness'] -= random.uniform(0.01, 0.5)

    for state in states:
        states[state] = min(1, max(0, states[state]))

# Simulation
'''In each time step, the whale has a chance (epsilon) of picking a behavior randomly. 
Otherwise, it chooses the behavior that has the highest Q-value.'''
while current_time <= end_time:
    if random.random() < epsilon:
        behavior = random.choice(behaviors)
    else:
        behavior = max(Q, key=Q.get)
    
    '''After the behavior is chosen, the Q-value for that behavior is updated based on the reward it 
    receives. The reward is determined by the get_reward() function which depends on the current state 
    (e.g., how hungry or tired the whale is).'''
    reward = get_reward(behavior, states)
    Q[behavior] = (1 - alpha) * Q[behavior] + alpha * (reward + gamma * max(Q.values()))
    
    '''The internal states of the whale are then updated. For example, if the whale was "Feeding", 
    its hunger level would decrease.'''
    update_states(behavior, states)
    
    behavior_counts[behavior] += 1
    total_counts = sum(behavior_counts.values())
    normalized_behavior_counts = {k: v / total_counts for k, v in behavior_counts.items()}
    
    total_states = sum(states.values())
    normalized_states = {k: v / total_states for k, v in states.items()}

    state_time_series.append({
        "Timestamp": current_time,
        **normalized_states 
    })

    behavior_time_series.append({
        "Timestamp": current_time,
        **normalized_behavior_counts
    })
    
    current_time += time_increment

# DataFrames
df_states = pd.DataFrame(state_time_series)
df_states['Timestamp'] = pd.to_datetime(df_states['Timestamp'])
df_states.set_index('Timestamp', inplace=True)

df_behaviors = pd.DataFrame(behavior_time_series)
df_behaviors['Timestamp'] = pd.to_datetime(df_behaviors['Timestamp'])
df_behaviors.set_index('Timestamp', inplace=True)

# Chart
fig, ax1 = plt.subplots(figsize=(15, 6))

# State values as shaded line graphs (Left Axis)
for state in states.keys():
    ax1.plot(df_states.index, df_states[state], label=f"State: {state}", linestyle='--')
    ax1.fill_between(df_states.index, 0, df_states[state], alpha=0.2)  # Shaded region under each line

ax1.set_xlabel('Time')
ax1.set_ylabel('Proportion of State Values', color='tab:blue')  # Change axis label
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Add Right Axis for Normalized Behavior Counts
ax2 = ax1.twinx()

# Normalized behavior counts as lines (Right Axis)
for behavior in behaviors:
    ax2.plot(df_behaviors.index, df_behaviors[behavior], label=f"Behavior: {behavior}", linestyle='-')

ax2.set_ylabel('Proportion of Time Spent in Behavior', color='tab:red')  # Change axis label
ax2.tick_params(axis='y', labelcolor='tab:red')

# Labels and title
plt.title('Proportion of State Values and Behavior Engagement Over Time')  

# Add legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

ax1.grid(True)
plt.show()
