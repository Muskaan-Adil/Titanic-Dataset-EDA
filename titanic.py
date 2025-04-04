import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Titanic_Dataset.csv')  # Adjust the path if needed

# 1. Basic Data Inspection
print("First 5 rows of the dataset:")
print(df.head())

print("\nLast 5 rows of the dataset:")
print(df.tail())

print("\nNo of columns in the dataset:")
print(df.columns)

print("\nDataset Info (Types, Missing Values):")
print(df.info())

print("\nSummary Statistics of Numerical Features:")
print(df.describe())

# 2. Checking for Missing Values
print("\nMissing Values Count:")
print(df.isnull().sum())

# 3. Distribution of Numerical Features
print("\nDistribution of 'Age' and 'Fare':")
sns.histplot(df['Age'], kde=True, color='blue', bins=30)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['Fare'], kde=True, color='green', bins=30)
plt.title('Distribution of Fare')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

# 4. Visualize Categorical Variables
print("\nCount Plot for 'Sex':")
sns.countplot(x='Sex', data=df)
plt.title('Count of Passengers by Sex')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()

print("\nCount Plot for 'Embarked':")
sns.countplot(x='Embarked', data=df)
plt.title('Count of Passengers by Embarked')
plt.xlabel('Embarked')
plt.ylabel('Count')
plt.show()

# 5. Relationship Between Age and Survival
print("\nBoxplot for 'Age' vs 'Survived':")
sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Age Distribution by Survival')
plt.xlabel('Survived')
plt.ylabel('Age')
plt.show()

# 6. Relationship Between Pclass and Survival
print("\nCount Plot for Survival by Pclass:")
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Survival by Class')
plt.xlabel('Pclass')
plt.ylabel('Count')
plt.show()

# 7. Correlation Matrix for Numerical Features
print("\nCorrelation Matrix:")
corr = df[['Age', 'SibSp', 'Parch', 'Fare']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()