import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerationModel, Part, Content, ChatSession

project = "sample-gemini"
vertexai.init(project=project)

config = generative_models.GenerationConfig(
    temperature=0.4
)

model = GenerationModel(
    "gemini-pro",
    generation_config = config
)
chat = model.start_chat()