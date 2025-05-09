import streamlit as st
from graph import build_graph

st.title("🧠 Self-Improving Coding Assistant")

user_prompt = st.text_area("Enter a coding task:", height = 100)
max_steps = st.slider("Max retries", 1, 5, 3)

if st.button("Run Assistant"):
    with st.spinner("Running..."):
        app = build_graph()

        state = {
            "prompt": user_prompt,
            "code": "",
            "output": "",
            "error": "",
            "step_count": 0,
            "max_steps": max_steps,
            "final": None
        }

        result = app.invoke(state)

        st.subheader("📄 Final Code")
        st.code(result["code"], language="python")

        if result["final"] == "success":
            st.success("✅ Execution successful!")
            st.subheader("🖨️ Output")
        else:
            st.error("❌ Failed after max retries.")
            st.subheader("🚫 Last Error")