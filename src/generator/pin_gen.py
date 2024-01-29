import pandas as pd


def extract_and_sort_unique_pincode(input_csv, output_txt, max_rows=30000, encoding='utf-8'):
    try:
        df = pd.read_csv(input_csv, usecols=[
                         'Pincode'], nrows=max_rows, encoding=encoding)
        unique_pincode = sorted(df['Pincode'].dropna().astype(int).unique())
        with open(output_txt, 'w') as file:
            for pin in unique_pincode:
                file.write(f"{pin}\n")
        print(
            f"Unique Pincode values extracted, sorted, and saved to {output_txt}")
    except Exception as e:
        print(f"Error: {e}")


input_csv_file = 'pincode.csv'
output_txt_file = 'pin.txt'

extract_and_sort_unique_pincode(input_csv_file, output_txt_file)
