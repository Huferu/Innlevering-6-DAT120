import csv
from datetime import datetime

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
            return datetime.strptime(date_str, "%m/%d/%Y %H:%M:%S %p")
        except ValueError:
            return None

if __name__=="__main__":
    # Load data from the first file into lists
    file1_data = read_csv_to_lists('trykk_og_temperaturlogg_rune_time.csv.txt')
    
    # Load data from the second file into lists
    file2_data = read_csv_to_lists('temperatur_trykk_met_samme_rune_time_datasett.csv.txt')
    
    # Convert date and time strings to datetime objects for the first file
    file1_datetimes = [convert_to_datetime(date_str, "%d.%m.%Y %H:%M") for date_str in file1_data['Dato og tid']]
    
    # Convert date and time strings to datetime objects for the second file
    file2_datetimes = [convert_to_datetime(date_str, "%d.%m.%Y %H:%M") for date_str in file2_data['Tid(norsk normaltid)']]
    
    # Print the first few datetime objects to verify the conversion
    print("Datetime objects from the first file:")
    print(file1_datetimes[:10])
    
    print("\nDatetime objects from the second file:")
    print(file2_datetimes[:10])