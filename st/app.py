import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Safe CSV load
try:
    data = pd.read_csv("diabetes.csv")
except FileNotFoundError:
    st.error(" 'diabetes.csv' not found! Please make sure it’s in the same folder as app.py.")
    st.stop()


# Title
st.title("Diabetes Dataset Visualization Dashboard")

# Show raw data
st.subheader("Raw Dataset")
st.dataframe(data.head(20))

# Basic summary
st.subheader("Data Summary")
st.write(data.describe())

# Outcome distribution
st.subheader("Diabetes Outcome Distribution")
outcome_counts = data['Outcome'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(outcome_counts, labels=['No Diabetes', 'Diabetes'], autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# Correlation Heatmap
st.subheader("Feature Correlation Heatmap")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax2)
st.pyplot(fig2)

# BMI vs Age by Outcome
st.subheader("BMI vs Age (Colored by Outcome)")
fig3, ax3 = plt.subplots()
sns.scatterplot(data=data, x='Age', y='BMI', hue='Outcome', palette='Set1', ax=ax3)
st.pyplot(fig3)

# Glucose Distribution by Outcome
st.subheader("Glucose Level Distribution")
fig4, ax4 = plt.subplots()
sns.histplot(data=data, x='Glucose', hue='Outcome', kde=True, element="step", bins=30, ax=ax4)
st.pyplot(fig4)

# Boxplot for numeric feature comparison
st.subheader("Boxplot Comparison of Key Features")
features = ['Glucose', 'BloodPressure', 'BMI', 'Age']
for feature in features:
    st.write(f"### {feature} by Outcome")
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x='Outcome', y=feature, ax=ax)
    ax.set_xticklabels(['No Diabetes', 'Diabetes'])
    st.pyplot(fig)

# Footer
st.markdown("---")

