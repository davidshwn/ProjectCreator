# ProjectCreator
A easier way to create projects to grow your skills.

> [!IMPORTANT]  
> This entire project is still being worked on and is on early development. Please report any issues you've saw! This app is currently tested on MacOS however will be tested later on other platforms

## Introduction
Do you sometimes also lack the creativity to create a project but you just want to build so you can grow your experience? So do I! This CLI app focusses on creating project ideas using LLM’s so you can expand your knowledge while you can focus on finding actual creativity for new projects!

## Features
> [!NOTE]  
> As the project is still in early development there may be some features missing and/or in development. 
- Creating assignments [WIP]
- Reviewing assignments [EARLY WIP]

## Getting started
To get started; Make sure you have python installed. The currently supported/tested version is [python 3.11.9](https://www.python.org/downloads/release/python-3119/).

The second requirement is to have [Ollama installed](https://ollama.com/) on your computer with [ministral-3 as model](https://ollama.com/library/ministral-3). (If you prefer another model you could always change models with the ``-m`` parameter. This will be described later!)

Once you have these 2 apps installed with the model run the following steps;
1. Clone this repository using the platfrom you're cloning it from.
2. Navigate to the folder you just cloned.
3. Open a terminal and run the following command ``pip install .`` (or ``pip3 install .``)

## Usage
Using this CLI tool is really easy. To get all parameters just use ``projectcreator [argument] -h``

## Examples
### Creating a assignment
to create a assignment navigate to the folder of your choice and run ``projectcreator init``. For parameters you could add run ``projectcreator init -h``. Default params are shown as well. Upon finishing it would create a MD file on the folder you're working in.

For example you could run the following command
```cmd
projectCreator init -l C -t 1h -d easy/learning
```
This will;
- Create a new project with the program language C
- Creates a estimated timeframe of 1 hour.
- Puts the difficulty on easy/learning


> [!IMPORTANT]  
> Currently only models coming from ollama are supported. I'm working on adding support for more providers.
You can as well change models if needed using;
```cmd
projectCreator init -l C -t 1h -d easy/learning -m gpt-oss
```
This would change the model to gpt-oss.

### Reviewing a assignment
> [!CAUTION]
> Reviewing would allow the LLM to gain full access over your computer terminal. While im planning to update that soon; **use it at your own risk**

> [!NOTE]  
> This feature is still heavily unstable and you shouldn't rely on this. While im working to improve this feature, the LLM may review your assignment incorrectly

to review a assignment navigate to the folder you're working in and run ``projectcreator review``. For parameters you could add run ``projectcreator init -h``. Default params are shown as well.

ProjectCreator assumes upon reviewing the code you're running on linux. If you're on another os such as Windows run; ``projectcreator review -p windows``.

## Issues and feedback
> [!NOTE]  
> WhoIsDavid may not allow the creation of accounts, consider going to the github mirror and create a issue there.
If you experience any issues or have any feedback feel free to create a issue on the service you're cloning it from!

## License
This project is released under the [Apache License 2.0](LICENSE)
