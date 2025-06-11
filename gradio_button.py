import gradio as gd

def correct_answer(selected_option):
    if selected_option == "python":
        return "Correct! python is the right answer."
    else:
        return "Incorrect. The correct answer is Option A."
    


interface = gd.Interface(
    fn=correct_answer,
    inputs=gd.Radio(
        choices=["python", "java", "c++", "javascript"],
        label="What is the best programming language?",
        type="value"
    ),
    outputs=gd.Textbox(label="Result"),
    title="Programming Language Quiz",
)

interface.launch(share=True)  # Set share=True to allow public access