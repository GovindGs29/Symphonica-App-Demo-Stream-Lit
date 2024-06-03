import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# # Custom CSS to add icons to the sidebar
# st.markdown("""
#     <style>
#         .icon::before {
#             content: '\\1F3E0'; /* Default Home icon */
#             font-family: 'Emoji'; 
#             font-size: 1.5rem;
#             margin-right: 0.5rem;
#         }
#         .icon-party::before { content: '\\1F464'; } /* Party icon */
#         .icon-order::before { content: '\\1F4E6'; } /* Order icon */
#         .icon-product::before { content: '\\1F4CA'; } /* Product icon */
#         .icon-service::before { content: '\\2699'; } /* Service icon */
#         .icon-workflow::before { content: '\\1F4C4'; } /* Workflow icon */
#         .icon-resource::before { content: '\\1F4DD'; } /* Resource icon */
#         .icon-global::before { content: '\\1F310'; } /* Global icon */
#     </style>
# """, unsafe_allow_html=True)


# Sample data for Service Specifications
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

# Sidebar with nested menu
with st.sidebar:
    st.image("https://www.intraway.com/wp-content/uploads/2022/09/Sym-Demo-Series-logo-300x82.png", caption="SYMPHONICA", use_column_width=True)  # Replace with your logo
    st.text_input("Search")

    selected_main = option_menu(
        "Main Menu",
        ["Home", "Party Domain", "Order Management", "Product Domain", "Service Domain", "Workflow Domain", "Resource Domain", "Global"],
        icons=["house", "person", "box", "table", "gear", "file-earmark", "pencil", "globe"],
        menu_icon="cast",
        default_index=0,
    )

    if selected_main == "Service Domain":
        selected_service = option_menu(
            "",
            ["Catalog", "Service Specification", "Test Specifications", "Extra Values", "Order Types"],
            icons=["book", "file-earmark-text", "file-earmark-check", "file-earmark-plus", "file-earmark-code"],
            menu_icon="gear",
            default_index=0,
            orientation="vertical"
        )

# Sidebar menu for navigation
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Home", "Party Domain", "Order Management", "Product Domain", "Service Domain", "Workflow Domain", "Resource Domain", "Global"],
        icons=["house", "person", "box", "table", "gear", "file-earmark", "pencil", "globe"],
        menu_icon="cast",
        default_index=0,
    )

# Home Tab
if selected == "Home":
    st.title("Welcome to Symphonica")
    st.write("This is the home page. Use the sidebar to navigate to different sections.")

# Party Domain Tab
elif selected == "Party Domain":
    st.title("Party Domain")
    st.write("Information about Party Domain.")

# Order Management Tab
elif selected == "Order Management":
    st.title("Order Management")
    st.write("Information about Order Management.")

# Product Domain Tab
elif selected == "Product Domain":
    st.title("Product Domain")
    st.write("Information about Product Domain.")

# Service Domain Tab
elif selected == "Service Domain":
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
    st.write("Information about Service Domain.")

# Workflow Domain Tab
elif selected == "Workflow Domain":
    st.title("Workflow Domain")
    st.write("Information about Workflow Domain.")

# Resource Domain Tab
elif selected == "Resource Domain":
    st.title("Resource Domain")
    st.write("Information about Resource Domain.")

# Global Tab
elif selected == "Global":
    st.title("Global")
    st.write("Information about Global settings.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Symphonica Enthusiast")
