import subprocess
import sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install','requests'])
import requests
def chatgpt_query(prompt):
    api_key = "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"  # Replace with your actual OpenAI API key
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
    
    bl_info = {
    "name": "Simple Text Printer",
    "blender": (4, 2, ),  # Adjust according to your Blender version
    "category": "Object",
}

import bpy

class SimpleTextPrinterPanel(bpy.types.Panel):
    """Creates a Panel in the Tool tab of the 3D Viewport"""
    bl_label = "Simple Text Printer"
    bl_idname = "VIEW3D_PT_text_printer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'  # Place in the Tools tab



    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Create a text input box
        layout.prop(scene, "user_input_text")
        
        # Create a button to print the text
        layout.operator("object.print_text", text="Print Text")

class PrintTextOperator(bpy.types.Operator):
    """Prints the input text to the console"""
    bl_idname = "object.print_text"
    bl_label = "Print Text"

    def execute(self, context):
        # Get the user input
        user_input = context.scene.user_input_text
        print(user_input)  # Print to console
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SimpleTextPrinterPanel)
    bpy.utils.register_class(PrintTextOperator)
    
    # Create a StringProperty to hold user input
    bpy.types.Scene.user_input_text = bpy.props.StringProperty(
        name="Input Text",
        description="Enter text to print",
        default=""
    )

def unregister():
    bpy.utils.unregister_class(SimpleTextPrinterPanel)
    bpy.utils.unregister_class(PrintTextOperator)
    del bpy.types.Scene.user_input_text

if __name__ == "__main__":
    register()