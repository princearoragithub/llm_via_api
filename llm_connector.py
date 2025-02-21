from typing import Literal, Optional
import os
from dotenv import load_dotenv
from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import OllamaLLM

# Load environment variables
load_dotenv()

LLMProvider = Literal["openai", "anthropic", "gemini", "ollama"]

def get_llm_response(
    provider: LLMProvider,
    prompt: str,
    model: Optional[str] = None,
    temperature: float = 0.7
) -> str:
    """
    Get a response from a specified LLM provider.
    
    Args:
        provider: The LLM provider to use ("openai", "anthropic", "gemini", or "ollama")
        prompt: The input prompt/question for the LLM
        model: Specific model to use (optional, provider-dependent)
        temperature: Controls randomness in the response (0.0 to 1.0)
    
    Returns:
        str: The LLM's response
    
    Raises:
        ValueError: If the provider is not supported or required configuration is missing
    """
    
    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key not found in environment variables")
        
        llm = ChatOpenAI(
            api_key=api_key,
            model_name=model or "gpt-3.5-turbo",
            temperature=temperature
        )
    
    elif provider == "anthropic":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("Anthropic API key not found in environment variables")
        
        llm = ChatAnthropic(
            api_key=api_key,
            model_name=model or "claude-3-sonnet-20240229",
            temperature=temperature
        )
    
    elif provider == "gemini":
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("Google API key not found in environment variables")
        
        llm = ChatGoogleGenerativeAI(
            api_key=api_key,
            model_name=model or "gemini-pro",
            temperature=temperature
        )
    
    elif provider == "ollama":
        # Ollama runs locally, no API key needed
        llm = OllamaLLM(
            model=model or "llama2",
            temperature=temperature
        )
    
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
    
    # Get the response from the LLM
    response = llm.invoke(prompt)
    return response.content if hasattr(response, 'content') else str(response)

# Example usage
if __name__ == "__main__":
    # Example with Ollama (local)
    try:
        response = get_llm_response(
            provider="ollama",
            prompt="Generate a creative tweet about a new AI project.",
            model="deepseek-r1:8b",
            temperature=0.7
        )
        print(f"Generated Tweet:\n{response}")
    except ValueError as e:
        print(f"Error: {e}") 