import random
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
from PIL import Image
import numpy as np

# Initialize Q-table
'''The Q-table is initialized with behaviors (Feeding, Exploring, etc.) as keys and their values set to 0. 
The Q-table essentially maps behaviors to "values" that indicate how good each behavior is, given the current state.'''
behaviors = ["Feeding", "Exploring", "Socializing", "Resting"]
Q = {behavior: 0 for behavior in behaviors}

# Parameters
alpha = 0.9 # learning rate (how fast organism modifies future behaviors in response to rewards, 0.1 = slow, 0.9 = fast)
gamma = 0.7  # discount factor (how much the organisms "weighs" future rewards vs. immediate rewards, immediate = 0.1, future = 0.9)
epsilon = 0.8  # exploration rate (how "focused" the organism is, or do they not really care for rewards.  0.1 = aloof, 0.9 = adept)

# Initial counts and time-series
behavior_counts = {behavior: 0 for behavior in behaviors}
state_time_series = []
behavior_time_series = []

# Time
start_time = datetime.now()
current_time = start_time
end_time = start_time + timedelta(weeks=2)
time_increment = timedelta(hours=1)

# States
'''This line initializes the internal states (hunger, boredom, etc.) of the organism randomly. 
These states influence the behavior of the organism.'''
states = {'Hunger': random.random(), 'Boredom': random.random(), 'Loneliness': random.random(), 'Tiredness': random.random()}

# 1. Expand the stateObj to include all states and their associated behaviors.
stateObj = {
    'Hunger': {'Q': random.random(), 'rewardRange': (0, 1), 'behavior': 'Feeding'},
    'Boredom': {'Q': random.random(), 'rewardRange': (0, 1), 'behavior': 'Exploring'},
    'Loneliness': {'Q': random.random(), 'rewardRange': (0, 1), 'behavior': 'Socializing'},
    'Tiredness': {'Q': random.random(), 'rewardRange': (0, 1), 'behavior': 'Resting'}
}

# 2. Modify the get_reward function to use the get_reward2 methodology.
def get_reward(behavior, states):
    for state, attributes in stateObj.items():
        if attributes['behavior'] == behavior:
            return random.uniform(*attributes['rewardRange'])
    return 0  # Default reward if no match (shouldn't happen)

# Update state function
def update_states(behavior, states):
    for state in states:
        states[state] += random.uniform(.01, 0.2)
        states[state] = max(0, states[state])

    if behavior == "Feeding":
        states['Hunger'] -= random.uniform(0.01, 0.8)
    elif behavior == "Exploring":
        states['Boredom'] -= random.uniform(0.01, 0.8)
    elif behavior == "Socializing":
        states['Loneliness'] -= random.uniform(0.01, 0.8)
    elif behavior == "Resting":
        states['Tiredness'] -= random.uniform(0.01, 0.8) # represent volitilty of the state

    for state in states:
        states[state] = min(1, max(0, states[state]))

# Time
time_increment = timedelta(days=.1)  # Change to one day per frame

# Create a list to store the frames
frames = []

# Simulation
'''In each time step, the organism has a chance (epsilon) of picking a behavior randomly. 
Otherwise, it chooses the behavior that has the highest Q-value.'''
while current_time <= end_time:
    if random.random() < epsilon:
        behavior = random.choice(behaviors)
    else:
        max_state = max(stateObj, key=lambda k: stateObj[k]['Q'])
        behavior = stateObj[max_state]['behavior']
    
    reward = get_reward(behavior, states)
    
    for state, attributes in stateObj.items():
        if attributes['behavior'] == behavior:
            attributes['Q'] = (1 - alpha) * attributes['Q'] + alpha * (reward + gamma * max([s['Q'] for s in stateObj.values()]))
    
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

    # Add space at the bottom for the annotation
    plt.subplots_adjust(bottom=0.2)

    # Add parameters as annotations below x-axis
    param_str = f"alpha={alpha}, gamma={gamma}, epsilon={epsilon}"
    ax1.annotate(param_str, xy=(0.5, -0.2), xycoords='axes fraction', ha='center', fontsize=12)

    ax1.grid(True)

        # Convert the plot to an image and add it to frames
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8').reshape(fig.canvas.get_width_height()[::-1] + (3,))
    frames.append(Image.fromarray(image))

    plt.close(fig)  # Close the plot to free up memory
        
    current_time += time_increment

# Create a GIF from the frames 
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
gif_filename = f"Behavior_Simulation_{timestamp}_alpha_{alpha}_gamma_{gamma}_epsilon_{epsilon}.gif"
frames[0].save(gif_filename, save_all=True, append_images=frames[1:], loop=0, duration=200)


print(f"Saved GIF as {gif_filename}")