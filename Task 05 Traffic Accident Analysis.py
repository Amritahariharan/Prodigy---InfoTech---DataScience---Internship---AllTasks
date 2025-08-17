import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'state': ['CA', 'TX', 'CA', 'NY', 'TX', 'NY', 'CA', 'TX', 'FL', 'FL', 'CA', 'NY', 'TX', 'FL', 'CA'],
    'weather': ['Clear', 'Rain', 'Rain', 'Clear', 'Snow', 'Rain', 'Fog', 'Snow', 'Clear', 'Rain', 'Clear', 'Snow', 'Fog', 'Rain', 'Clear'],
    'time_of_day': ['Morning', 'Night', 'Evening', 'Morning', 'Evening', 'Night', 'Morning', 'Evening', 'Morning', 'Night', 'Evening', 'Morning', 'Night', 'Morning', 'Evening']
}
df = pd.DataFrame(data)

# 1. Accidents by State
plt.figure(figsize=(7, 4))
sns.countplot(x='state', data=df, palette='coolwarm')
plt.title("Accidents by State")
plt.show()

# 2. Accidents by Weather Condition
plt.figure(figsize=(7, 4))
sns.countplot(x='weather', data=df, palette='muted')
plt.title("Accidents by Weather Condition")
plt.xticks(rotation=45)
plt.show()

# 3. Accidents by Time of Day
plt.figure(figsize=(7, 4))
sns.countplot(x='time_of_day', data=df, palette='Set2')
plt.title("Accidents by Time of Day")
plt.show()

# 4. State vs Weather Heatmap
state_weather = pd.crosstab(df['state'], df['weather'])
plt.figure(figsize=(7, 5))
sns.heatmap(state_weather, annot=True, cmap='Blues', fmt='d')
plt.title("State vs Weather Accident Counts")
plt.show()
