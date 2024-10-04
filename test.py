bl_info = {
    "name": "Simple Text Printer",
    "blender": (4, 2, ),  # Adjust according to your Blender version
    "category": "Object",
}

import bpy
import requests



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


    

class PrintTextOperator(bpy.types.Operator):
    """Prints the input text to the console"""
    bl_idname = "object.print_text"
    bl_label = "Print Text"






    def execute(self, context):
        # Get the user input
        user_input = context.scene.user_input_text
        print(user_input)  # Print to console
        result = chatgpt_query(user_input)
        print(result)
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
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
