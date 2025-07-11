# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('cleaned.csv')  

# Quick check
print(df.info())
print(df.head())

# Set Seaborn style
sns.set(style="whitegrid")


# 1. Accidents by Road Surface Type

plt.figure(figsize=(10, 6))
sns.countplot(data=df,
              y='Road_surface_type',
              order=df['Road_surface_type'].value_counts().index,
              palette="viridis")
plt.title('Accidents by Road Surface Type')
plt.xlabel('Number of Accidents')
plt.ylabel('Road Surface Type')
plt.tight_layout()
plt.show()


# 2. Accidents by Weather Conditions

plt.figure(figsize=(10, 6))
sns.countplot(data=df,
              y='Weather_conditions',
              order=df['Weather_conditions'].value_counts().index,
              palette="magma")
plt.title('Accidents by Weather Conditions')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Conditions')
plt.tight_layout()
plt.show()


# 3. Accidents by Light Conditions (Time of Day)

plt.figure(figsize=(10, 6))
sns.countplot(data=df,
              y='Light_conditions',
              order=df['Light_conditions'].value_counts().index,
              palette="cubehelix")
plt.title('Accidents by Light Conditions (Time of Day)')
plt.xlabel('Number of Accidents')
plt.ylabel('Light Conditions')
plt.tight_layout()
plt.show()


# 4. Top Causes of Accidents

plt.figure(figsize=(10, 6))
sns.countplot(data=df,
              y='Cause_of_accident',
              order=df['Cause_of_accident'].value_counts().head(10).index,
              palette="coolwarm")
plt.title('Top 10 Causes of Accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Cause of Accident')
plt.tight_layout()
plt.show()


# 5. Severity Distribution by Light Conditions

plt.figure(figsize=(10, 6))
sns.boxplot(data=df,
            x='Accident_severity',
            y='Light_conditions',
            palette="Set2")
plt.title('Accident Severity by Light Conditions')
plt.xlabel('Accident Severity')
plt.ylabel('Light Conditions')
plt.tight_layout()
plt.show()


# 6. Correlation Heatmap (if numeric)

corr = df.select_dtypes(include=['int64', 'float64']).corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='Blues', fmt=".2f")
plt.title('Correlation Heatmap (Numeric Features)')
plt.tight_layout()
plt.show()


# Done!


print("✅ Analysis Complete!")
