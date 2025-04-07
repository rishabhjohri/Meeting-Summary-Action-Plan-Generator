import streamlit as st
import requests

st.set_page_config(page_title="Meeting Summary & Action Plan Generator")

st.title("📄 Meeting Summary & Action Plan Generator")

uploaded_file = st.file_uploader("Upload a .txt or .pdf meeting transcript", type=["txt", "pdf"])

if uploaded_file is not None:
    st.success("File uploaded. Sending to Upload Service...")

    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
    upload_response = requests.post("http://127.0.0.1:8000/upload/", files=files)

    if upload_response.status_code == 200:
        raw_text = upload_response.json()["text"]
        st.subheader("📝 Raw Transcript:")
        st.text_area("", raw_text, height=200)

        if st.button("Generate Summary"):
            with st.spinner("🧠 Generating summary..."):
                summary_response = requests.post("http://127.0.0.1:8001/summarize/", json={"text": raw_text})

            if summary_response.status_code == 200:
                summary = summary_response.json()["summary"]
                st.subheader("🧠 Summary:")
                st.text_area("", summary, height=150)

                with st.spinner("🗂️ Generating action plan..."):
                    plan_response = requests.post("http://127.0.0.1:8002/plan/", json={"summary": summary})

                if plan_response.status_code == 200:
                    action_plan = plan_response.json()["action_plan"]
                    st.subheader("🗂️ Action Plan:")
                    st.text_area("", action_plan, height=200)
                else:
                    st.error("Planner service error: " + plan_response.text)
            else:
                st.error("Summarizer service error: " + summary_response.text)
    else:
        st.error("Upload service error: " + upload_response.text)
