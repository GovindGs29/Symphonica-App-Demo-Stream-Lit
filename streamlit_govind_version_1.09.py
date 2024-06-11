# Govind App Networking Symphonica Example
# Version : 1.08

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
from streamlit_option_menu import option_menu
from st_aggrid import AgGrid, GridOptionsBuilder

# Sample data for Service Specifications
service_options = ["Catalog", "Service Specification", "Test Specifications", "Extra Values", "Order Types"]
main_options = ["Home", "Party Domain", "Order Management", "Product Domain", "Service Domain", "Workflow Domain", "Resource Domain", "Global"]

data_for_graph = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
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

# Initial users data
if "users" not in st.session_state:
    st.session_state.users = {
        "usernames": ["admin", "guest"],
        "passwords": ["admin_pass", "guest_pass"]
    }

# Set page configuration
st.set_page_config(page_title="Symphonica App", page_icon="📊", layout="wide")

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

# Login function
def login(users):
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    if st.sidebar.button("Login"):
        if username in users["usernames"] and password == users["passwords"][users["usernames"].index(username)]:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.sidebar.success("Logged in as {}".format(username))
        else:
            st.sidebar.error("Invalid username or password")

# Register function
def register(users):
    st.sidebar.title("Register")
    new_username = st.sidebar.text_input("New Username")
    new_password = st.sidebar.text_input("New Password", type="password")
    
    if st.sidebar.button("Register"):
        if new_username not in users["usernames"]:
            st.session_state.users["usernames"].append(new_username)
            st.session_state.users["passwords"].append(new_password)
            st.sidebar.success("User registered successfully")
        else:
            st.sidebar.error("Username already exists")

# Forgot password function
def forgot_password(users):
    st.sidebar.title("Forgot Password")
    forgot_username = st.sidebar.text_input("Username for password reset")
    
    if st.sidebar.button("Reset Password"):
        if forgot_username in users["usernames"]:
            # For simplicity, resetting to a default password
            st.session_state.users["passwords"][users["usernames"].index(forgot_username)] = "default_pass"
            st.sidebar.success("Password reset to 'default_pass'. Please login and change your password.")
        else:
            st.sidebar.error("Username not found")

# Check login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login(st.session_state.users)
    st.sidebar.markdown("---")
    register(st.session_state.users)
    st.sidebar.markdown("---")
    forgot_password(st.session_state.users)
else:
    # Main content after login
    with st.sidebar:
        st.image("https://www.intraway.com/wp-content/uploads/2022/09/Sym-Demo-Series-logo-300x82.png", caption="SYMPHONICA", use_column_width=True)  # Replace with your logo
        search_query = st.text_input("Search")

        # Filter main menu options based on search query
        filtered_main_options = [option for option in main_options if search_query.lower() in option.lower()]

        selected_main = option_menu(
            "Main Menu",
            filtered_main_options,
            icons=["house", "person", "box", "table", "gear", "file-earmark", "pencil", "globe"],
            menu_icon="cast",
            default_index=0,
            key="main_menu"
        )

        # Order Management submenu
        if selected_main == "Order Management":
            order_management_options = ["Service Orders", "Cancel Service Orders", "Workflow Orders", "Resource Orders", "User Tasks"]
            filtered_order_management_options = [option for option in order_management_options if search_query.lower() in option.lower()]
            selected_order_management = option_menu(
                "Order Management",
                filtered_order_management_options,
                icons=["box", "x", "clipboard", "inboxes", "check2-square"],
                menu_icon="table",
                default_index=0,
                key="order_management_menu"
            )

        # Service Domain submenu
        if selected_main == "Service Domain":
            service_options = ["Catalog", "Service Specification", "Test Specifications", "Extra Values", "Order Types"]
            filtered_service_options = [option for option in service_options if search_query.lower() in option.lower()]
            selected_service = option_menu(
                "Service Domain",
                filtered_service_options,
                icons=["list", "info-circle", "check2-circle", "plus", "tags"],
                menu_icon="gear",
                default_index=0,
                key="service_domain_menu"
            )

    # Home Page
    if selected_main == "Home":
        set_background("https://as1.ftcdn.net/v2/jpg/05/14/95/12/1000_F_514951224_2dxMLbIw5qNRdPGD003chpbVcxWtcp7K.jpg")
        st.title("Home")
        st.write("Welcome to the Govind Networking Streamlit Demo App!")

    # Party Domain Tab
    elif selected_main == "Party Domain":
        set_background("https://as2.ftcdn.net/v2/jpg/08/24/78/07/1000_F_824780703_2pvuE26gFEqERrVUMvJRSgoUL5NDyNUA.jpg")
        st.title("Networking - The Basics")
        st.write("""
        ## Networking Basics
        Networking is the practice of connecting computers and other devices together to share resources and information.
        """)
        st.header("1. What is a Network?")
        st.write("""
        A network is a collection of computers, servers, mainframes, network devices, peripherals, or other devices connected to one another to allow the sharing of data.
        """)
        st.header("2. IP Address")
        st.write("""
        An IP address is a unique identifier assigned to each device connected to a network. It allows devices to communicate with each other.
        """)
        st.header("3. Subnetting")
        st.write("""
        Subnetting is the process of dividing a network into smaller subnetworks (subnets).
        """)

    # Order Management Tab
    elif selected_main == "Order Management":
        set_background("https://as2.ftcdn.net/v2/jpg/05/36/43/69/1000_F_536436947_D5gjAr3kwqCJrAjD8SuEGEq3dD3dhMfH.jpg")
        st.title(f"{selected_order_management}")

        if selected_order_management == "Service Orders":
            st.subheader("Service Orders")
            st.write("Displaying data for Service Orders...")

            # Display service orders data using Ag-Grid
            gb = GridOptionsBuilder.from_dataframe(orders_data)
            gb.configure_pagination(paginationAutoPageSize=True)
            gb.configure_side_bar()
            gridOptions = gb.build()

            AgGrid(orders_data, gridOptions=gridOptions, enable_enterprise_modules=True)

    # Service Domain Tab
    elif selected_main == "Service Domain":
        set_background("https://as2.ftcdn.net/v2/jpg/05/15/63/85/1000_F_515638554_4wecUEOe90Yvg8bf24KaR86CdX61zNO3.jpg")
        st.title(f"{selected_service}")

        if selected_service == "Catalog":
            st.subheader("Catalog")
            st.write("Displaying data for Catalog...")

            # Display catalog data using Ag-Grid
            gb = GridOptionsBuilder.from_dataframe(service_data)
            gb.configure_pagination(paginationAutoPageSize=True)
            gb.configure_side_bar()
            gridOptions = gb.build()

            AgGrid(service_data, gridOptions=gridOptions, enable_enterprise_modules=True)

    # Visualization Tab
    elif selected_main == "Product Domain":
        set_background("https://as1.ftcdn.net/v2/jpg/05/44/22/63/1000_F_544226371_7TrcEOZGAAXifMWbTtrCEhwRiACyYmPj.jpg")
        st.title("Visualization")
        st.write("This section is dedicated to visualizing data using different charts and graphs.")

        st.header("Bar Chart")
        bar_chart = alt.Chart(data_for_graph).mark_bar().encode(
            x='Category',
            y='Values'
        )
        st.altair_chart(bar_chart, use_container_width=True)

        st.header("Line Chart")
        line_chart = alt.Chart(data_for_graph).mark_line().encode(
            x='Category',
            y='Values'
        )
        st.altair_chart(line_chart, use_container_width=True)

        st.header("Pie Chart")
        pie_chart = px.pie(data_for_graph, values='Values', names='Category')
        st.plotly_chart(pie_chart)

    # Workflow Domain Tab
    elif selected_main == "Workflow Domain":
        set_background("https://as1.ftcdn.net/v2/jpg/03/02/73/60/1000_F_302736098_nFY5k09G15PfDpDUpkVcxJS9DdAm5aQn.jpg")
        st.title("Workflow Domain")
        st.write("""
        This section covers multiple graph data related to the Workflow Domain.
        """)

        st.header("Workflow Graph 1")
        workflow_data = pd.DataFrame({
            'Task': ['Task A', 'Task B', 'Task C', 'Task D'],
            'Duration': [5, 3, 4, 2]
        })
        workflow_bar_chart = px.bar(workflow_data, x='Task', y='Duration', title="Workflow Task Durations")
        st.plotly_chart(workflow_bar_chart)

        st.header("Workflow Graph 2")
        workflow_line_chart = alt.Chart(workflow_data).mark_line().encode(
            x='Task',
            y='Duration'
        )
        st.altair_chart(workflow_line_chart, use_container_width=True)

    # Resource Domain Tab
    elif selected_main == "Resource Domain":
        set_background("https://as1.ftcdn.net/v2/jpg/02/27/38/30/1000_F_227383025_cj6qHRFxjJttodnD3d5ZSmZxtnuow8vC.jpg")
        st.title("Resource Domain")
        st.write("""
        This section covers multiple graph data related to the Resource Domain.
        """)

        st.header("Resource Graph 1")
        resource_data = pd.DataFrame({
            'Resource': ['Resource A', 'Resource B', 'Resource C', 'Resource D'],
            'Usage': [75, 50, 90, 60]
        })
        resource_bar_chart = px.bar(resource_data, x='Resource', y='Usage', title="Resource Usage")
        st.plotly_chart(resource_bar_chart)

        st.header("Resource Graph 2")
        resource_pie_chart = px.pie(resource_data, values='Usage', names='Resource', title="Resource Usage Distribution")
        st.plotly_chart(resource_pie_chart)

    # Global Tab
    elif selected_main == "Global":
        set_background("https://as2.ftcdn.net/v2/jpg/05/14/95/18/1000_F_514951833_UkqUcmJx5CBN6mR1D2VyYJfXPa98MS7k.jpg")
        st.title("Global")
        st.write("""
        This section covers global data and visualizations.
        """)

        st.header("Global Chart")
        global_data = pd.DataFrame({
            'Region': ['North America', 'Europe', 'Asia', 'South America'],
            'Value': [400, 300, 500, 200]
        })
        global_bar_chart = px.bar(global_data, x='Region', y='Value', title="Global Values by Region")
        st.plotly_chart(global_bar_chart)

        st.header("Global Pie Chart")
        global_pie_chart = px.pie(global_data, values='Value', names='Region', title="Global Value Distribution")
        st.plotly_chart(global_pie_chart)

# Footer
st.markdown("---")
st.markdown("Built with ❤️, Thanks for watching my app ~ Govind!!!")
