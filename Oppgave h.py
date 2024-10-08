import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Function to read data from a CSV file and load it into lists
def read_csv_to_lists(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        columns = reader.fieldnames
        data = {column: [] for column in columns}
        for row in reader:
            for column in columns:
                data[column].append(row[column])
    return data

# Function to convert date and time strings to datetime objects
def convert_to_datetime(date_str, date_format):
    try:
        return datetime.strptime(date_str, date_format)
    except ValueError:
        # Handle different date formats
        try:
            return datetime.strptime(date_str, "%m/%d/%Y %I:%M:%S %p")
        except ValueError:
            return None

# Load data from the file into lists
file_data = read_csv_to_lists('temperatur_trykk_met_samme_rune_time_datasett.csv.txt')

# Convert date and time strings to datetime objects
datetimes = [convert_to_datetime(date_str, "%d.%m.%Y %H:%M") for date_str in file_data['Tid(norsk normaltid)']]

# Convert temperature strings to floats, handling empty strings
temperatures = [float(temp.replace(',', '.')) if temp else None for temp in file_data['Lufttemperatur']]

# Filter out None values from the temperature lists along with their corresponding datetime values
datetimes = [dt for dt, temp in zip(datetimes, temperatures) if temp is not None]
temperatures = [temp for temp in temperatures if temp is not None]

# Find the indices for the specified time range
start_time = datetime.strptime("11.06.2021 17:31", "%d.%m.%Y %H:%M")
end_time = datetime.strptime("12.06.2021 03:05", "%d.%m.%Y %H:%M")

start_index = next(i for i, dt in enumerate(datetimes) if dt >= start_time)
end_index = next(i for i, dt in enumerate(datetimes) if dt >= end_time)

# Slice the lists to get the data for the specified time range
selected_datetimes = datetimes[start_index:end_index + 1]
selected_temperatures = temperatures[start_index:end_index + 1]

# Plot the temperature fall
plt.figure(figsize=(10, 6))
plt.plot(selected_datetimes, selected_temperatures, label='Temperature', color='blue')
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Fall from Evening of June 11 to Night of June 12, 2021')
plt.legend()
plt.grid(True)
plt.show()
