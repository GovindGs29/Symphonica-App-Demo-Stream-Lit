import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
from streamlit_option_menu import option_menu

# Sample data for graphs
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
})

# Function to set background image
def set_bg_hack(main_bg):
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url({main_bg});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Set page configuration
st.set_page_config(page_title="Networking App", page_icon="📊", layout="wide")

# Sidebar menu for navigation
with st.sidebar:
    selected = option_menu(
        "Main Menu", 
        ["Home", "Networking Options", "No-Code SaaS", "Basics of Networking", "Graph Data 1", "Graph Data 2"],
        icons=["house", "diagram-3", "cloud", "info-circle", "bar-chart-line", "bar-chart-line-fill"],
        menu_icon="cast", 
        default_index=0,
    )

# Home Tab
if selected == "Home":
    set_bg_hack("https://example.com/home_bg.jpg")
    st.title("Welcome to the Networking App")
    st.write("""
    This is a sample Streamlit app with multiple tabs. Use the sidebar to navigate between different sections.
    """)

# Networking Options Tab
elif selected == "Networking Options":
    set_bg_hack("https://example.com/networking_options_bg.jpg")
    st.title("Networking Options")
    st.write("""
    This section contains information about various networking options.
    """)

    st.header("1. VPN (Virtual Private Network)")
    st.write("""
    A VPN extends a private network across a public network, allowing users to send and receive data as if their devices were directly connected to the private network.
    """)

    st.header("2. LAN (Local Area Network)")
    st.write("""
    A LAN is a computer network that interconnects computers within a limited area such as a residence, school, laboratory, or office building.
    """)

    st.header("3. WAN (Wide Area Network)")
    st.write("""
    A WAN is a telecommunications network that extends over a large geographic area for the primary purpose of computer networking.
    """)

# No-Code SaaS Tab
elif selected == "No-Code SaaS":
    set_bg_hack("https://example.com/nocode_saas_bg.jpg")
    st.title("No-Code SaaS Solutions")
    st.write("""
    This section provides explanations of various no-code SaaS (Software as a Service) solutions.
    """)

    st.header("1. Airtable")
    st.write("""
    Airtable is a cloud collaboration service that combines the features of a database with the simplicity of a spreadsheet. It enables users to create custom applications without any coding.
    """)

    st.header("2. Zapier")
    st.write("""
    Zapier is an online automation tool that connects your favorite apps, such as Gmail, Slack, Mailchimp, and over 1,500 more. You can automate repetitive tasks without coding or relying on developers to build the integration.
    """)

    st.header("3. Bubble")
    st.write("""
    Bubble is a no-code development platform that enables users to design, develop, and host web applications without having to code.
    """)

# Basics of Networking Tab
elif selected == "Basics of Networking":
    set_bg_hack("https://example.com/basics_of_networking_bg.jpg")
    st.title("Basics of Networking")
    st.write("""
    This section covers the basics of networking concepts.
    """)

    st.header("1. IP Address")
    st.write("""
    An IP address is a unique address that identifies a device on the internet or a local network. It stands for Internet Protocol address.
    """)

    st.header("2. MAC Address")
    st.write("""
    A MAC address (Media Access Control address) is a unique identifier assigned to a network interface controller for use as a network address in communications within a network segment.
    """)

    st.header("3. Router and Switch")
    st.write("""
    A router is a networking device that forwards data packets between computer networks. A switch is a device in a computer network that connects other devices together.
    """)

# Graph Data 1 Tab
elif selected == "Graph Data 1":
    set_bg_hack("https://example.com/graph_data1_bg.jpg")
    st.title("Networking Data Visualization - 1")
    st.write("""
    This section contains graphs related to networking data.
    """)

    # Matplotlib Bar Chart
    st.write("### Matplotlib Bar Chart")
    fig, ax = plt.subplots()
    ax.bar(data['Category'], data['Values'], color='skyblue')
    ax.set_xlabel('Category')
    ax.set_ylabel('Values')
    ax.set_title('Bar Chart')
    st.pyplot(fig)

    # Altair Line Chart
    st.write("### Altair Line Chart")
    alt_chart = alt.Chart(data).mark_line(point=True).encode(
        x='Category',
        y='Values'
    )
    st.altair_chart(alt_chart, use_container_width=True)

# Graph Data 2 Tab
elif selected == "Graph Data 2":
    set_bg_hack("https://example.com/graph_data2_bg.jpg")
    st.title("Networking Data Visualization - 2")
    st.write("""
    This section contains additional graphs related to networking data.
    """)

    # Plotly Scatter Plot
    st.write("### Plotly Scatter Plot")
    fig = px.scatter(data, x='Category', y='Values', title='Scatter Plot')
    st.plotly_chart(fig)

    # Plotly Bar Chart
    st.write("### Plotly Bar Chart")
    fig = px.bar(data, x='Category', y='Values', title='Bar Chart')
    st.plotly_chart(fig)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Streamlit Enthusiast")
