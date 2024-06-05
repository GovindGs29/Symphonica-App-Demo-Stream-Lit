# Govind App Networking Symphonica Example
# Version : 1.07

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
from streamlit_option_menu import option_menu

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

# Set page configuration
st.set_page_config(page_title="Symphonica App", page_icon="📊", layout="wide")

# This Function used to generated url links to background images :
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

# Sidebar with nested menu and search functionality
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
            "",
            filtered_order_management_options,
            icons=["file-earmark-text", "file-earmark-x", "file-earmark-check", "file-earmark-code", "file-earmark-person"],
            menu_icon="gear",
            default_index=0,
            orientation="vertical",
            key="order_management_menu"
        )

    if selected_main == "Service Domain":
        # Filter service domain options based on search query
        filtered_service_options = [option for option in service_options if search_query.lower() in option.lower()]

        selected_service = option_menu(
            "",
            filtered_service_options,
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
    
# Order Management Tab
elif selected_main == "Order Management":
    set_background("https://as2.ftcdn.net/v2/jpg/08/24/78/07/1000_F_824780703_2pvuE26gFEqERrVUMvJRSgoUL5NDyNUA.jpg")  # Replace with your background image URL
    st.title("Order Management")
    
    if selected_order_management == "Service Orders":
        st.subheader("Service Orders")
        
        # Filters
        with st.expander("Filters"):
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                order_id = st.text_input("Id")
            with col2:
                order_type = st.selectbox("Order Type", ["All", "CEASE", "PROVIDE"])
            with col3:
                customer_id = st.text_input("Customer Id")
            with col4:
                start_date = st.date_input("Start Date")
            with col5:
                end_date = st.date_input("End Date")

        # Filtering data
        filtered_data = orders_data[
            (orders_data["Id"].str.contains(order_id, case=False)) &
            (orders_data["Order Type"].str.contains(order_type if order_type != "All" else "", case=False)) &
            (orders_data["Customer Id"].str.contains(customer_id, case=False))
        ]
        
        # Displaying data
        st.dataframe(filtered_data)

    elif selected_order_management == "Cancel Service Orders":
        st.subheader("Cancel Service Orders")
        st.write("Information about Cancel Service Orders.")

    elif selected_order_management == "Workflow Orders":
        st.subheader("Workflow Orders")
        st.write("Information about Workflow Orders.")

    elif selected_order_management == "Resource Orders":
        st.subheader("Resource Orders")
        st.write("Information about Resource Orders.")

    elif selected_order_management == "User Tasks":
        st.subheader("User Tasks")
        st.write("Information about User Tasks.")

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
        st.dataframe(service_data)
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
st.markdown("Built with ❤️, Thanks for watching my app ~ Govind!!!")
