import csv
import os


def process_file(input_file, label, output_file='newCombinedData.csv', chunk_size=10):
    """
    Combines data from the input file into rows of chunk_size and appends a label.
    """
    combined_rows = []  
    row_buffer = []  


    # Read the input file
    with open(input_file, 'r') as file:
        data = csv.reader(file)
        for count, row in enumerate(data, start=1):
            row_buffer.extend(row)  
            if count % chunk_size == 0:  
                combined_rows.append(row_buffer + [label])  
                row_buffer = []  

    # Write combined rows to the output file
    write_to_csv(output_file, combined_rows, label)



def write_to_csv(output_file, rows, label):
    """
    Writes combined rows to the output CSV file with dynamic headers.
    """
    headers = [f"{sensor}{i}-{j}" for i in range(1, 11) for sensor in ['acc', 'gyro'] for j in range(1, 4)]
    headers.append('label')

    # Write the rows to the file
    with open(output_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if os.stat(output_file).st_size == 0: 
            writer.writerow(headers)
        writer.writerows(rows)

process_file('Data_collection/circle.csv', label=1)
process_file('Data_collection/cross.csv', label=0)
