import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define global labels
row_labels = ['Predicted Maple', 'Predicted Tabby', 'Background']
col_labels = ['Background', 'True Tabby', 'True Maple']

# Function to create confusion matrix
def create_confusion_matrix(true_tabby, false_tabby, true_maple, false_maple, background_tabby, background_maple):
    total = sum([true_tabby, false_tabby, true_maple, false_maple, background_tabby, background_maple])
    data = [
        [0, false_tabby/total, true_maple/total],   # Predicted Maple
        [0, true_tabby/total, false_maple/total],             # Predicted Tabby
        [0, background_tabby/total, background_maple/total]              # Background
    ]
    return data

# Define confusion matrix values
true_tabby = 11    # True Positives for Tabby
false_tabby = 1    # False Negatives for Tabby
true_maple = 11    # True Positives for Maple
false_maple = 1     # False Negatives for Maple
background_tabby = 1    # Background or other category
background_maple = 1

# Create the data matrix
data = create_confusion_matrix(true_tabby, false_tabby, true_maple, false_maple, background_tabby, background_maple)

# Create a dataframe using the labels and data
df = pd.DataFrame(data, index=row_labels, columns=col_labels)

# Plot the heatmap
plt.figure(figsize=(6, 6))
sns.heatmap(df, annot=True, cmap='Blues', linewidths=.5)
plt.title('Confusion Matrix for Large Validation Set')
plt.show()
