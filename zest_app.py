import streamlit as st
from huggingface_hub import InferenceClient

# Aapka naya Token yahan paste karein
HF_TOKEN = "hf_MIAUxChXKtmNwdyVafjUcUoXwGhK0YhVnE" 
client = InferenceClient(api_key=HF_TOKEN)

st.set_page_config(page_title="Zest AI ⚡", page_icon="🚀")
st.title("⚡ ZEST AI - Pro Edition")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

if prompt := st.chat_input("Zest se pucho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat_completion(
            model="microsoft/Phi-3-mini-4k-instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        ans = response.choices[0].message.content
        st.markdown(ans)
        st.session_state.messages.append({"role": "assistant", "content": ans})
