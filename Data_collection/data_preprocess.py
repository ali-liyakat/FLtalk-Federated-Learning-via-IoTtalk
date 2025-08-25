import pandas as pd

# Load dataset
df = pd.read_csv("Dataset/sensor_data.csv", header=None)

# Split by class
class1 = df.iloc[:600]      # label 1
class0 = df.iloc[600:]      # label 0

# Shuffle class-wise
class1 = class1.sample(frac=1, random_state=42).reset_index(drop=True)
class0 = class0.sample(frac=1, random_state=42).reset_index(drop=True)

# Training: first 500 from each class
train_class1 = class1.iloc[:500]
train_class0 = class0.iloc[:500]

# Testing: remaining 100 from each class
test_class1 = class1.iloc[500:]
test_class0 = class0.iloc[500:]

# Final datasets
train_data = pd.concat([train_class1, train_class0]).sample(frac=1, random_state=42).reset_index(drop=True)
test_data = pd.concat([test_class1, test_class0]).sample(frac=1, random_state=42).reset_index(drop=True)

# Client splits
client1_data = pd.concat([train_class1.iloc[:250], train_class0.iloc[:250]]).sample(frac=1, random_state=1).reset_index(drop=True)
client2_data = pd.concat([train_class1.iloc[250:], train_class0.iloc[250:]]).sample(frac=1, random_state=2).reset_index(drop=True)

# Save
client1_data.to_csv("client1_train.csv", index=False, header=False)
client2_data.to_csv("client2_train.csv", index=False, header=False)
test_data.to_csv("test_data.csv", index=False, header=False)
