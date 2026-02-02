# ProjectCreator
A easier way to create projects for educational purposes

> [!IMPORTANT]  
> This entire project is still being worked on and is on early development. Please report any issues you've saw! This app is currently tested on MacOS.

> [!NOTE]  
> Readme is still in early WIP. Changed may be made


## getting started
Make sure you have python installed. The currently supported/tested version is [python 3.11.9](https://www.python.org/downloads/release/python-3119/)
1. clone this repository and navigate to the folder.
2. run the command ``pip install .``

## usage
Using this CLI tool is really easy. If you're stuck somewhere just use ``projectcreator -h``
### creating a assignment
to create a assignment navigate to the folder of your choice and run ``projectcreator init``. For parameters you could add run ``projectcreator init -h``. Default params are shown as well. Upon finishing it would create a MD file on the folder you're working in.

### Reviewing a assignment
> [!CAUTION]
> Reviewing would allow the LLM to gain full access over your computer terminal. While im planning to update that soon; **use it at your own risk**

to review a assignment navigate to the folder you're working in and run ``projectcreator review``. For parameters you could add run ``projectcreator init -h``. Default params are shown as well.

ProjectCreator assumes upon reviewing the code you're running on linux. If you're on another os such as Windows run; ``projectcreator review -p windows``.
