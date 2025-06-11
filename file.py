import gradio as gd

def analyze_text(file):
    text=file.name
    with open(text, 'r',encoding='utf-8') as f:
        text = f.read()
    word_count = len(text.split())
#    char_count = len(text)
    return f"Word Count: {word_count} "

#, Character Count: {char_count}"

interface = gd.Interface(
    fn=analyze_text,
    inputs=gd.File(label="Upload Text File"),
    outputs=gd.Textbox(label="Analysis Result"),
    title="Text File Analyzer",
)

interface.launch(share=True)  # Set share=True to allow public access