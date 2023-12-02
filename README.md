# Q Learning Simulation

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


## Features

- Adaptive Behavior based on internal states
- Q-learning algorithm for decision-making
- Time-series data for behavior and state tracking

## Requirements

- Python 3.x
- Pandas
- Matplotlib
- Datetime

You can install the required packages using:

```bash
pip install -r requirements.txt
```

## How to Run

1. Clone this repository.
2. Navigate to the project directory and install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the `q_whale.py` script to start the simulation:

   ```bash
   python src/q_whale.py
   ```

## Output

The output will be a time-series plot showing the proportion of time spent in each behavior and the corresponding internal states.

## License

This project is licensed under the GNU General Public License (GPL-3.0) - see the LICENSE file for details.

