# Import necessary libraries
import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Gaming Data Analysis")

# Get the current credentials
session = get_active_session()

# Query the gaming table from Snowflake
query = "SELECT * FROM datasheet_week.ds_schm.gaming_table"
df = session.sql(query).to_pandas()

# Display the raw data
st.subheader("Raw Data")
st.dataframe(df, use_container_width=True)

# Summary Statistics
st.subheader("Summary Statistics")
st.write(df.describe())

# Ratings Distribution
st.subheader("Ratings Distribution")
rating_counts = df['RATING'].value_counts()
st.bar_chart(rating_counts)

# Votes Distribution
st.subheader("Votes Distribution")
if 'VOTES' in df.columns:
    # Use Streamlit's built-in line_chart for a simple distribution representation
    st.line_chart(df['VOTES'].value_counts())
else:
    st.write("The 'VOTES' column does not exist in the DataFrame.")


# Genre Analysis
st.subheader("Genre Analysis")
genre_columns = ['ACTION', 'ADVENTURE', 'COMEDY', 'CRIME', 'FAMILY', 'FANTASY', 'MYSTERY', 'SCI_FI', 'THRILLER']
genre_counts = df[genre_columns].sum()
st.bar_chart(genre_counts)

# Certificate Analysis
st.subheader("Certificate Analysis")
certificate_counts = df['CERTIFICATE'].value_counts()
st.bar_chart(certificate_counts)

# Correlation Matrix
st.subheader("Correlation Matrix")
correlation_matrix = df.corr()
st.write(correlation_matrix)

# # Scatter Plot of Rating vs. Votes
# st.subheader("Scatter Plot: Rating vs. Votes")
# st.scatter_chart(df, x='RATING', y='VOTES')

# # Pair Plot
# st.subheader("Pair Plot")
# st.pair_plot(df)

# # Box Plot of Ratings by Certificate
# st.subheader("Box Plot: Ratings by Certificate")
# st.box_plot(df, x='CERTIFICATE', y='RATING')

# # Heatmap of Genre Correlation
# st.subheader("Heatmap: Genre Correlation")
# genre_correlation = df[genre_columns].corr()
# st.heatmap(genre_correlation)

# Additional analyses and visualizations can be added based on your specific requirements.

# Closing Snowflake connection
# session.close()
