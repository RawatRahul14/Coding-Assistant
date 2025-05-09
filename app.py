import streamlit as st
from graph import build_graph

st.title("🧠 Self-Improving Coding Assistant")

user_prompt = st.text_area("Enter a coding task:", height=100)
max_steps = st.slider("Max retries", 1, 5, 3)

if st.button("Run Assistant"):
    with st.spinner("Running..."):
        app = build_graph()

        state = {
            "prompt": user_prompt,
            "code": [],
            "explanation": [],
            "requirements": "",
            "error": "",
            "output": "",
            "step_count": 0,
            "max_steps": max_steps,
            "final": None
        }

        result = app.invoke(state)

        # Show Required Installs
        st.subheader("📦 Required Installs")
        st.code(result["requirements"] or "None", language="bash")

        # Interleaved Explanation + Code
        st.markdown("---")
        st.subheader("🧠 Explanation and Code")

        explanation = result["explanation"]
        code = result["code"]

        section_count = min(len(explanation), len(code)) // 2

        for i in range(section_count):
            section_name = explanation[i * 2]
            section_expl = explanation[i * 2 + 1]
            section_code = code[i * 2 + 1]

            st.markdown(f"### 🔹 {section_name}")
            st.markdown(f"**Explanation:** {section_expl}")
            st.code(section_code, language="python")
            st.markdown("---")