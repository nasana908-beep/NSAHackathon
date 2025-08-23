import streamlit as st
from openai import OpenAI

# Initialize client
client = OpenAI(api_key="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")  # or use environment variable

st.set_page_config(page_title="Your Mountaineering Guide", page_icon="")

st.title("💬 Your Mountaineering Guide")

# Store conversation in Streamlit session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get OpenAI response
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-4o", "gpt-3.5-turbo"
        messages=st.session_state["messages"]
    )
    reply = response.choices[0].message.content

    # Add assistant message
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)