# Setup instructions
*Instructions are for Windows. I've never done this on any other OS so I cannot help, sorry.*

- Download Python 3.6 from the Python website here - https://www.python.org/downloads/

- When installing, make sure you select "add python to PATH environment" or whatever that box is. I can't remember the exact wording, but it is something along those lines. You can just spam click "next" after checking that box.

- After it is completed, open your command prompt and type in "pip install praw", and let it do its thing. Once it is installed you can close the command prompt. 

- Download this program by clicking on the green "Clone or Download" button, followed by "Download ZIP". After it downloads, extract the "Reddit Notification Bot.py" file anywhere you like. 

- Open your start menu and type "IDLE", and open the program that is called "IDLE (Python 3.6 32-bit)". It might also be 64-bit instead of 32-bit. 

- When the window opens, go to *File > Open* and select the file that you just extracted.

- Next, to create a bot account on Reddit, create a new Reddit account like you normally would. After it is created, go to *preferences > apps > create new app*. Make sure you select "script". Call the bot whatever you like, and in the "redirect uri" box, enter "http://localhost:8080". Then click create.

- Go back to IDLE and follow the instructions that I commented. (Everything with a hash symbol. The text should be red.)

- After you entered in all of the credentials for your bot and then press F5 to save and run the program.

If you cannot get the bot set up using these instructions or the bot crashes with an error message, head over to https://www.reddit.com/r/redditdev and make a text post there. Make sure you link this github page so that we can help you quicker and let us know what the problem is. 
