def simulate_queue(data):
    arrival_times = data['inter_arrival_time'].cumsum()
    service_times = data['service_time']

    start_times = [arrival_times[0]]
    waiting_times = [0]
    end_times = [start_times[0] + service_times[0]]
    times_in_system = [service_times[0]]
    idle_times = [0]

    for i in range(1, len(data)):
        start_time = max(arrival_times[i], end_times[i-1])
        wait_time = start_time - arrival_times[i]
        end_time = start_time + service_times[i]
        time_in_system = wait_time + service_times[i]
        idle_time = start_time - end_times[i-1] 

        start_times.append(start_time)
        waiting_times.append(wait_time)
        end_times.append(end_time)
        times_in_system.append(time_in_system)
        idle_times.append(idle_time)

    data['arrival_time'] = arrival_times
    data['start_time'] = start_times
    data['end_time'] = end_times
    data['waiting_time'] = waiting_times
    data['time_in_system'] = times_in_system
    data['idle_time'] = idle_times

    return data
