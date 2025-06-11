import gradio as gd

def square_number(num):
    return num ** 2 

interface = gd.Interface(
    fn=square_number,
    inputs=gd.Slider(minimum=0, maximum=100, step=1, label="Select a Number"),
    outputs=gd.Number(label="Squared Value"),
    title="Square a Number",
)


interface.launch(share=True)  # Set share=True to allow public access