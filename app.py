import streamlit as st
import pathlib
import google.generativeai as genai
from api_key import api_key
import base64

# api key
genai.configure(api_key=api_key)

# lower the temperature less creative the model becomes
generation_config = {
    "temperature": 0.4, # Reduced for medical accuracy
    "top_p": 1,
    "top_k": 64,
    "max_output_tokens": 8192,
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]
system_prompt = """As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining images. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the images. 
Your responsibilities include:
1. Detailed Analysis:
Thoroughly analyze each image, focusing on identifying any abnormal findings.
2. Finding Reports: 
Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format.
3. Recommendations and Next Steps: 
Based on your analysis, suggest potential next steps, including further tests or treatments as applicable.
4. Treatment Suggestions: 
If appropriate, recommend possible treatment options or interventions.

Important Notes:
1. Scope of Responses: Only respond if the image pertains to human health issues.
2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image.' 
3. Disclaimer: Accompany your analysis with the disclaimer:
"Consult with a doctor before making any decisions."

Please provide me an output response with these 4 headings Detailed Analysis, Finding Reports, Recommendations and Next Steps, Treatment Suggestions and disclaimer.
"""

# model configuration
model = genai.GenerativeModel(model_name="gemini-pro-vision", 
                            generation_config=generation_config,
                            safety_settings=safety_settings)

st.set_page_config(page_title="LyfeHub", page_icon="stethoscope")

# logo
st.image("logo-color.png", width=200,)

# title
st.markdown("<h1 style='text-align: center; font-family: Roboto Slab'>Welcome to LyfeHub</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='font-family: Roboto Slab'>An application that will provide treatment options using images.</h3>", unsafe_allow_html=True)

upload_file = st.file_uploader("Upload some images so we can help you more efficiently", type=["png", "jpeg", "jpg"])
if upload_file:
    st.image(upload_file, width = 200, caption="Uploaded Image")
submit_button = st.button("Click to generate analysis")

if submit_button:
    if upload_file is not None:
        # Image processing
        image_upload = upload_file.getvalue()

        # Encoding image to base64
        encoded_image = base64.b64encode(image_upload).decode('utf-8')
        image_parts = [
            {
                "mime_type": "image/jpeg",  # Use appropriate mime_type
                "data": encoded_image
            }
        ]
        prompt_parts = [
            image_parts[0],
            system_prompt
        ]

        # generating response
        st.title("🧾 Here is the analysis based on the image")
        response = model.generate_content(prompt_parts)
        st.write(response.text) 
    else:
        st.warning("Please upload an image.")