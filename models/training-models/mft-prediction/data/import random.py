import random
import csv

def generate_random_data(num_records):
    countries = ["internal", "external", "hybrid", ...]
    file_types = ["txt", "pdf", "docx", ...]
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Wednesday", "Friday", "Saturday", "Sunday", ...]
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Wednesday", "Friday", "Saturday", "Sunday", ...]
    size = ["XL", "L", "M", "S", ...]

    data = []
    for _ in range(num_records):
        size = random.choice(size)
        file_size = random.randint(100, 10000)
        time_between_transfers = random.randint(10, 100)
        source_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        destination_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        is_executable = random.choice([0, 1])
        is_compressed = random.choice([0, 1])
        source_country = random.choice(countries)
        destination_country = random.choice(countries)
        file_type = random.choice(file_types)
        time_of_day = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"
        day_of_week = random.choice(days_of_week)
        data.append([size, file_size, time_between_transfers, source_ip, destination_ip, is_executable, is_compressed, source_country, destination_country, file_type, time_of_day, day_of_week])

    return data

# Generate 100 records
data = generate_random_data(100)

# Save data to a CSV file
with open('mftinput2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['size_cat','File Size', 'Time Between Transfers', 'Source IP', 'Destination IP', 'Is Executable', 'Is Compressed', 'Source Country', 'Destination Country', 'File Type', 'Time of Day', 'Day of Week'])
    writer.writerows(data)