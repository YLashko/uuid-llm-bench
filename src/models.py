from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate


class TestResponse(BaseModel):
    new_random_uuid: str


prompt = PromptTemplate.from_template(
    "You are a random UUID generator. Your task is to generate a random UUID that is not contained in the sequence below: {uuids}." \
    "Make sure the pattern is not recognizable and the UUIDs are truly random. Make sure that you are adding a valid UUID-v4."
)
