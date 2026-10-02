from openai import OpenAI

from .config import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)


def generate_summary(document_text: str) -> str:

    prompt = f"""
You are an expert document analyst.

Analyze the following document and return the result in Markdown.

Use exactly this structure:

# Executive Summary

Write a concise executive summary.

# Key Points

- Point 1
- Point 2
- Point 3

# Important Facts

- Fact 1
- Fact 2
- Fact 3

# Conclusion

Write a concise conclusion.

Do not return JSON.

Do not use code blocks.

Return only Markdown.

DOCUMENT:

{document_text}
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text