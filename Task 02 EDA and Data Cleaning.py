import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [25, 30, None, 45, 28],
    'income': [50000, 60000, 55000, None, 52000]
}
df = pd.DataFrame(data)

# Cleaning
df['age'].fillna(df['age'].mean(), inplace=True)
df.dropna(subset=['income'], inplace=True)

# EDA: Summary and visuals
print("Summary Statistics:\n", df.describe())

sns.boxplot(x='age', data=df)
plt.title("Boxplot of Age")
plt.show()

sns.scatterplot(x='age', y='income', data=df)
plt.title("Age vs Income")
plt.show()
