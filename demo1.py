import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample dataset
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 30, 40, 50]

# Create a bar chart using Seaborn
plt.figure(figsize=(8, 6))
sns.barplot(x=categories, y=values)

# Create a Streamlit app
st.title("Bar Chart Example")
st.pyplot(plt.gcf())
