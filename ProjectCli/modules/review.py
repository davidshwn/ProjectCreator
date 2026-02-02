import os

from ollama import ChatResponse, chat


def RunCommand(command) -> str:
    """Runs a command on the HOST os"""
    """
  Args:
      command; Parsed command the LLM sends

  Returns:
      Output of command
  """
    try:
        return os.popen(command).read()
    except Exception as e:
        return f"Error occourd while processing: {e}"


class review:
    def __init__(self) -> None:
        pass

    def generateReview(self, providedModel, platform, markdown) -> str:
        # save the messageHistory while the model is reviewing the project
        messageHistory = [
            {
                "role": "system",
                "content": f"""You are going to review a project the user made based on a MD file.
- The user is currently on the platform; {platform}
- You will be allowed using tool calling to execute commands directly on the OS machine.
- You are NOT allowed to search up the web, do curl requests, modify files, or harm the device. The tool calling is intended purely for read only access
- Upon checking and validating the code generate your output (message content) in markdown formatted text as this will be directly injected into A markdown file
- do NOT use markdown blocks or anything else that would break the MD file in your output.
- review the user based on the score provided in the instuctions the user is going to provide. If not provided make up your own based on the instuctions
- When creating the markdown file always include the following things; Introduction, Review, Evaluation, Score, Rating, Comments, Extra information (if needed)
- when your evalution the project use the terminal (tool calling) to inspect files and read them.
- be VERY critical when reviewing the project. The user has to learn fropm this experience.
- before starting its adviced to do pwd and ls using tool calling as you can find the right place to review.


-- MARKDOWN FILE --
{markdown}
                """,
            },
            {
                "role": "user",
                "content": "Using tool calling and instructions provided in sys prompt, Complete the review.",
            },
        ]

        while True:
            # print("generate")
            response: ChatResponse = chat(
                model=providedModel,
                messages=messageHistory,
                tools=[RunCommand],
            )
            # print("Content: ", response.message.content)
            if response.message.tool_calls:
                print("attempted tool calling")
                for tool in response.message.tool_calls:
                    try:
                        print("-- TOOL CALLING RAN --")
                        print(
                            "- The LLM is currently running tests on your computer in order to generate a review -"
                        )

                        print(f"Command; {tool.function.arguments}")
                        result = RunCommand(**tool.function.arguments)
                        print(f"Result: {result}")
                        messageHistory.append(
                            {
                                "role": "tool",
                                "tool_name": tool.function.name,
                                "content": str(result),
                            }
                        )
                        print("-- END OF TOOL CALL --")
                    except Exception as e:
                        print("-- TOOL CALLING ERROR --")
                        print("- Error occourd while using tool calling -")

                        print(f"Result: {e}")
                        messageHistory.append(
                            {
                                "role": "tool",
                                "tool_name": tool.function.name,
                                "content": str(e),
                            }
                        )
                        print("-- END OF TOOL ERROR --")

            else:
                return response["message"]["content"]
