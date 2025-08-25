import matplotlib.pyplot as plt
import numpy as np

# Define updated metrics and axis positions
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-score', 'ROC-AUC']
x = np.arange(len(metrics))

# Updated metric values from user input
client1 = [0.791, 0.79, 0.79, 0.79, 0.83]
client2 = [0.7811, 0.78, 0.78, 0.78, 0.84]
global_model = [0.7960, 0.80, 0.80, 0.80, 0.84]

# Bar width and colors
width = 0.25
color1 = '#FF9999'
color2 = '#66B2FF'
color3 = '#999999'

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars for each model
bars1 = ax.bar(x - width, client1, width, label='M1', color=color1, edgecolor='black', hatch="/")
bars2 = ax.bar(x, client2, width, label='M2', color=color2, edgecolor='black')
bars3 = ax.bar(x + width, global_model, width, label='M3', color=color3, edgecolor='black', hatch="-")

# Axis configuration with custom font sizes
ax.set_ylabel('Score', fontsize=22)
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=22)
ax.set_yticks(np.linspace(0, 1.0, 11))
ax.set_yticklabels([f'{t:.1f}' for t in np.linspace(0, 1.0, 11)], fontsize=22)
ax.set_ylim(0, 1.05)
ax.legend(fontsize=15)

# Annotate bar values with larger font size
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.3f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

# Final layout
plt.tight_layout()
plt.savefig("Results.png")
plt.show()
