# import gradio as gr

# def souparna(name,i):
#     return "hello,"+ name + "$" + int(i)

# demo=gr.Interface(
#     fn=souparna,
#     inputs=["text","slider"],
#     outputs=["text"],
# )

# demo.launch()

def transform_history(history):
    new_history = []
    for chat in history:
        new_history.append({"parts": [{"text": chat[0]}], "role": "user"})
        new_history.append({"parts": [{"text": chat[1]}], "role": "model"})
    return new_history

def response(message, history):
    global chat
    # The history will be the same as in Gradio, the 'Undo' and 'Clear' buttons will work correctly.
    chat.history = transform_history(history)
    response = chat.send_message(message)
    response.resolve()

    # Each character of the answer is displayed
    for i in range(len(response.text)):
        time.sleep(0.05)
        yield response.text[: i+1]

gr.ChatInterface(response,
                 title='Gemini Chat',
                 textbox=gr.Textbox(placeholder="Question to Gemini"),
                 retry_btn=None).launch(debug=True)