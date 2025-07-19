import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for headless environments

import matplotlib.pyplot as plt
import os

# Create output directory if it doesn't exist
output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

def plot_arrival_vs_service(data):
    plt.figure(figsize=(10, 5))
    plt.scatter(data['arrival_time'], data['service_time'], alpha=0.6)
    plt.xlabel('Arrival Time (min)')
    plt.ylabel('Service Time (min)')
    plt.title('Arrival Time vs Service Time')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/arrival_vs_service.png")
    plt.close()

def plot_waiting_time_distribution(data):
    plt.figure(figsize=(10, 5))
    plt.hist(data['waiting_time'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Waiting Time (min)')
    plt.ylabel('Number of Customers')
    plt.title('Distribution of Waiting Time')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/waiting_time_distribution.png")
    plt.close()

def plot_idle_time(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['arrival_time'], data['idle_time'], label='Idle Time', color='orange')
    plt.xlabel('Arrival Time (min)')
    plt.ylabel('Idle Time (min)')
    plt.title('Server Idle Time Over Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/idle_time_over_time.png")
    plt.close()

def plot_time_in_system(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['time_in_system'], label='Time in System', color='green')
    plt.xlabel('Customer Index')
    plt.ylabel('Time in System (min)')
    plt.title('Time in System for Each Customer')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/time_in_system_per_customer.png")
    plt.close()
