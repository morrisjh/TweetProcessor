##A simple python program which can be used to process twitter data prior to analysis. It will return the text of all the tweets and write them to a new file.

filename = 'tweet.txt'

try:
    with open(filename) as file_object:
        text = file_object.read() #Opens and reads the file "tweet.txt".
except FileNotFoundError:
    message = "The file was not found."
    print(message)
else:
    for line in text.splitlines():
        if "full_text" in line: #Finds all lines which contain the label "full_text".
            f = open("TweetsText.txt", "a+")
            f.write(line) #Writes all lines containing the label "full_text" to a new file entitled "TweetsText.txt".
            print(line) #Prints the lines containing the label "full_text" in the terminal.
    print("Complete.") #Tells the user that the program is complete.
