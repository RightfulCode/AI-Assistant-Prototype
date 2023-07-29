# AI-Assistant-Prototype
Just a personal passion project

"Assistant.py" is the main file to be run, it takes in all the inputs and then requests the output from either "Utility.py" or "Ai.py" depending on what the input is.

The file "Ai.py" contains the code for training the assistant on the database provided by "Chatterbot", the inputs that are more general based like "How are you?","Hello" and other normal conversationas are handled by this file.

The inputs that ask for a specific task to be done like, "open something", "do this" etc are handled by "Utility.py".

The "show.py" is used to handle a the "google_search" function in the "Utility.py" module, more specifically, it displays the results of the search.
