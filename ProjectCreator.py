'''
Init
'''

# import libraries
import argparse
from modules.init import init

# load the classes
initClass = init()


'''
Parser functions
'''
# init funtion
def initParser():
    
    pass


'''
Main class
'''
def main():
    # create the parser and subparser
    parser = argparse.ArgumentParser(description="Use LLM's to create project ideas. Powered by ollama!")
    subparsers = parser.add_subparsers(required=True)

    parser_init = subparsers.add_parser("init", help="Creates a new project using LLM's")
    parser_init.add_argument("-m", "--model", help="Defines the ollama model. [Default; ministral-3]", default="ministral-3", required=False, type=str)
    parser_init.add_argument("-l", "--language", help="Defines which programming language you want to create the project in. This will be send to the LLM", required=True, type=str)
    parser_init.add_argument("-d", "--difficulty", help="Set your difficulty to the LLM [Default; Beginner]", default="Beginner", required=False)
    parser_init.add_argument("-t", "--time", help="Set the estimated time you want to work on the project. [Default; 1 Hour]", default="1 Hour", type=str)
    parser_init.add_argument("-p", "--project", help="Set the type of project. (For example; CLI-app, Website, Etc) [Default; Any]", default="Any", type=str)
    parser_init.set_defaults(func=initParser)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()