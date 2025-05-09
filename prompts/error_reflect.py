from langchain_core.prompts import ChatPromptTemplate

reflect_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a senior Python developer helping debug code.
            ---
            Task Description: {task}
            ---
            Below is the Python code organized in a list:
            {code}
            ---
            Requirements: {requirements}
            ---
            Explanation of the logic:
            {explanation}
            ---
            The following error occurred during execution:
            {error}
            ---
            Output:
                1. A corrected version of the code, formatted the same way (flat list alternating section names and code blocks).
                    - Use only the following section names (as applicable): 
                        ["Data Ingestion", "Data Cleaning", "Data Transformation", "Feature Engineering", "Model Training", "Model Evaluation", etc.]
                    - Each code block must be enclosed in triple backticks and must be valid Python code.
                    - Example:
                        [
                            "Data Ingestion", "`Data Ingestion code`",
                            "Data Cleaning", "`Data Cleaning Code`"
                        ]
                2. A brief explanation of the overall code logic (step-by-step or modular). Make it similarly like the code:
                    - Example:
                    [
                        "Data Ingestion", "`Data Ingestion Explanation`",
                        "Data Cleaning", "`Data Cleaning Explanation`"
                    ]
                3. An updated or corrected list of requirements (if needed).
            """
        )
    ]
)