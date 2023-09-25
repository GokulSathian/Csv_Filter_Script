import pandas as pd
import sys

def check_null(data):
    #Checking for null values in each column
    data.eq(0).any()

    #Removing Null values
    new_data=data[data['sq__ft']!=0]
    return new_data

def filter_csv(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)

    new_data=check_null(data.copy())

    # Calculate the average price per square foot
    new_data['price_per_sq_ft'] = new_data['price'] / new_data['sq__ft']
    average_price_per_sq_ft = new_data['price_per_sq_ft'].mean()

    # Filter properties with prices less than the average price per square foot
    filtered_properties = new_data[new_data['price_per_sq_ft'] < average_price_per_sq_ft]

    # Write the filtered data to a new CSV file
    filtered_properties.to_csv('filtered-properties.csv', index=False)

    print(f'Task Completed. File created - "filtered-properties.csv".')


if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Specify file_path to be filtered")
    else:
        file_path = sys.argv[1]
        filter_csv(file_path)

