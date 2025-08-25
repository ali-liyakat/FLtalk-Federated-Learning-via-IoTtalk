import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Load training data
train_df = pd.read_csv("client2_train.csv", header=None)
X_train = train_df.iloc[:, :-1].values
y_train = train_df.iloc[:, -1].values

# Load testing data
test_df = pd.read_csv("test_data.csv", header=None)
X_test = test_df.iloc[:, :-1].values
y_test = test_df.iloc[:, -1].values

# Standardize
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate
score = model.score(X_test, y_test)
print(f"Test Accuracy: {score:.4f}")

y_pred = model.predict(X_test)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
conf_mat = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Client 2')
plt.tight_layout()
plt.show()

# ROC Curve
if len(np.unique(y_test)) == 2:
    y_proba = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve - Client 2")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Save model params
params = {
    "coef": model.coef_[0].tolist(),
    "intercept": model.intercept_.tolist()
}
with open("params_client2.json", "w") as f:
    json.dump(params, f)
