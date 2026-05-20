from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class ScriptReadTimeEstimatorInput(BaseModel):
    """Input schema for ScriptReadTimeEstimator."""

    script_text: str = Field(
        ...,
        description="The generated YouTube script text."
    )


class ScriptReadTimeEstimator(BaseTool):

    name: str = "Script Read Time Estimator"

    description: str = (
        "Calculates estimated narration time for a YouTube script "
        "based on 130 words per minute."
    )

    args_schema: Type[BaseModel] = ScriptReadTimeEstimatorInput

    def _run(self, script_text: str) -> str:

        word_count = len(script_text.split())

        estimated_time = round(word_count / 130, 2)

        return (
            f"Word Count: {word_count}\n"
            f"Estimated Read Time: {estimated_time} minutes"
        )