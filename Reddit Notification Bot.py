import praw
import time

# The keywords or phrases that the bot looks for.
# Just follow the same format as below. Add more or remove some where necessary.
KEYWORDS = ['keyword1', 'keyword2', 'keyphrases work also', 'etc...']

# You can have 1 subreddit or multiple. If you have multiple, separate them with + symbols like I have done in the example
SUBREDDITS = 'subreddit1+subreddit2+subreddit3+etc...'

# Enter your username.
USERNAME = ''

# The subject of the message that the bot sends you.
MESSAGE_SUBJECT = 'Found new post'

#The body of the message that the bot sends you.
MESSAGE_BODY = 'Link to post: '

reddit = praw.Reddit( # Enter the credentials for your bot here. https://i.imgur.com/7MpgEgL.png
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