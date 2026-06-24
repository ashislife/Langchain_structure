# from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
# from dotenv import load_dotenv
# from typing import TypedDict

# load_dotenv()

# llm=HuggingFaceEndpoint(
#     repo_id="zai-org/GLM-5.2",
#     task="text-generation"   
# )
# model=ChatHuggingFace(llm=llm)

# # schema
# class Review(TypedDict):
#     summery: str
#     sentiment: str

# structured_model=model.with_structured_output(Review)

# result=structured_model.invoke("Actually, this (Bhoot Bangla) should be the Bhool Bhoolaiya-2 successor series and not the Kartik Aryan one. The trailer feels nostalgic in the sense that the setting, tone, tenor, and atmosphere, feels like Bhool Bhoolaiyya. Only that the role of the characters have been tweaked somewhat")

# print(result)



# ---------------------------------------------<>----------------------------------------------------------------

# Guide the Datatype of the output using TypedDict(using Annotated) 

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5.2",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "A list of key themes discussed in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "positive / negative / neutral"]
    pros: Annotated[list[str], "A list of positive aspects mentioned in the review"]
    cons: Annotated[list[str], "A list of negative aspects mentioned in the review"]

structured_model = model.with_structured_output(Review)

text = """
Bhoot Bangla, at least from its trailer, feels less like a fresh standalone horror-comedy and more like a spiritual successor to the classic Priyadarshan school of chaos-driven comedy. It evokes strong nostalgia similar to Bhool Bhulaiyaa with its tone and atmosphere. Humor feels organic and not forced.

However, CGI looks weak in some parts and some performances feel underwhelming. The film relies heavily on nostalgia which may become a weakness if it offers nothing new.
"""

result = structured_model.invoke(
    "Return output strictly as JSON with keys: key_themes, summary, sentiment, pros, cons. "
    "Analyze this text:\n" + text
)

print(result)

print(result.get("key_themes", []))
print(result.get("summary", ""))
print(result.get("sentiment", "unknown"))
print(result.get("pros", []))
print(result.get("cons", []))