import openai

def compare_documents(file1_path, file2_path, api_key):
    """Compares two documents using OpenAI's ChatGPT API."""
    
    # Read the contents of both files
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        text1 = file1.read()
        text2 = file2.read()
    
    # Define the prompt
    prompt = f"""
    Compare the following two documents:
    
    Document 1:
    {text1}
    
    Document 2:
    {text2}
    
    Provide a summary of similarities and differences, including content, structure, and key points.
    """
    
    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Adjust model if needed
        messages=[
            {"role": "system", "content": "You are an expert in document comparison."},
            {"role": "user", "content": prompt}
        ],
        api_key=api_key
    )
    
    # Extract and return the response
    return response["choices"][0]["message"]["content"]

# Example usage
if __name__ == "__main__":
    file1 = "document1.txt"
    file2 = "document2.txt"
    api_key = "your-openai-api-key"  # Replace with your API key
    
    result = compare_documents(file1, file2, api_key)
    print(result)
