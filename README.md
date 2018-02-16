# Windows setup instructions

1. Download Python 3.6 from the Python website here - https://www.python.org/downloads/

2. When installing, make sure you select "add python to PATH environment" or whatever that box is. I can't remember the exact wording, but it is something along those lines. You can just spam click "next" after checking that box.

3. After it is completed, open your command prompt and type in "pip install praw", and let it do its thing. Once it is installed you can close the command prompt. 

4. Download this program by clicking on the green "Clone or Download" button, followed by "Download ZIP". After it downloads, extract the "Reddit Notification Bot.py" file anywhere you like. 

5. Open your start menu and type "IDLE", and open the program that is called "IDLE (Python 3.6 32-bit)". It might also be 64-bit instead of 32-bit. 

6. When the window opens, go to *File > Open* and select the file that you just extracted.

7. Next, to create a bot account on Reddit, create a new Reddit account like you normally would. After it is created, go to *preferences > apps > create new app*. Make sure you select "script". Call the bot whatever you like, and in the "redirect uri" box, enter "http://localhost:8080". Then click create.

8. Go back to IDLE and follow the instructions that I commented. (Everything with a hash symbol. The text should be red.)

9. After you entered in all of the credentials for your bot and then press F5 to save and run the program.

If you cannot get the bot set up using these instructions or the bot crashes with an error message, head over to https://www.reddit.com/r/redditdev and make a text post there. Make sure you link this github page so that we can help you quicker and let us know what the problem is. 

# Linux setup instructions

1. Ensure Python 3 is installed by typing `python3` or `python --version` into a shell. If it isn't, then install it with `sudo yum install python3` (Red Hat / CentOS), `sudo pacman -S python3` (Arch), or `sudo apt-get install python3` (Debian / Ubuntu).

2. If PIP is not installed for Python 3 (check for `pip3`), run the following:

```
$ wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py
$ python3 ./get-pip.py
$ rm get-pip.py
```

3. Run `pip install praw`.

4. If `git` is not installed, install it just like Python. Run `git clone https://github.com/ashleyoconnor/RedditKeywordNotificationBot.git`, and `cd` into RedditKeywordNotificationBot.

5. Follow step 7 from above.

6. Open `Reddit Notification Bot.py` using `vim` and edit to contain the client/secret Reddit gave you.

7. Run `python3 Reddit\ Notification\ Bot.py`.

8. If you're in a headless environment over SSH, consider using a virtual shell such as `screen`, so the program doesn't terminate when the shell and connection do. Install it like above, run `screen`, and run the program as normal. Exit the screen session with `Ctrl+A D`.
