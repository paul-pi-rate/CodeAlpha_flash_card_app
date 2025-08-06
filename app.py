import streamlit as st

# App title
st.title("🧠 Bolt AI App Clone with Streamlit")

# Sidebar
st.sidebar.title("🔧 Settings")
user_name = st.sidebar.text_input("Enter your name", "Guest")

# Main area
st.write(f"Hello, **{user_name}**! 👋")
st.write("This is a basic Streamlit app that mimics a Bolt AI-generated app.")

# Input form
st.subheader("📥 User Input")
user_input = st.text_input("Say something:")

# Display user input
if user_input:
    st.success(f"You said: {user_input}")

# Optionally do something with input (e.g., basic sentiment check)
if user_input:
    if "bad" in user_input.lower():
        st.warning("⚠️ That seems negative!")
    elif "good" in user_input.lower():
        st.info("😊 Glad to hear that!")

# Footer
st.markdown("---")
st.markdown("✅ Built with [Streamlit](https://streamlit.io)")
