# Govind App for symbonica example
# Version : 1.04


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
from streamlit_option_menu import option_menu

# Sample data for Service Specifications

data_for_graph = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
})

data = pd.DataFrame({
    'Code': ['RESIDENTIAL_TV', 'RESIDENTIAL_ACCESS_GPON', 'RESIDENTIAL_ACCESS_ROUTER', 'RESIDENTIAL_ACCESS', 'RESIDENTIAL_HSD', 'RESIDENTIAL_VOICE'],
    'Version': [1.0, 1.1, 1.1, 1.0, 1.0, 1.0],
    'Name': ['RESI', 'RESI', 'RESI', 'RESI', 'RESI', 'RESI'],
    'Type': ['CFS', 'CFS', 'CFS', 'CFS', 'CFS', 'CFS'],
    'Description': ['RESI TV', 'RESI GPON', 'RESI ROUTER', 'RESI ACCESS', 'RESI HSD', 'RESI VOICE'],
    'Start Date': ['10/12/2020', '10/12/2020', '10/12/2020', '10/12/2020', '10/12/2020', '10/12/2020'],
    'End Date': ['10/12/2025', '10/12/2025', '10/12/2025', '10/12/2025', '10/12/2025', '10/12/2025'],
    'Life Cycle Status': ['IN_TEST', 'IN_TEST', 'IN_TEST', 'IN_TEST', 'IN_TEST', 'IN_TEST'],
    'Created Date': ['10/02/2020', '10/02/2020', '10/02/2020', '10/02/2020', '10/02/2020', '10/02/2020'],
    'Last Modified Date': ['10/12/2020', '10/12/2020', '10/12/2020', '10/12/2020', '10/12/2020', '10/12/2020']
})

# Set page configuration
st.set_page_config(page_title="Symphonica App", page_icon="📊", layout="wide")

image_url = "https://as1.ftcdn.net/v2/jpg/05/14/95/12/1000_F_514951224_2dxMLbIw5qNRdPGD003chpbVcxWtcp7K.jpg"
# Custom CSS for background images
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Sidebar with nested menu
with st.sidebar:
    st.image("https://www.intraway.com/wp-content/uploads/2022/09/Sym-Demo-Series-logo-300x82.png", caption="SYMPHONICA", use_column_width=True)
    st.text_input("Search")

    selected_main = option_menu(
        "Main Menu",
        ["Home", "Party Domain", "Order Management", "Product Domain", "Service Domain", "Workflow Domain", "Resource Domain", "Global"],
        icons=["house", "person", "box", "table", "gear", "file-earmark", "pencil", "globe"],
        menu_icon="cast",
        default_index=0,
        key="main_menu"
    )

    if selected_main == "Service Domain":
        selected_service = option_menu(
            "",
            ["Catalog", "Service Specification", "Test Specifications", "Extra Values", "Order Types"],
            icons=["book", "file-earmark-text", "file-earmark-check", "file-earmark-plus", "file-earmark-code"],
            menu_icon="gear",
            default_index=0,
            orientation="vertical",
            key="service_menu"
        )

# Home Tab
if selected_main == "Home":
    set_background("https://as1.ftcdn.net/v2/jpg/05/14/95/12/1000_F_514951224_2dxMLbIw5qNRdPGD003chpbVcxWtcp7K.jpg")  # Replace with your background image URL
    st.title("Welcome to Symphonica")
    st.write("This is the home page. Use the sidebar to navigate to different sections.")

# Party Domain Tab
elif selected_main == "Party Domain":
    set_background("https://as2.ftcdn.net/v2/jpg/08/24/78/07/1000_F_824780703_2pvuE26gFEqERrVUMvJRSgoUL5NDyNUA.jpg")  # Replace with your background image URL
    st.title("Party Domain")
    st.write("Information about Party Domain.")

# Order Management Tab
elif selected_main == "Order Management":
    set_background("https://as2.ftcdn.net/v2/jpg/08/24/78/07/1000_F_824780703_2pvuE26gFEqERrVUMvJRSgoUL5NDyNUA.jpg")  # Replace with your background image URL
    st.title("Order Management")
    st.write("Information about Order Management.")

# Product Domain Tab
elif selected_main == "Product Domain":
    set_background("https://as2.ftcdn.net/v2/jpg/08/24/78/07/1000_F_824780703_2pvuE26gFEqERrVUMvJRSgoUL5NDyNUA.jpg")  # Replace with your background image URL
    st.title("Product Domain")
    st.write("Information about Product Domain.")

# Service Domain Tab
elif selected_main == "Service Domain":
    set_background("https://as1.ftcdn.net/v2/jpg/08/02/99/42/1000_F_802994297_QzkwDZUlwwO63BxM0v7tOOFrkGLNr5zl.jpg")  # Replace with your background image URL
    st.title("Service Domain")
    if selected_service == "Catalog":
        st.write("Catalog information.")
    elif selected_service == "Service Specification":
        st.write("Service Specification details.")
        st.dataframe(data)
    elif selected_service == "Test Specifications":
        st.write("Test Specifications details.")
    elif selected_service == "Extra Values":
        st.write("Extra Values details.")
    elif selected_service == "Order Types":
        st.write("Order Types details.")

# Workflow Domain Tab
elif selected_main == "Workflow Domain":
    set_background("https://as1.ftcdn.net/v2/jpg/08/00/15/46/1000_F_800154650_OrwpKHznvnf6nU2BOsFi2dEVFy4LPdgL.jpg")  # Replace with your background image URL
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
    
# Resource Domain Tab
elif selected_main == "Resource Domain":
    set_background("https://as1.ftcdn.net/v2/jpg/08/00/15/46/1000_F_800154650_OrwpKHznvnf6nU2BOsFi2dEVFy4LPdgL.jpg")  # Replace with your background image URL
    st.title("Networking Data Visualization - 1")
    st.write("""
    This section contains graphs related to networking data.
    """)
    
    st.write("### Matplotlib Bar Chart")
    fig, ax = plt.subplots()
    ax.bar(data_for_graph['Category'], data_for_graph['Values'], color='skyblue')
    ax.set_xlabel('Category')
    ax.set_ylabel('Values')
    ax.set_title('Bar Chart')
    st.pyplot(fig)

    st.write("### Altair Line Chart")
    alt_chart = alt.Chart(data_for_graph).mark_line(point=True).encode(
        x='Category',
        y='Values'
    )
    st.altair_chart(alt_chart, use_container_width=True)

# Global Tab
elif selected_main == "Global":
    set_background("https://as1.ftcdn.net/v2/jpg/08/00/15/46/1000_F_800154650_OrwpKHznvnf6nU2BOsFi2dEVFy4LPdgL.jpg")  # Replace with your background image URL
    st.write("""
    This section contains additional graphs related to networking data.
    """)

    st.write("### Plotly Scatter Plot")
    fig = px.scatter(data_for_graph, x='Category', y='Values', title='Scatter Plot')
    st.plotly_chart(fig)


    st.write("### Plotly Bar Chart")
    fig = px.bar(data_for_graph, x='Category', y='Values', title='Bar Chart')
    st.plotly_chart(fig)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Symphonica Enthusiast")
