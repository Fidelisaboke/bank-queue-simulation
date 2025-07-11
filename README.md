# Bank Queue Simulation: Single Server System
## Project Overview
This project simulates a single-server queue system for a bank, using discrete-event simulation in 
Python. The simulation models customer arrivals and services, operating under a FIFO 
(First-In, First-Out) queuing discipline. It is designed to help analyze key performance metrics and 
understand customer flow dynamics.

## Assumptions
- Customers arrive randomly with inter-arrival times uniformly distributed between 1 and 8 minutes.
- Service times are uniformly distributed between 1 and 6 minutes.
- Only one server is available.
- The queue follows FIFO discipline.

## Installation and Setup
### Prerequisites
- Python 3.12+

### Setup Instructions
- Clone the repository:
```bash
https://github.com/Fidelisaboke/bank-queue-simulation.git
cd bank-queue-simulation
```

- Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate # ON Linux or macOS
.venv\Scripts\activate    # On Windows OS
```

- Install dependencies:
```bash
pip install -r requirements.txt
```

## Basic Usage
- Run the `main.py` file in `src`:
```bash
cd src
python main.py
```
This will:
- Generate random inter-arrival and service times for 500 customers.
- Simulate customer flow through the bank.
- Output a CSV file with arrival, service, start, end, and waiting times.


