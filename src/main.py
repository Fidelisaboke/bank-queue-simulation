from generate_data import generate_customer_data
from simulate import simulate_queue

data = generate_customer_data()
simulated_data = simulate_queue(data)
simulated_data.to_csv('data/simulated_data.csv')
