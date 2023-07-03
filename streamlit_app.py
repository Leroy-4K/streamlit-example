from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import streamlit as st
import pandas as pd
import plotly.express as pt

# Create menu items
menu_items = {
    'Home': '/',
    'About': '/about',
    'Contact': '/contact'
}

# Define logo and company name
logo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSk3aZGBOM7uclp1-l0F6JzkiA_S1xg4nNZf-5YcC6YgQ&s"

company_name = 'Dojo Analytics'

# Set layout for top bar
st.set_page_config(page_title=company_name, page_icon=logo_url)

# Display logo and company name
col1, col2 = st.columns([1, 9])
with col1:
    st.image(logo_url, width=50)  # Adjust the width as desired
with col2:
    st.title(company_name)


st.title('Dojo Analytics')
# Upload CSV file

uploaded_file = st.file_uploader("Upload CSV file", type="csv")

# Check if a file was uploaded
if uploaded_file is not None:
    # Read CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    # Display the DataFrame in Streamlit
    df['week'] = df['week'].replace({'1': 'Sunday'}).astype('string')
    df['week'] = df['week'].replace({'1': 'Sunday'}).astype('string')
    df['week'] = df['week'].replace({'2': 'Monday'}).astype('string')
    df['week'] = df['week'].replace({'3': 'Tuesday'}).astype('string')
    df['week'] = df['week'].replace({'4': 'Wednesday'}).astype('string')
    df['week'] = df['week'].replace({'5': 'Thursday'}).astype('string')
    df['week'] = df['week'].replace({'6': 'Friday '}).astype('string')
    df['week'] = df['week'].replace({'7': 'Saturday'}).astype('string')
    option = st.selectbox('Which location do you want data for?',('All locations', 'SW1W', 'W1S', 'SW7', 'NW8', 'W11'))
    if option == "All locations":
      fig = pt.bar(df, x=df['week'], y=df['amount'], title = "Weekday vs Profit")
      j = pt.bar(df, x=df['hr'], y=df['amount'], title = "Hour vs Profit: Across all locations")
      st.plotly_chart(fig)
      st.plotly_chart(j)
      k = pt.bar(df, x=df['postcode_area'], y=df['amount'], title = "Postcode Area vs Profit")
      st.plotly_chart(k)


    elif option == 'SW1W':
      g=df[(df['postcode_area'] == 'SW1W')].copy()
      fig = pt.bar(g, x=g['week'], y=g['amount'], title = "Weekday vs Profit: SW1W")
      j = pt.bar(df, x=g['hr'], y=g['amount'], title = "Hour vs Profit: SW1W")
      st.plotly_chart(fig)
      st.plotly_chart(j)
    elif option == "W1S":
      u=df[(df['postcode_area'] == 'W1S')].copy()
      fig = pt.bar(u, x=u['week'], y=u['amount'], title = "Weekday vs Profit: W1S")
      j = pt.bar(df, x=u['hr'], y=u['amount'], title = "Hour vs Profit: W1S")
      st.plotly_chart(fig)
      st.plotly_chart(j)

    elif option == "SW7":
      u=df[(df['postcode_area'] == 'SW7')].copy()
      fig = pt.bar(u, x=u['week'], y=u['amount'], title = "Weekday vs Profit: SW7")
      j = pt.bar(df, x=u['hr'], y=u['amount'], title = "Hour vs Profit: SW7")
      st.plotly_chart(fig)
      st.plotly_chart(j)

    elif option == "NW8":
      u=df[(df['postcode_area'] == 'NW8')].copy()
      fig = pt.bar(u, x=u['week'], y=u['amount'], title = "Weekday vs Profit: NW8")
      j = pt.bar(df, x=u['hr'], y=u['amount'], title = "Hour vs Profit: NW8")
      st.plotly_chart(fig)
      st.plotly_chart(j)

    elif option == "W11":
      u=df[(df['postcode_area'] == 'W11')].copy()
      fig = pt.bar(u, x=u['week'], y=u['amount'], title = "Weekday vs Profit: W11")
      j = pt.bar(df, x=u['hr'], y=u['amount'], title = "Hour vs Profit: W11")
      st.plotly_chart(fig)
      st.plotly_chart(j)