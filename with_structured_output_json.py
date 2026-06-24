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
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}


structured_model = model.with_structured_output(json_schema )

text = """
Bhoot Bangla, at least from its trailer, feels less like a fresh standalone horror-comedy and more like a spiritual successor to the classic Priyadarshan school of chaos-driven comedy. It evokes strong nostalgia similar to Bhool Bhulaiyaa with its tone and atmosphere. Humor feels organic and not forced.

However, CGI looks weak in some parts and some performances feel underwhelming. The film relies heavily on nostalgia which may become a weakness if it offers nothing new.
"""

result = structured_model.invoke(
    "Return output strictly as JSON with keys: key_themes, summary, sentiment, pros, cons. "
    "Analyze this text:\n" + text
)

print(result)
