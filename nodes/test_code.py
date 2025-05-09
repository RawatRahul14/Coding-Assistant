from utils.state_schema import AgentState

def test_code(state: AgentState):
    try:
        # Step 1: Convert flat list to dict
        raw_code_list = state["code"]
        sectioned_code = {
            raw_code_list[i]: raw_code_list[i + 1]
            for i in range(0, len(raw_code_list), 2)
        }

        # Step 2: Combine all code blocks into one executable string
        combined_code = ""
        for section, code_block in sectioned_code.items():
            if code_block.startswith("```") and code_block.endswith("```"):
                code_block = code_block.strip("`").strip()  # Remove the triple backticks
                # Remove 'python' if it's like ```python\n...
                if code_block.startswith("python\n"):
                    code_block = code_block[len("python\n"):]
            combined_code += code_block + "\n\n"

        # Step 3: Execute the code safely
        local_env = {}
        exec(combined_code, {}, local_env)

        return {
            **state,
            "output": str(local_env),
            "error": "",
            "final": "success"
        }

    except Exception as e:
        return {
            **state,
            "output": "",
            "error": str(e),
            "final": None
        }