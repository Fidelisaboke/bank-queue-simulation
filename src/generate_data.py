import numpy as np
import pandas as pd

def generate_customer_data(n_customers=500, seed=42):
    """
    Generate inter-arrival and service times of customers
    and store them in a CSV File.
    - Inter-arrival time of customers is uniformly distributed 
    between 1 and 8 minutes.
    - Service times are uniformly distributed between 1 and
    6 minutes.
    """
    np.random.seed(seed)
    inter_arrival_times = np.random.uniform(1, 8, n_customers)
    service_times = np.random.uniform(1, 6, n_customers)

    data = pd.DataFrame({
        'inter_arrival_time': inter_arrival_times,
        'service_time': service_times
    })
    data.to_csv('../data/customer_data.csv', index=False)
    return data