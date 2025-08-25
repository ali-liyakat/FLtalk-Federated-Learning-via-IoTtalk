import pandas as pd
import numpy as np
import json
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler


# Step 1: Load data
df = pd.read_csv('client1_data.csv')
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

scaler = StandardScaler()
X = scaler.fit_transform(X)


# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print(f"Test Accuracy: {score:.4f}")

# Step 3: Evaluate the model
y_pred = model.predict(X_test)
conf_mat = confusion_matrix(y_test, y_pred)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 4: Plot confusion matrix
plt.figure(figsize=(6, 5))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Client 1')
plt.tight_layout()
# plt.savefig("Client1_confusion_matrix.png")
plt.show()

# Step 5: Plot ROC Curve (for binary classification only)
if len(np.unique(y)) == 2:
    y_proba = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve - Client 1')
    plt.legend(loc="lower right")
    plt.tight_layout()
    # plt.savefig("Client1_roc_curve.png")
    plt.show()

# Step 6: Save model parameters
# params = {
#     'coef': model.coef_[0].tolist(),
#     'intercept': model.intercept_.tolist()
# }
# with open('params_client1.json', 'w') as f:
#     json.dump(params, f)
# print("Model parameters saved.")
