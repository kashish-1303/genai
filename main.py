

# from openai import OpenAI
# import re

# client = OpenAI(api_key="sk-proj-elcxIFzuutp7nFKjtzhvT3BlbkFJARwOefUtjKLsS8fgkHzJ")

# def chat_with(prompt):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content.strip()
            
# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit", "exit", "bye"]:
#             break

#         response = chat_with(user_input)
#         response = re.sub(r'^\d+\.\s*', '', response, flags=re.MULTILINE)
#         sentences = re.split(r'(?<=\.)\s+', response.strip())
#         sentences = [sentence if sentence.endswith('.') else sentence + '.' for sentence in sentences]

#         c=0
#         for sentence in sentences:
#             c = c+1
#             response1 = client.images.generate(
#                     model="dall-e-3",
#                     prompt=sentence,
#                     size="1024x1024",
#                     quality="standard",
#                     n=1,
#                     style="natural")
#             image_url = response1.data[0].url
#             print("Chatbot:Step",c,"-",sentence)
#             print("Generated image URL: ",image_url)

# import streamlit as st
# from openai import OpenAI
# import re

# # Initialize OpenAI client
# client = OpenAI(api_key="sk-proj-elcxIFzuutp7nFKjtzhvT3BlbkFJARwOefUtjKLsS8fgkHzJ")

# def chat_with(prompt):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content.strip()

# def generate_image(prompt):
#     response = client.images.generate(
#         model="dall-e-3",
#         prompt=prompt,
#         size="1024x1024",
#         quality="standard",
#         n=1,
#         style="natural"
#     )
#     return response.data[0].url

# # Streamlit app
# st.title("Chatbot with Image Generation")

# user_input = st.text_input("You: ", "")
# if st.button("Send"):
#     if user_input.lower() in ["quit", "exit", "bye"]:
#         st.stop()

#     response = chat_with(user_input)
#     response = re.sub(r'^\d+\.\s*', '', response, flags=re.MULTILINE)
#     sentences = re.split(r'(?<=\.)\s+', response.strip())
#     sentences = [sentence if sentence.endswith('.') else sentence + '.' for sentence in sentences]

#     for c, sentence in enumerate(sentences, 1):
#         image_url = generate_image(sentence)
#         st.write(f"Chatbot: Step {c} - {sentence}")
#         st.image(image_url, caption=f"Generated Image for Step {c}")

# # Run Streamlit app
# if __name__ == "__main__":
#     st.set_page_config(page_title="Chatbot with Image Generation")
#     st.experimental_rerun()
            
import streamlit as st
from openai import OpenAI
import re

# Set Streamlit page configuration
st.set_page_config(page_title="Chatbot with Image Generation")

# Initialize OpenAI client
client = OpenAI(api_key="sk-proj-elcxIFzuutp7nFKjtzhvT3BlbkFJARwOefUtjKLsS8fgkHzJ")

def chat_with(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
        style="natural"
    )
    return response.data[0].url

# Streamlit app
st.title("Chatbot with Image Generation")

user_input = st.text_input("You: ", "")
if st.button("Send"):
    if user_input.lower() in ["quit", "exit", "bye"]:
        st.stop()

    response = chat_with(user_input)
    response = re.sub(r'^\d+\.\s*', '', response, flags=re.MULTILINE)
    sentences = re.split(r'(?<=\.)\s+', response.strip())
    sentences = [sentence if sentence.endswith('.') else sentence + '.' for sentence in sentences]

    for c, sentence in enumerate(sentences, 1):
        image_url = generate_image(sentence)
        st.write(f"Chatbot: Step {c} - {sentence}")
        st.image(image_url, caption=f"Generated Image for Step {c}")

