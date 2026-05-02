# import libraries
import argparse
import os

from .modules.documentation import documentation
from .modules.init import init
from .modules.review import review

# load the classes
initClass = init()
reviewClass = review()
documentationClass = documentation()

"""
Parser functions
"""


# init funtion
def initParser(args):
    # get total steps
    steps = 3
    currentStep = 1
    if args.documentation:
        steps += 3

    print("Creating project idea. This may take some time based on hardware.")
    # get systemPrompt
    print(f"Creating instructions system prompt. ({currentStep}/{steps})")
    systemPrompt: str = initClass.generatePrompt(args)

    currentStep += 1

    # Let the LLM generate a system prompt
    print(f"Generating Instructions (.MD) file. ({currentStep}/{steps})")
    instructions = initClass.generateMd(systemPrompt, args.model)

    currentStep += 1

    print(f"Creating instructions file. ({currentStep}/{steps})")
    with open(f"{os.path.abspath(os.getcwd())}/Instructions.md", "w") as f:
        f.write(instructions)

    # if documentation is enabled
    if args.documentation:
        print(f"Creating documentation system prompt. ({currentStep}/{steps})")
        systemPromptDoc: str = documentationClass.generatePrompt(args)

        currentStep += 1

        print(f"Generating documentation (.MD) file. ({currentStep}/{steps})")
        documentation = documentationClass.generateMd(
            systemPromptDoc, args.model, instructions
        )

        currentStep += 1

        # print(documentation)
        print(f"Creating documentation file. ({currentStep}/{steps})")
        with open(f"{os.path.abspath(os.getcwd())}/documentation.md", "w") as f:
            f.write(documentation)

        currentStep += 1

    print(
        f"-- COMPLETED --\nInstructions: {os.path.abspath(os.getcwd())}/Instructions.md"
    )
    return


def reviewParser(args):
    print("Generating review. This may take some time based on hardware.")
    print("⚠ THIS IS STILL A EARLY WIP, REVIEWING MAY NOT BE ACCURATE")
    print(
        "THE LLM MAY ACCESS FILES AND IF NOT HANDLED PROPERLY MODIFY THEM. YOU WILL BE NOTIFIED WHEN THE LLM IS DOING SUCH ACTIONS."
    )
    # get Instuctions
    print("Getting instructions. (1/3)")
    markdownFile: str = ""
    with open(f"{os.path.abspath(os.getcwd())}/Instructions.md", "r") as f:
        markdownFile = f.read()

    print("Generating Review (.MD) file. (2/3)")
    review = reviewClass.generateReview(
        providedModel=args.model, platform=args.platform, markdown=markdownFile
    )

    print("Creating Review MD file. (3/3)")
    with open(f"{os.path.abspath(os.getcwd())}/Review.md", "w") as f:
        f.write(review)

    print(f"-- COMPLETED --\nReview path: {os.path.abspath(os.getcwd())}/Review.md")
    return


"""
Main class
"""


def main():
    # create the parser and subparser
    parser = argparse.ArgumentParser(
        description="Use LLM's to create project ideas. Powered by ollama!"
    )
    subparsers = parser.add_subparsers(required=True)

    # init parser
    parser_init = subparsers.add_parser(
        "init", help="Creates a new project using LLM's"
    )
    parser_init.add_argument(
        "-m",
        "--model",
        help="Defines the ollama model. [Default; ministral-3]",
        default="ministral-3",
        required=False,
        type=str,
    )
    parser_init.add_argument(
        "-l",
        "--language",
        help="Defines which programming language you want to create the project in. This will be send to the LLM [default: Any]",
        required=False,
        default="Any",
        type=str,
    )
    parser_init.add_argument(
        "-f",
        "--framework",
        help="Defines a framework if prefered. [default; Not specified]",
        required=False,
        default="Not specified",
        type=str,
    )
    parser_init.add_argument(
        "-e",
        "--packages",
        help="Defines if external packages are allowed",
        required=False,
        default=True,
        type=bool,
    )
    parser_init.add_argument(
        "-d",
        "--difficulty",
        help="Set your difficulty to the LLM [Default; Beginner]",
        default="Beginner",
        required=False,
    )
    parser_init.add_argument(
        "-t",
        "--time",
        help="Set the estimated time you want to work on the project. [Default; 1 Hour]",
        default="1 Hour",
        type=str,
    )
    parser_init.add_argument(
        "-p",
        "--project",
        help="Set the type of project. (For example; CLI-app, Website, Etc) [Default; Any]",
        default="Any",
        type=str,
    )
    parser_init.add_argument(
        "-c",
        "--custom",
        help="Give the llm custom instructions if needed. [Default; None]",
        default="none",
        type=str,
    )
    parser_init.add_argument(
        "--documentation",
        help="Adds a documentation file to the project, useful if the user wants general documentation. [Default; True]",
        default=True,
        type=bool,
    )
    parser_init.set_defaults(func=initParser)

    # review parser
    parser_review = subparsers.add_parser(
        "review", help="Reviews project assignment [REQUIRES 'Instructions.md' FILE]"
    )

    parser_review.add_argument(
        "-m",
        "--model",
        help="Defines the ollama model. [Default; ministral-3]",
        default="ministral-3",
        required=False,
        type=str,
    )

    parser_review.add_argument(
        "-p",
        "--platform",
        help="Defines the platform the user is on. [Default; Ubuntu]",
        default="Ubuntu",
        required=False,
        type=str,
    )
    parser_review.set_defaults(func=reviewParser)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
