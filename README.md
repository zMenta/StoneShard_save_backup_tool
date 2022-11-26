# StoneShard_save_backup_tool
 A tool to create backups and load them.

### Requirements
   1 - Have Python installed in your machine.

   2 - Install Python 'keyboard' module.

   Note: You can install the keyboard module via pip. Open your terminal / command prompt and type:

         pip install keyboard

  After these steps you have everything setup to use the tool.


## Setup and Usage
  Configure the program by opening the "config.json" file.
  
  In this file you will find the following fields:
   

### 1. save_backup_directory
 >- The directory you want the backup to be saved.
 
 
 
### 2. stoneShard_save_directory
 > -The stoneshard save /exitsave_1 path.
 > 
 >**-Note that the character_# can change depending on how many characters you have. Choose the path for the character you are playing/want to make the backup upon "save and exit".**

### 3. backup_key
 > -Shortcut to backup save.
 > -Default key: F5

### 4. insert_save_key
 > -Shortcut to apply saved backup.
 > -Default key: F8

### 5. exit_key
 > -Shortcut to exit executing the program.
 > -Default key: F9
    
## How to Use

   Execute run.py file. A terminal windown will open, after this everything is working as long you keep the run.py open.
   
   Use the shortcuts to save, apply the backup in the game or exit the terminal.
   You can check the text logs in the terminal to know what is happeing.

  
   If you want you can run the files backupSave.py and insertSave.py manually.

   **Note: The program does a backup of the save when you exit to the menu to the specified character. It WON'T backup other saves.**
