import matplotlib
import seaborn as sns
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

def plot_service_time_distribution(data):
    plt.figure(figsize=(10, 5))
    sns.histplot(data['service_time'], bins=range(1, 7), kde=True, color='orange', edgecolor='black')
    plt.title("Histogram of Service Times")
    plt.xlabel("Service Time (minutes)")
    plt.ylabel("Number of Customers")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/service_time_distribution.png")
    plt.close()


def plot_customers_in_system_over_time(data):
    # Collecting all unique event times
    events = sorted(set(data['arrival_time'].tolist() + data['end_time'].tolist()))

    customers_in_system = []

    for t in events:
        count = ((data['arrival_time'] <= t) & (data['end_time'] > t)).sum()
        customers_in_system.append(count)

    plt.figure(figsize=(10, 5))
    plt.plot(events, customers_in_system, color='purple')
    plt.title("Number of Customers in System Over Time")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Number of Customers")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/customers_in_system_over_time.png")
    plt.close()

def plot_server_status_over_time(data):
    # Getting all unique event times (arrival or end times)
    event_times = sorted(set(data['arrival_time'].tolist() + data['end_time'].tolist()))
    server_status = []

    # Determining server status at each point
    for t in event_times:
        is_busy = ((data['start_time'] <= t) & (data['end_time'] > t)).any()
        server_status.append(1 if is_busy else 0)

    plt.figure(figsize=(10, 4))
    plt.plot(event_times, server_status, drawstyle='steps-post', color='red')
    plt.title("Server Status Over Time (1 = Busy, 0 = Idle)")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Server Status")
    plt.yticks([0, 1], ["Idle", "Busy"])
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/server_status_over_time.png")
    plt.close()

def plot_waiting_time_boxplot(data):
    plt.figure(figsize=(6, 5))
    sns.boxplot(y=data['waiting_time'], color='lightblue')
    plt.title("Boxplot of Customer Waiting Times")
    plt.ylabel("Waiting Time (minutes)")
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/waiting_time_boxplot.png")
    plt.close()

def plot_waiting_time_per_customer(data):
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, len(data) + 1), data['waiting_time'], color='teal')
    plt.title("Waiting Time per Customer")
    plt.xlabel("Customer Index")
    plt.ylabel("Waiting Time (minutes)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/waiting_time_per_customer.png")
    plt.close()