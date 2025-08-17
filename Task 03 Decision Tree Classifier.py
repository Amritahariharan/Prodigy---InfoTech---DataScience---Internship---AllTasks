import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

data = {
    'age': [22, 25, 47, 52, 46],
    'salary': [25000, 32000, 50000, 52000, 49000],
    'buys': [0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[['age', 'salary']]
y = df['buys']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Plot tree
plt.figure(figsize=(8, 5))
plot_tree(model, feature_names=['age', 'salary'], class_names=['No', 'Yes'], filled=True)
plt.title("Decision Tree Classifier")
plt.show()
