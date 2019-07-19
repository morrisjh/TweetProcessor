##A simple python program which can be used to process twitter data prior to analysis. It will return the text of all the tweets and write them to a new file.

filename = 'tweet.txt'

try:
    with open(filename) as file_object:
        text = file_object.read()
except FileNotFoundError:
    message = "The file was not found."
    print(message)
else:
    for line in text.splitlines():
        if "full_text" in line:
            f = open("TweetsText.txt", "a+")
            f.write(line)
            print(line)
    print("Complete.")