import requests # type: ignore
from io import StringIO, BytesIO, FileIO
import json
import gdown # type: ignore
import streamlit as st

# response = requests.get(url='https://drive.google.com/uc?export=download&id=10SSqgquSRVlz_aQUGkF4Xhf6UG4vnyU2', stream=True)

# OPENAI_KEY = st.secrets['OPENAI_API_KEY']

# st.write(response.content)

# from openai import OpenAI

# client = OpenAI(api_key=OPENAI_KEY)

# stream = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": "Say this is a test"}],
#     stream=True,
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")

# st.write_stream(stream)


# response = requests.get(
#     url='https://www.googleapis.com/drive/v3/files/',
#     params={
#         'fileId': '1OnXq7tseyaFpb40gW7wm_t80c4SFVJj9'
#     }
# )

# print(response.content)

# t = BytesIO()

gdown.download(url='https://docs.google.com/document/d/12AcN1pAPCo5lxl19a1j3luDjX_-ZwgQm/edit?usp=drive_link&ouid=103951275346460084316&rtpof=true&sd=true', output='try.txt', fuzzy=True)

