import gradio as gd

def calcultor(operation, num1, num2):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"    
    

interface = gd.Interface(
    fn=calcultor,
    inputs=[
        gd.Dropdown(
            choices=["Add", "Subtract", "Multiply", "Divide"],
            label="Select Operation"
        ),
        gd.Number(label="First Number"),
        gd.Number(label="Second Number")
    ],
    outputs=gd.Textbox(label="Result"),
    title="Simple Calculator",
)

interface.launch(share=True)  # Set share=True to allow public acces