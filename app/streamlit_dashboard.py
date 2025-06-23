# app/streamlit_dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Alloy Explorer", layout="wide")

# Load cleaned data
@st.cache_data
def load_data():
    file_path = '/Users/m.mughees/Desktop/2025-IEEE_SciVis-Contest-Mughees/data/Dataset_VisContest_Rapid_Alloy_development_v3.txt'

    # Try reading with ISO-8859-1 encoding (Latin-1), which handles many special characters
    try:
        df = pd.read_csv(file_path, sep='\t', encoding='ISO-8859-1')
    except Exception as e:
        print("Tab delimiter failed. Trying semicolon with ISO-8859-1...")
        df = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1')

    return df

df = load_data()


# Sidebar – Filters

st.sidebar.header("🔍 Filter Alloys")

# Target Property Filters
ys_range = st.sidebar.slider("Yield Strength (MPa)", 0, int(df["YS(MPa)"].max()), (200, 400))
cond_range = st.sidebar.slider("Thermal Conductivity (W/mK)", 0, int(df["Therm.conductivity(W/(mK))"].max()), (0, 200))
csc_safe = st.sidebar.checkbox("Only show low-crack-risk alloys (CSC < 1)", value=True)

# Use Case Scenario

scenario = st.sidebar.selectbox("Use Case", [
    "Aerospace",
    "Automotive",
    "Power Generation",
    "Additive Manufacturing",
    "E-Mobility",
    "Utility Infrastructure"
])


# Main Area – Display Results

st.title("Alloy Explorer Dashboard")
st.markdown(f"Use case selected: **{scenario}**")

# Apply Filters

filtered_df = df[
    (df["YS(MPa)"] >= ys_range[0]) & (df["YS(MPa)"] <= ys_range[1]) &
    (df["Therm.conductivity(W/(mK))"] >= cond_range[0]) & 
    (df["Therm.conductivity(W/(mK))"] <= cond_range[1])
]

if csc_safe:
    filtered_df = filtered_df[filtered_df["CSC"] < 1]

st.subheader(f"Top {min(10, len(filtered_df))} Candidates")

# Show filtered table
st.dataframe(filtered_df.sort_values("YS(MPa)", ascending=False).head(10))

# Show comparison barplot
st.subheader("YS vs. Thermal Conductivity")
fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(
    data=filtered_df, x="Therm.conductivity(W/(mK))", y="YS(MPa)", hue="CSC", palette="coolwarm", ax=ax
)
ax.set_title("Candidate Alloys: YS vs. Conductivity")
st.pyplot(fig)
