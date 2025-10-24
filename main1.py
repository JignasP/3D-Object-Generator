import subprocess
import sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install','requests'])
import requests
def chatgpt_query(prompt):
    api_key = ""  # Replace with your actual OpenAI API key
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # You can also use other models
        "messages": [{"role": "user", "content": prompt}]
    }

    # Send request to the API
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()  # Return the entire response
    else:
        return {"error": response.text}  # Return error messagecr


# Example usage
i = 0
prompt=input("Ask gpt:")
result = chatgpt_query(prompt)
x=result["choices"][0]["message"]["content"]


if 'choices' in result:
   i=1
else:
    print("Error:",result)

m = x.find("import")
n = x.rfind(")")

code = x[m:n+1]
print(code+")")

# Install the 'requests' package
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])

# Function to query OpenAI's API
def chatgpt_query(prompt):
    api_key = "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"  # Replace with your actual OpenAI API key
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # You can use other models like gpt-4, etc.
        "messages": [{"role": "user", "content": prompt}]
    }

    # Send request to the API
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()  # Return the entire response
    else:
        return {"error": response.text}  # Return error message


# Example usage
prompt = "Generate Python code to create a cube in Blender."
result = chatgpt_query(prompt)

# Ensure that 'choices' exists in the result
if 'choices' in result:
    response_content = result["choices"][0]["message"]["content"]
    # Find the code between 'import' and the last closing parenthesis
    m = response_content.find("import")
    n = response_content.rfind(")")
    
    if m != -1 and n != -1:
        code = response_content[m:n+1]
        print("Copy and paste this code into Blender's Python console:")
        print(code)
    else:
        print("No valid code found.")
else:
    print("Error:", result)














