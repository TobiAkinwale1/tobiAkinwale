import pandas as pd
import numpy as np

# Generate 1000 random numbers
random_numbers = np.random.randint(low=1, high=10000, size=1000)

# Create a DataFrame
df = pd.DataFrame(random_numbers, columns=['Random Numbers'])

# Save to an Excel file
excel_file_path = '/mnt/data/random_numbers.xlsx'
df.to_excel(excel_file_path, index=False)

excel_file_path
