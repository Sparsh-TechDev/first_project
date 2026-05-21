from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

message = HumanMessage(
    content=[
        {"type": "text", "text": "Describe this image in detail"},
        {"type": "image_url", "image_url": {"url": "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d"}},
    ]
)

response = model.invoke([message])
print(response.content)

