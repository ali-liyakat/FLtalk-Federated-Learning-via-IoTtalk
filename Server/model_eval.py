import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    auc,
    precision_recall_curve
)

# ------------------------------
# Step 1: Load global model parameters
# ------------------------------
with open('global_model.json', 'r') as f:
    global_params = json.load(f)

coef = np.array(global_params['coef']).reshape(1, -1)
intercept = np.array(global_params['intercept'])

# ------------------------------
# Step 2: Load shared test dataset
# ------------------------------
df_test = pd.read_csv('test_data.csv', header=None)
X_test = df_test.iloc[:, :-1].values
y_test = df_test.iloc[:, -1].values

# Standardize test data
scaler = StandardScaler()
X_test = scaler.fit_transform(X_test)  # Ideally use training scaler; here we fit for simplicity

# ------------------------------
# Step 3: Reconstruct global logistic regression model
# ------------------------------
model = LogisticRegression(max_iter=1000)
model.coef_ = coef
model.intercept_ = intercept
model.classes_ = np.unique(y_test)  # Ensure proper class mapping

# ------------------------------
# Step 4: Predict using global model
# ------------------------------
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]  # For ROC/PR curves

# ------------------------------
# Step 5: Print metrics
# ------------------------------
print(f"✅ Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print("📄 Classification Report:\n", classification_report(y_test, y_pred))

# ------------------------------
# Step 6: Plot Confusion Matrix
# ------------------------------
plt.figure(figsize=(6, 5))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix - Global Model")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.tight_layout()
plt.show()

# ------------------------------
# Step 7: ROC Curve
# ------------------------------
fpr, tpr, _ = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Global Model')
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()

# ------------------------------
# Step 8: Precision-Recall Curve
# ------------------------------
precision, recall, _ = precision_recall_curve(y_test, y_proba)

plt.figure()
plt.plot(recall, precision, label="PR Curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve - Global Model")
plt.tight_layout()
plt.show()
