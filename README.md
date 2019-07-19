# TweetProcessor
This is a simple program that returns the text of tweets and the handle of the twitter user who made that tweet from data downloaded from Twitter.

# How to use
First you will need some data. 

    1. Log in to a Twitter account that you control.
    2. Click "Profile and settings" (your profile's picture).
    3. Click "Settings and privacy".
    4. Click "Your Twitter data".
    5. Confirm your password.
    6. Click "Request data".
    7. Recieve an email from Twitter.
    8. Follow the link in the email.
    9. Download your data.
    10. Unzip the data.

Next you will want to find the "tweet.js" file in the unzipped folder of data that you downloaded from Twitter. Once you have found it save it as a .txt file named "tweet.txt" and place it in the TweetProcessor folder replacing the current "tweet.txt" file which is acting as a placeholder. 

If you open the "tweet.txt" (formerly "tweet.js") file you'll notice that it contains a large array of data that may not necessarily be useful to the user. By running TweetProcessor.py you will be able to gather the text of all the tweets in the data (labelled in the file as "full_text") and the handle(s) of the user(s) who tweeted them. This data will be printed in your terminal and saved to a new file called "TweetsText.txt".

# TweetProcessor.py
This simple piece of code will return all lines labelled "full_text" in the "tweet.txt" file. This includes the label "full_text", the handle of the Twitter user who made the tweet, and the text of the tweet. 

These lines will be printed in the terminal in which the code is being run and written to a new .txt file called "TweetsText.txt".

# tweet.txt
This is a placeholder file. After downloading data from a twitter account you should rename the "tweet.js" file as "tweet.txt" and save it here.
