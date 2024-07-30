import pandas as pd
import sys

def reduce_csv_rows(input_file, output_file, percentage):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Calculate the number of rows to keep
    num_rows_to_keep = int(len(df) * (percentage / 100))
    
    # Reduce the DataFrame to the desired number of rows
    df_reduced = df.head(num_rows_to_keep)
    
    # Save the reduced DataFrame to a new CSV file
    df_reduced.to_csv(output_file, index=False)
    print(f"Reduced CSV file saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python reduce_csv.py <input_file> <output_file> <percentage>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        percentage = float(sys.argv[3])
        
        if not (0 <= percentage <= 100):
            print("Percentage must be between 0 and 100")
        else:
            reduce_csv_rows(input_file, output_file, percentage)
