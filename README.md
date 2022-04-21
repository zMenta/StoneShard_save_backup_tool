# Stoneshard Exit Save Backup Tool

> **Original files and idea came from [zMenta](https://github.com/zMenta). I just changed the code to be more user friendly.**

## Requirements

- 28KB of storage

- At least version 3.X or better [Python](https://www.python.org/downloads/)

- During the Python install check all the boxes, especially installing Python to your path.

- Open a command prompt and upgrade pip.

$`python -m pip install -–upgrade pip`

## Installation

- Download or clone this [repo](https://github.com/ZeroOneZero/Stoneshard-Exit-Save-Backup-Tool.git)

- Unzip and/or CD into the repo

- Inside the directory, open a command prompt and verify the Python version

$`python --version`

> **Python 3.10.4** 

- Then install the requirements.txt

$`pip install -r requirements.txt`

## Info
- To run the script double click on the `run.py` file or run it from the command prompt.

$`python run.py`

- Upon startup the script creates two folders inside of your **%LOCALAPPDATA%/Stoneshard** save directory for **Character 1**

> **If you are using another character, make sure you go into `settings.py` and update the directory from character_1 to charater_x**

### **Backup your save folder before running this tool.**

- As long as you need the script to backup and restore you will need to run it and keep it running during the play.

## Usage

- Run the script

- Load up a save

- When you want to save your progress, press **ESC** and select **Save and Exit**

- This takes you back to the Main Menu.

### **DO NOT EXIT THE GAME**

> **The game, by default, erases the Exit Save upon exiting the game.**

- To backup the **Exit Save**, press `F5`

- `F5` triggers the script to backup the `exitsave_1` directory to `.exitsave_1` inside the same parent directory.

- Load back into the **Exit Save** via **Load** in the Main Menu.

- When you die, exit back to the main menu.

- To load the Exit Save press `F8`

- `F8` triggers the script to copy the **Exit Save** from `.exitsave_1` to the `exitsave_1` directory

- This allows you to save anywhere and anytime you want

# CHEERS
