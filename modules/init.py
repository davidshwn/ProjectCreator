from ollama import ChatResponse, chat


class init:
    def __init__(self) -> None:
        pass

    def generateMd(self, sysPrompt, providedModel) -> str:
        response: ChatResponse = chat(
            model=providedModel,
            messages=[
                {
                    "role": "system",
                    "content": sysPrompt,
                },
            ],
        )

        return response["message"]["content"]

    def generatePrompt(self, args) -> str:
        return f"""You will give the user a markdown formatted programming project they can work on.
-- Details --
Language: [[ {args.language} ]]
Framework: [[ {args.framework} ]]
External packages allowed: [[ {str(args.packages)} ]]
Difficulty: [[ {args.difficulty} ]]
Estimated Time the user want to spend on the project: [[ {args.time} ]]
Type of project: [[ {args.project} ]]
Custom instructions: [[ {args.custom} ]]

-- information --
- Align the project based on this information.
- This project is intended for users that want to practise their programming skills.
- When creating the markdown file always include the following things; header, instruction, final product, rules, general information provided by user (Details), Technical Requirements, and lastly the points (score)
- do NOT use markdown blocks as your response will immediately be injected into a .MD file upon completion.
- If the user did not provide a Programming Language (based on details) the assign the user one based on the project. Clearly define the language in the MD file
- If there is a framework (such as symfony) included (or a engine such as unity) or a library/package that requires a advanced instalation (based on difficulty), provide a installation guide in the MD file and/or a cheatsheet unless the assistant is unsure on how to set it up.
- Make the user decide on their own which packages they want to use unless explicitly specified in Custom instructions and/or General Details
- Do NOT provide any code structures or samples (unless required by previous instructions). Let the user figure it out on its own as this is intended to be a challenge
"""
