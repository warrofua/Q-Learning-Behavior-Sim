# Q Learning Whale Simulation

## Overview

Q Whale is a simulation model that uses Q-learning to adapt the behavior of an organism (in this case, a whale) based on its internal states such as hunger, boredom, loneliness, and tiredness.

## Features

- Adaptive Behavior based on internal states
- Q-learning algorithm for decision-making
- Monte Carlo elements for randomness
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

3. Run the `main.py` script to start the simulation:

   ```bash
   python src/main.py
   ```

## Output

The output will be a time-series plot showing the proportion of time spent in each behavior and the corresponding internal states.

## License

This project is licensed under the GNU General Public License (GPL-3.0) - see the LICENSE file for details.

## Acknowledgements

- Inspired by the behavior of real-world organisms
- Q-learning and Monte Carlo methods for decision-making

