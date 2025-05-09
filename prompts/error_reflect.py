from langchain_core.prompts import ChatPromptTemplate

reflect_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a senior Python developer helping debug code.
            ---
            Below is the python code for the given task: {task}
            ---
            Below is the Python code written to solve the task:
            **code**: {code}
            **Requirements**: {requirements} (This should always contain pip installs)
            **Explanation**: {explanation}
            ---
            However, the following error occurs when the code is executed:
            {error}
            ---
            Output:
                1. A corrected version of the code.
                2. A clear explanation of the issue and your fix.
                3. An updated or corrected list of requirements (if needed).
            """
        )
    ]
)