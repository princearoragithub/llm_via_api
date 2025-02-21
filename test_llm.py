from llm_connector import get_llm_response

# Replace 'openai' with 'anthropic' or 'gemini' depending on which API key you have
try:
    response = get_llm_response(
        provider="openai",
        prompt="What is the capital of France? Please answer in one word.",
        temperature=0.7
    )
    print(f"Response: {response}")
except ValueError as e:
    print(f"Error: {e}") 