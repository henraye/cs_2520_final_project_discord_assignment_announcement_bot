from openai import OpenAI

#Add your own OpenAI key to use
api_key = "REDACTED"
client = OpenAI(api_key=api_key)

def get_response(lowered: str) -> str:
    assignment_description = (
        "I will be providing a description of an assignment. \n"
        "Please generate and format a discord announcement about when the assignment is due. \n"
        "Respond with an announcement that includes: the due date, assignment title, and provide tips. \n"
        "----------------------- \n"
        + lowered
    )
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": assignment_description}
        ]
    )
    return completion.choices[0].message.content