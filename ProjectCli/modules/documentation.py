from ollama import ChatResponse, chat


class documentation:
    def __init__(self) -> None:
        pass

    def generateMd(self, sysPrompt, providedModel, instructions: str) -> str:
        response: ChatResponse = chat(
            model=providedModel,
            messages=[
                {
                    "role": "system",
                    "content": sysPrompt,
                },
                {
                    "role": "user",
                    "content": instructions,
                },
            ],
            options={"temperature": 1},
        )

        return response["message"]["content"]

    def generatePrompt(self, args) -> str:
        return """You will give the user a markdown formatted **general** documentation based on user input. The user will give you instructions another LLM provided and it's your task to documentate everything
-- general information --
- Once the user sends in the information, you will parse it to general information for a programming language/framwork. For example the user would send a assignment about learning Python, creating a timer script. Its your task to explain basic syntax on what the project needs, frameworks if needed, and how to run scripts
- This documentation is meant for users that would like to learn a new skill. Give general documentation with sources however **dont spoil the project itself nor any context from the project**. Explain general information what the user could find online without defining the project itself
- When generating the markdown file always include the following things; header (allowed to give a general scope of what the user will learn), basic syntax and/or basic guide on framework/package if existant, compile guide, installation guide, extra (open) resources, conclusion
- Do NOT use markdown blocks as your response will immediately be injected into a .MD file upon completion.
- When providing documentation, please provide **general** examples using code blocks
- Provide advanced and professional documentation like regular apps would do

The user will give you a markdown file, generate the markdown based on instructions above.
"""
