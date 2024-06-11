# Govind App Networking Symphonica Example
# Version : 1.08

import streamlit as st
import pandas as pd
import yaml
import os
import hashlib
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
from streamlit_option_menu import option_menu
from st_aggrid import AgGrid

# List used for switching menu options
service_options = ["Catalog", "Service Specification", "Test Specifications", "Extra Values", "Order Types"]
main_options = ["Home", "Party Domain", "Order Management", "Product Domain", "Service Domain", "Workflow Domain", "Resource Domain", "Global"]

# Sample Dataframes
data_for_graph = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [10, 20, 30, 40, 50]
})

additional_data = pd.DataFrame({
    'Category': ['F', 'G', 'H', 'I', 'J'],
    'Values': [15, 25, 35, 45, 55]
})

orders_data = pd.DataFrame({
    "Id": ["62dc28595", "62dc28165", "62dc28596", "62dc28166", "62dc28597", "62dc28167", "62dc28598", "62dc28168", "62dc28599", "62dc28169", "62dc28600", "62dc28170"],
    "Source": ["SYM-SOM", "SYM-SOM", "SYM-SOM", "SYM-SOM", "SYM-SOM", "SYM-SOM", "SYM-SOM", "SYM-SOM", "SYM-SOM", "SYM-SOM", "SYM-SOM", "SYM-SOM"],
    "External Id": ["SYM-001", "SYM-002", "SYM-003", "SYM-004", "SYM-005", "SYM-006", "SYM-007", "SYM-008", "SYM-009", "SYM-010", "SYM-011", "SYM-012"],
    "Customer Id": ["eze2307", "eze2307", "eze2308", "eze2308", "eze2309", "eze2309", "eze2310", "eze2310", "eze2311", "eze2311", "eze2312", "eze2312"],
    "Order Type": ["CEASE", "PROVIDE", "CEASE", "PROVIDE", "CEASE", "PROVIDE", "CEASE", "PROVIDE", "CEASE", "PROVIDE", "CEASE", "PROVIDE"],
    "Category": ["Completed", "Failed", "Completed", "Failed", "Completed", "Failed", "Completed", "Failed", "Completed", "Failed", "Completed", "Failed"],
    "Order Date": ["7/23/2022 12:56 pm", "7/23/2022 12:55 pm", "7/24/2022 12:56 pm", "7/24/2022 12:55 pm", "7/25/2022 12:56 pm", "7/25/2022 12:55 pm", "7/26/2022 12:56 pm", "7/26/2022 12:55 pm", "7/27/2022 12:56 pm", "7/27/2022 12:55 pm", "7/28/2022 12:56 pm", "7/28/2022 12:55 pm"],
    "State": ["COMPLETED", "FAILED", "COMPLETED", "FAILED", "COMPLETED", "FAILED", "COMPLETED", "FAILED", "COMPLETED", "FAILED", "COMPLETED", "FAILED"],
})

service_data = pd.DataFrame({
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

# Setting page configuration
st.set_page_config(page_title="Streamlit_app v.10", page_icon="📊", layout="wide")

# Function to set background image
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

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Load user data from YAML file
def load_user_data():
    if os.path.exists("users.yaml"):
        with open("users.yaml", "r") as file:
            return yaml.safe_load(file)
    return {}

# Save user data to YAML file
def save_user_data(user_data):
    with open("users.yaml", "w") as file:
        yaml.safe_dump(user_data, file)

# Initialize user data
user_data = load_user_data()

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# Login function
def login(username, password):
    if username in user_data and user_data[username] == hash_password(password):
        st.session_state.logged_in = True
        st.session_state.username = username
        return True
    else:
        return False
# Register function
def register(username, password):
    if username not in user_data:
        user_data[username] = hash_password(password)
        save_user_data(user_data)
        return True
    else:
        return False

# Logout function
def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""

# Login Page Customization can be used here
def login_page():
    set_background("https://as1.ftcdn.net/v2/jpg/05/14/95/12/1000_F_514951224_2dxMLbIw5qNRdPGD003chpbVcxWtcp7K.jpg")
    st.title("Symphonica App Login")

    st.subheader("Login")
    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login(login_username, login_password):
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")

    st.subheader("Register")
    register_username = st.text_input("New Username")
    register_password = st.text_input("New Password", type="password")
    if st.button("Register"):
        if register(register_username, register_password):
            st.success("Registered successfully! You can now log in.")
        else:
            st.error("Username already exists. Please choose a different username.")

# Main App Data can be modified here
def main_app():
    # Sidebar with nested menu and search functionality
    with st.sidebar:
        st.image("https://www.intraway.com/wp-content/uploads/2022/09/Sym-Demo-Series-logo-300x82.png", caption="SYMPHONICA", use_column_width=True)
        search_query = st.text_input("Search")

        # Filter main menu options based on search query
        filtered_main_options = [option for option in main_options if search_query.lower() in option.lower()]

        selected_main = option_menu(
            "Main Menu",
            filtered_main_options,
            icons=["house", "person", "box", "table", "gear", "file-earmark", "pencil", "globe"],
            menu_icon="cast",
            default_index=0,
        )

        if selected_main == "Order Management":
            selected_order_management = option_menu(
                "Order Management",
                ["Service Orders", "Cancel Service Orders", "Workflow Orders", "Resource Orders", "User Tasks"],
                icons=["box-arrow-in-right", "x", "arrows-move", "boxes", "clipboard-check"],
                menu_icon="boxes",
                default_index=0,
            )

        if selected_main == "Service Domain":
            selected_service = option_menu(
                "Service Domain",
                service_options,
                icons=["collection", "file-earmark-text", "file-earmark-text", "file-earmark-text", "file-earmark-text"],
                menu_icon="boxes",
                default_index=0,
            )

    # Home Tab
    if selected_main == "Home":
        set_background("https://as1.ftcdn.net/v2/jpg/05/14/95/12/1000_F_514951224_2dxMLbIw5qNRdPGD003chpbVcxWtcp7K.jpg")
        st.title("Welcome to Symphonica")

        st.write(f"Welcome, {st.session_state.username}!")
        st.button("Logout", on_click=logout)
        st.write("This is the home page. Use the sidebar to navigate to different sections.")

    # Party Domain Tab
    elif selected_main == "Party Domain":
        set_background("https://as2.ftcdn.net/v2/jpg/08/24/78/07/1000_F_824780703_2pvuE26gFEqERrVUMvJRSgoUL5NDyNUA.jpg")
        st.title("Basics of Networking")
        st.write("This section covers the basics of networking concepts.")

        st.header("1. IP Address")
        st.write("An IP address is a unique address that identifies a device on the internet or a local network. It stands for Internet Protocol address.")

        st.header("2. MAC Address")
        st.write("A MAC address (Media Access Control address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment.")

        st.header("3. Routers and Switches")
        st.write("Routers and switches are the building blocks for all business communications, from data to voice and video to wireless access. They send information, connect computers and provide access to the Internet.")

        # Example graph using matplotlib
        st.subheader("Network Traffic Analysis")
        fig, ax = plt.subplots()
        ax.plot(data_for_graph['Category'], data_for_graph['Values'], marker='o')
        ax.set_title("Network Traffic Over Time")
        ax.set_xlabel("Time")
        ax.set_ylabel("Traffic")
        st.pyplot(fig)

    # Order Management Tab
    elif selected_main == "Order Management":
        set_background("https://as2.ftcdn.net/v2/jpg/01/90/61/12/1000_F_190611262_jGbMQB3Tdk2Hk7rQu8PVYPAr8rC8j02D.jpg")
        st.title("Order Management")
        st.write("This section covers order management.")

        if selected_order_management == "Service Orders":
            st.header("Service Orders")

            # Display the orders data
            st.subheader("Order Data")
            AgGrid(orders_data, height=300)

            st.subheader("Order Status Distribution")
            order_status_counts = orders_data['State'].value_counts().reset_index()
            order_status_counts.columns = ['State', 'Count']

            fig = px.pie(order_status_counts, values='Count', names='State', title='Order Status Distribution')
            st.plotly_chart(fig)

        elif selected_order_management == "Cancel Service Orders":
            st.header("Cancel Service Orders")
            st.write("This section covers the cancellation of service orders.")

        elif selected_order_management == "Workflow Orders":
            st.header("Workflow Orders")
            st.write("This section covers workflow orders.")

        elif selected_order_management == "Resource Orders":
            st.header("Resource Orders")
            st.write("This section covers resource orders.")

        elif selected_order_management == "User Tasks":
            st.header("User Tasks")
            st.write("This section covers user tasks.")

    # Product Domain Tab
    elif selected_main == "Product Domain":
        set_background("https://as1.ftcdn.net/v2/jpg/01/90/61/12/1000_F_190611262_jGbMQB3Tdk2Hk7rQu8PVYPAr8rC8j02D.jpg")
        st.title("Product Domain")
        st.write("This section covers the product domain.")

    # Service Domain Tab
    elif selected_main == "Service Domain":
        set_background("https://as2.ftcdn.net/v2/jpg/05/18/67/24/1000_F_518672490_3WQMQNRVZ9jD0BkWCV2Qz1nlZ2l62xuI.jpg")
        st.title("Service Domain")

        if selected_service == "Catalog":
            st.header("Service Catalog")
            st.write("This section covers the service catalog.")

            # Display the service data
            st.subheader("Service Data")
            AgGrid(service_data, height=300)

            st.subheader("Service Distribution")
            service_distribution = service_data['Code'].value_counts().reset_index()
            service_distribution.columns = ['Service Code', 'Count']

            fig = px.pie(service_distribution, values='Count', names='Service Code', title='Service Distribution')
            st.plotly_chart(fig)

        elif selected_service == "Service Specification":
            st.header("Service Specification")
            st.write("This section covers service specifications.")

        elif selected_service == "Test Specifications":
            st.header("Test Specifications")
            st.write("This section covers test specifications.")

        elif selected_service == "Extra Values":
            st.header("Extra Values")
            st.write("This section covers extra values related to services.")

        elif selected_service == "Order Types":
            st.header("Order Types")
            st.write("This section covers different order types.")

    # Workflow Domain Tab
    elif selected_main == "Workflow Domain":
        set_background("https://as2.ftcdn.net/v2/jpg/05/18/67/24/1000_F_518672490_3WQMQNRVZ9jD0BkWCV2Qz1nlZ2l62xuI.jpg")
        st.title("Workflow Domain")
        st.write("This section covers the workflow domain.")

    # Resource Domain Tab
    elif selected_main == "Resource Domain":
        set_background("https://as1.ftcdn.net/v2/jpg/01/90/61/12/1000_F_190611262_jGbMQB3Tdk2Hk7rQu8PVYPAr8rC8j02D.jpg")
        st.title("Resource Domain")
        st.write("This section covers the resource domain.")

    # Global Tab
    elif selected_main == "Global":
        set_background("https://as2.ftcdn.net/v2/jpg/05/18/67/24/1000_F_518672490_3WQMQNRVZ9jD0BkWCV2Qz1nlZ2l62xuI.jpg")
        st.title("Global")
        st.write("This section covers global aspects of the application.")

# Session State Checker
if st.session_state.logged_in:
    main_app()
else:
    login_page()
