import numpy as np
import pandas as pd

df = pd.read_csv("Dataset/sensor_data.csv")

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Split features (X) and target labels (y)
X = df.iloc[:, :-1].values  
y = df.iloc[:, -1].values   

NUM_CLIENTS = 2 

# Split dataset equally into clients
client_datasets = np.array_split(df, NUM_CLIENTS)

# Save each client’s data separately
for i, client_data in enumerate(client_datasets):
    client_data.to_csv(f"client_{i+1}_data.csv", index=False)

print("Dataset split into", NUM_CLIENTS, "clients. Saved as CSV files.")
