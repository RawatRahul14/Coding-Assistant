def extract_code_block(text: str) -> str:
    """
    Extracts Python code from a string, removing Markdown-style fences or explanations.
    """
    import re

    # Look for code block inside triple backticks
    match = re.search(r"```(?:python)?\n(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Fallback: return text as-is (best effort)
    return text.strip()