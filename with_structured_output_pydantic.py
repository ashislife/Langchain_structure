# Showing Error Pandamic not support HuggingFace (Hugging Face not able to structure to convert well formate )

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict, Annotated,Literal,Optional
from pydantic import BaseModel ,Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5.2",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# schema
class Review(BaseModel):
    
    key_themes:list[str]=Field(description="A list of key themes discussed in the review")
    summary:str=Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg", "neutral"]=Field(description="Return the sentiment of the review either positive , negative or neutral")
    pros:Optional[list[str]]=Field(default=None,description="A list of positive aspects mentioned in the review")
    cons:Optional[list[str]]=Field(default=None,description="A list of negative aspects mentioned in the review")


structured_model = model.with_structured_output(Review)

text = """
Bhoot Bangla, at least from its trailer, feels less like a fresh standalone horror-comedy and more like a spiritual successor to the classic Priyadarshan school of chaos-driven comedy. It evokes strong nostalgia similar to Bhool Bhulaiyaa with its tone and atmosphere. Humor feels organic and not forced.

However, CGI looks weak in some parts and some performances feel underwhelming. The film relies heavily on nostalgia which may become a weakness if it offers nothing new.
"""

result = structured_model.invoke(
    "Return output strictly as JSON with keys: key_themes, summary, sentiment, pros, cons. "
    "Analyze this text:\n" + text
)

print(result.pros)
