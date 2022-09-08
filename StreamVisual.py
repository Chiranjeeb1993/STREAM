import streamlit as st
import pandas as pd
import plotly.express as px

st.title("House Rent Dashboard")
st.markdown('The dashboard will visualize the House Rent in India')

df = pd.read_csv("D:\\DATASHEET\\House_Rent_Dataset.csv")
st.write(df.head())
option = st.selectbox('Chart',
                      ('Pie', 'Scatter', 'Bar Plot'))

st.write("Chart Define by", option)
if option == "Pie":
    fig = px.pie(data_frame=df, title="House Rent Define by City", values="Rent", names="City")
    st.plotly_chart(fig)

elif option == "Scatter":
    fig = px.scatter(data_frame=df, title="House Rent Define by Size", x="Size", y="Rent", color="Size")
    st.plotly_chart(fig)

else:
    fig = px.bar(data_frame=df, title="House Rent Define by City using Area Type", x="Area Type", y="Rent", hover_name="City", facet_col="Furnishing Status", color="City",
                 color_continuous_scale=px.colors.sequential.Plasma,template="simple_white")
    fig.update_layout(legend=dict(bgcolor='#C19F14'))
    st.plotly_chart(fig)
