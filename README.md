# S5T
Super Simple Song Search (and) Sampling Tool

S5T is a program written in **Python**, utilising the `yt-dlp` and `ytmusicapi` libraries. 
S5T allows you to quickly and efficiently fetch **any Youtube Music search query** (song or album) or **URL** (also song or album / playlist), in lightweight 320K **MP3** format.
S5T ensures the downloaded audio contains the appropriate **metadata**, ensuring it is compatible with music players and other software.
S5T is a **<ins>terminal-based</ins>** program, and is available accross all operating systems (as long as Python + dependencies are installed; see `requirements.txt`).

# Universal Installation
## To get started, simply **clone this repository**.
If you are currently in a **terminal / command prompt**, type the following command:
```git clone https://github.com/OofySimpsonV3/S5T```
If ^this command returns an error, or if you don't have GIT installed, no worries! Simply follow these instructions:
1. Click the green `<> Code` button at the top of this repository's webpage.
2. Simply hit the `Download ZIP` button, to clone the repository as a compressed ZIP file.
3. Extract the freshly downloaded ZIP file by using your desired ZIP extracting software.
4. Navigate into the un-compressed folder.

## Ensure Python and dependencies are installed and up-to-date
Now that we have cloned the repository, we must ensure we have Python and the dependencies installed for S5T.

To install Python, simply [click here](https://www.python.org/downloads/) to navigate to the official Python downloads page. Please ensure you select the correct option for your operating system, and for the best results, please ensure you are downloading the latest version of Python.

*Please also ensure `pip` is installed when installing Python. This is the tool to download Python dependencies.*

Once Python is installed on your system, we can now ensure the appropriate dependencies / libraries are installed, to ensure the software functions correctly.

To install the dependencies, simply type the following command:

`pip install -U -r requirements.txt` ***OR*** `python -m pip install -U -r ./requirements.txt`

*Please note: if the `python` command doesn't exist after installation, please also try `py`, `python3`, or `py3`.*

This will download all the dependencies listen within the `requirements.txt` file.

*Alternatively*, you may also install the dependencies using the following command:

```pip install -U yt-dlp ytmusicapi```

# Running the software

Now we have the repository cloned, the interpreter (Python) installed as well as the dependencies, we may now test our software!

Ensuring your terminal session is still within the repository folder, we may run the main python file:
```python main.py```

This will return the command usage. You should see something like this: 

```
[user@archlinux ~/S5T]$ python main.py

Arguments:

--url <URL> (may require quotes)
Downloads Youtube media via a URL

--song "<QUERY>"
Searches and downloads the first song result in Youtube Music.

--album "<QUERY>"
Searches and downloads the first album result in Youtube Music.

--video "<QUERY>"
Searches and downloads the first video result in Youtube Music.

--help
Shows a list of commands.
```

Simply append the relevant arguments to your command. For example:

```python main.py --song "Ghost Town The Specials"```

The software uses an API which ensures the search feature is nice and flexible. This means the software (should) know which song you are wishing to download, dispite grammar or spelling.

For example, `python main.py --song "Gohst Town by Specials"` would download the same song as the previous example.

# Housekeeping
The software is now officially installed! However, going to the repository folder and typing `python main.py...` every time for a song or album can drastically affect the efficiency of the tool.

To ensure future use is **nice and simple**, we can assign the program to our own, custom command / alias!

## For Linux / UNIX systems
To create an alias in most Linux / *NIX systems, you would simply use the `alias` command.
Typing `alias getsong='python ~/Downloads/s5t/main.py'` will create an alias for the entire command and path, with the convenience of being just a single command, being `getsong` in this example.

Creating an alias is only temporary, however, and closing the terminal session will clear the alias from the memory.

To ensure the alias is available every time we enter our terminal session, we simply have to append the alias command to the end of the `.bashrc` file, located within the home (~) directory.

To do this is one easy command, simply enter:

```echo "alias getsong='python /home/user/Downloads/s5t/main.py'" >> ~/.bashrc```

This will ensure the alias is assigned each time a terminal session is opened.

*Please note: The shell RC file may differ between shell environments. E.g. The FreeBSD operating system natively uses the `.shrc` RC file, as this OS uses standard `sh` instead of `bash`.*

*If you wish to remove your alias, simply edit the RC file using your preferred text editor and simply remove the line which assigns the alias.*

## For Windows / Win32 systems

*WARNING: This process will require the Registry Editor and, therefore, will require Admin access.*

To set up a permenant alias in the Windows command prompt, it is just a tad more tricky.
Luckily, just like UNIX, these one-time steps will ensure a future ease of access, and can also be removed any time.

In Windows, the `doskey` command is used to create custom aliases named `macro`s.

To begin, we will need to create a Batch file which will store any custom aliases (hereby referred to as `macro`s).

Anywhere in your Windows home folder, create a file named `macros.bat`, ensuring the filepath is remembered, as it would be required quite shortly.

After creating our file, simply add the following command to the file:

```DOSKEY getsong=python C:/absolute/path/to/S5T/main.py $*```

After creating the file which declares our custom macro(s), we now need to ensure this code runs whenever a Command Prompt is opened.

To do this, we would require the **Registry Editor**.

Then, open the following register:

`HKEY_CURRENT_USER\Software\Microsoft\Command Processor`

Add a *String Value* named Autorun, and set the value to the path (absolute) of the `macros.bat` file.

You are now finished! Simply **reboot** your machine, open the Command Prompt and type in your custom macro!

For example: ```getsong --album "ELO - Eldorado"```

# Questions, Concerns or Issues
Should you experience any issues with this software, such as bugs, errors, inconveniences or deprecated code, please reach out via Github or my E-Mail address [mail@antonwilliams.me](mailto:mail@antonwilliams.me) so I may help out as much as possible!

Feel free to contribute to this project with any issues or pull requests.

# License
Go wild! :)
