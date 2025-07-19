from generate_data import generate_customer_data
from simulate import simulate_queue
from metrics import compute_metrics
from visualize import (
    plot_arrival_vs_service,
    plot_waiting_time_distribution,
    plot_idle_time,
    plot_time_in_system,
    plot_service_time_distribution,
    plot_customers_in_system_over_time,
    plot_server_status_over_time,
    plot_waiting_time_boxplot,
    plot_waiting_time_per_customer
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
plot_service_time_distribution(simulated_data)
plot_customers_in_system_over_time(simulated_data)
plot_server_status_over_time(simulated_data)
plot_waiting_time_boxplot(simulated_data)
plot_waiting_time_per_customer(simulated_data)