import gradio as gd

def reverse_text(text):
    return text[::-1]

interface = gd.Interface(
    fn=reverse_text,
    inputs=gd.Textbox(label="Enter Text"),
    outputs=gd.Textbox(label="Reversed Text"),
    title="Text Reverser",
)

interface.launch(share=True)  # Set share=True to allow public access