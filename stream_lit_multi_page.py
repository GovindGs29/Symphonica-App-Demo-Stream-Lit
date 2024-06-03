import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Govind Sample Networking Concelpt - Multiple Tab App", page_icon="📊", layout="wide")

# Sidebar menu for navigation
with st.sidebar:
    selected = option_menu(
        "Main Menu", ["Home", "Networking Options", "No-Code SaaS"],
        icons=["house", "diagram-3", "cloud"],
        menu_icon="cast", default_index=0,
    )

# Home Tab
if selected == "Home":
    st.title("Welcome to the Multi-Tab App")
    st.write("""
    This is a sample Streamlit app with multiple tabs. Use the sidebar to navigate between different sections.
    """)

# Networking Options Tab
elif selected == "Networking Options":
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

# Footer
st.markdown("---")
st.markdown("Built with StreamLit - Govind Gs ")
