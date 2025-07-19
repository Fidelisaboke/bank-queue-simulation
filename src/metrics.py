"""This module contains functions for the metrics of the queuing system."""

import pandas as pd

def compute_metrics(simulated_data):
    """
    Compute and print performance metrics from the simulated queue data.

    Parameters:
        simulated_data (DataFrame): DataFrame containing arrival time, 
        service time, start time, end time, waiting time, time in system, and idle time.

    Returns:
        metrics (dict): Dictionary containing the calculated performance metrics.
    """
    total_customers = len(simulated_data)
    total_simulation_time = simulated_data['end_time'].iloc[-1]
    total_service_time = simulated_data['service_time'].sum()
    total_waiting_time = simulated_data['waiting_time'].sum()
    total_idle_time = simulated_data['idle_time'].sum()

    avg_waiting_time = simulated_data['waiting_time'].mean()
    avg_service_time = simulated_data['service_time'].mean()
    avg_inter_arrival_time = simulated_data['inter_arrival_time'].mean()
    avg_time_in_system = simulated_data['time_in_system'].mean()
    server_utilization = total_service_time / total_simulation_time
    avg_idle_time = simulated_data['idle_time'].mean()
    max_queue_length = compute_max_queue_length(simulated_data)
    pr_wait = (simulated_data['waiting_time'] > 0).mean()
    pr_idle = total_idle_time / total_simulation_time

    metrics = {
        'Total Customers': total_customers,
        'Total Simulation Time (min)': total_simulation_time,
        'Average Waiting Time (min)': avg_waiting_time,
        'Average Service Time (min)': avg_service_time,
        'Average Time Between Arrivals (min)': avg_inter_arrival_time,
        'Average Time in System (min)': avg_time_in_system,
        'Server Utilization (%)': server_utilization * 100,
        'Average Idle Time (min)': avg_idle_time,
        'Max Queue Length': max_queue_length,
        'Probability of Customer Waiting in Queue': pr_wait,
        'Probability that System is idle': pr_idle
    }

    print("\n Performance Metrics ")
    for k, v in metrics.items():
        print(f"{k}: {v:.2f}" if isinstance(v, float) else f"{k}: {v}")

    return metrics


def compute_max_queue_length(data):
    """
    Compute the maximum number of customers in the queue at any time.

    Parameters:
        data (DataFrame): Simulated queue data.

    Returns:
        max_queue (int): Maximum queue length.
    """
    events = []

    # Create a list of (time, +1 arrival) and (time, -1 service start)
    for i in range(len(data)):
        events.append((data.loc[i, 'arrival_time'], 'arrival'))
        events.append((data.loc[i, 'start_time'], 'service'))

   
    events.sort()

    current_queue = 0
    max_queue = 0

    for time, event_type in events:
        if event_type == 'arrival':
            current_queue += 1
        else:  
            current_queue -= 1
        max_queue = max(max_queue, current_queue)

    return max_queue