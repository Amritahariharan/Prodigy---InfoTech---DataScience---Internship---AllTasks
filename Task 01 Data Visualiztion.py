import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data={'age':[22,38,26,35,28,42,19,40,33,27,18,50,23,21,45,29,31,37,41,34],
      'gender':['male','female','female','female','male','male','female','male','male','female','male','female','male',
                                    'female','male','female','male','female','male','female']
}
df=pd.DataFrame(data)

#1.Bar Chart for Gender
plt.figure(figsize=(6, 4))
sns.countplot(x='gender', data=df, palette='Set2')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

#2.Histogram for Age
plt.figure(figsize=(8, 5))
sns.histplot(df['age'], bins=10, kde=True, color='skyblue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#3.Pie Chart for Gender Percentage
gender_counts = df['gender'].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'])
plt.title("Gender Percentage")
plt.show()

#4.Boxplot for Age by Gender
plt.figure(figsize=(6, 4))
sns.boxplot(x='gender', y='age', data=df, palette='pastel')
plt.title("Age Distribution by Gender")
plt.show()




