from generate_data import generate_customer_data
from simulate import simulate_queue
from metrics import compute_metrics
from visualize import (
    plot_arrival_vs_service,
    plot_waiting_time_distribution,
    plot_idle_time,
    plot_time_in_system
)


data = generate_customer_data()
simulated_data = simulate_queue(data)
simulated_data.to_csv('../data/simulated_data.csv')

compute_metrics(simulated_data)

# Generate visualizations
plot_arrival_vs_service(simulated_data)
plot_waiting_time_distribution(simulated_data)
plot_idle_time(simulated_data)
plot_time_in_system(simulated_data)


