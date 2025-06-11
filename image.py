import gradio as gd

def resize_image(image, width, height):
    if image is None:
        return None
    return image.resize((width, height))


interface = gd.Interface(
    fn=resize_image,
    inputs=[
        gd.Image(type='pil',label="Upload Image"),
        gd.Number(label="Width(px)"),
        gd.Number(label="Height(px)")
    ],
    outputs=gd.Image(type="pil",label="Resized Image"),
    title="Image Resizer",
)

interface.launch(share=True)  # Set share=True to allow public access