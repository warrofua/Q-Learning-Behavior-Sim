## Overview


This is a simulation model that uses Q-learning to adapt the behavior of an organism based on its internal states and output the results as a gif to view the changes over time.

Roughly speaking, this python app will do the following:

Utilize:

get_reward: Calculates the reward for a behavior based on the current states.

update_states: Updates the internal states of the organism after a given behavior is performed.

Run a loop from the start time to the end time, incrementing the time in defined steps.

In each iteration, decide the behavior based on the epsilon-greedy strategy (choose randomly or based on the highest Q-value).

Update the Q-table based on the received reward.

Record the state and behavior proportions at each time step.

Use Matplotlib to create plots showing the changes in states and behaviors over time.

Save each plot as an image frame using PIL. 
Create and Save GIF: Combine the saved image frames into a GIF to visualize the behavior changes over time.

A slow learner (Alpha = 0.4)
![Behavior_Simulation_20231203181305_alpha_0 4_gamma_0 7_epsilon_0 8](https://github.com/warrofua/Q-Learning-Behavior-Sim/assets/41028474/6300f9ff-5f08-41f4-8084-c9ba8d3ab4b7)

A fast learner (Alpha = 0.99)
![Behavior_Simulation_20231205180758_alpha_0 99_gamma_0 7_epsilon_0 8](https://github.com/warrofua/Q-Learning-Behavior-Sim/assets/41028474/8e78c598-030c-4823-9ba0-9c73cdabc2fe)


## Features

- Adaptive Behavior based on internal states
- Q-learning algorithm for decision-making
- Time-series data for behavior and state tracking

## Requirements

- Python 3.x
- Pandas
- Matplotlib
- Pillow
- Numpy

You can install the required packages using:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the GNU General Public License (GPL-3.0) - see the LICENSE file for details.

