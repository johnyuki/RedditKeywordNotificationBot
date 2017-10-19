import praw
import time

# The keywords or phrases that the bot looks for.
# Just follow the same format as below. Add or remove words/phrases as necessary.
# Keywords and phrases are NOT case sensitive. However it will match them literally, so make sure you spell them correctly.
KEYWORDS = ['keyword1', 'keyword2', 'keyphrases also work', 'etc...']

# You can have 1 subreddit or multiple. If you have multiple, separate them with + symbols like I have done in the example.
# Also, you do not need to include the "/r/" part, just the name of the subreddit as shown in the example.
SUBREDDITS = 'gifs+pics+videos+etc...'

# Enter your username. You do not need to include the "/u/" part, just the username like in the example
USERNAME = 'your_username'

# The subject of the message that the bot sends you.
MESSAGE_SUBJECT = 'Found new post'

#The body of the message that the bot sends you. #The bot will automatically attach the link to the post at the end of the message body.
MESSAGE_BODY = 'Link to post: '

reddit = praw.Reddit( # Enter the credentials for your bot here. Guide - https://i.imgur.com/7MpgEgL.png
    username = 'username', # The username of your bot
    password = 'password', # The password to your bots account
    client_id = 'client ID', # Your bots client ID
    client_secret = 'client secret', # Your bots client secret
    user_agent = 'Message Notification Bot, by /u/John_Yuki') # A short, unique description.

# Main program. Don't mess with anything below here unless you know what you're doing.
def send_message(submission, reddit):
    reddit.redditor(USERNAME).message(MESSAGE_SUBJECT, MESSAGE_BODY+submission.shortlink)
    print('Sent new message') # This line is for testing purposes. If you don't want it, you can completely remove this line.

def find_submissions(reddit):
    while True:
        start_time = time.time()
        for submission in reddit.subreddit(SUBREDDITS).stream.submissions():
            for keyword in KEYWORDS:
                if keyword in submission.title.lower() and submission.created_utc > start_time:
                    send_message(submission, reddit)
                    break

if __name__ == '__main__':
    find_submissions(reddit)
