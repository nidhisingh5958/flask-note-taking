import streamlit as st
import os
#from dotenv import load_dotenv
#load_dotenv()
import google.generativeai as genai
from  PIL import Image
#Google_API_KEY=st.secrets["GOOGLE_API_KEY"]
#os.environ["GOOGLE_API_KEY"]=Google_API_KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
def get_gemini_response(input_prompt,image):
    model=genai.GenerativeModel("gemini-1.5-pro")
    response=model.generate_content([input_prompt,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    #check if file uploaded
    if uploaded_file is not None:
        #read the file into bytes
        bytes_data=uploaded_file.getvalue()

        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
st.set_page_config(page_title="Thumbnail reader")
st.header("Thumbnail Reader App")
uploaded_file=st.file_uploader("chooes an image .....",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Images.",use_column_width=True)

submit=st.button("Read the thumbnail")
input_prompt="""
    You are export Thumbnail reader where you read the thumbnail and give response  according to the thumbnail
    and give your opinion according to that,

"""
if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.header("The Response is ")
    st.write(response)