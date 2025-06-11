import gradio as gd

def add_number(a,b):
    return a + b

interface = gd.Interface(
    fn=add_number,
    inputs=[
        gd.Number(label="First Number"),
        gd.Number(label="Second Number")
    ],
    outputs=gd.Number(label="Sum"),)

interface.launch(share=True)