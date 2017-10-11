from NodeList import NodeList
from random import randint
from nltk import word_tokenize


# Generates up to len words of text using the given node_list
# Stops if there are no more connections that can be followed
# Starts at the node containing the list start_words if it exists, random otherwise
# Starts at the node containing the string start_phrase if it exists, delimited by " " random otherwise
# If both start_words and start_phrase are specified, start_words takes precedence
#   unless it's invalid, in which case start_phrase is chosen
def generate_text(text, length=100, node_length=2, start_words=None, start_string=None):
    if length < 0:
        print("Error: Length of generated text must be non-negative")
        return []
    if node_length <= 0:
        print("Error: Number of words per node must be positive")
        return []

    node_list = NodeList(text, node_length)

    index = -1
    # First check start_words
    if start_words is not None:
        index = node_list.contains(start_words)
    # start_words was either not valid or not specified
    if index == -1:
        if start_string is not None:
            index = node_list.contains(word_tokenize(start_string))

    # One of start_words or start_phrase found an initial index
    if index == -1:
        current_node = node_list.get(randint(0, node_list.length - 1))
    else:
        current_node = node_list.get(index)

    generated_text = []
    for i in range(node_length):
        if i == length:
            break
        generated_text.append(current_node.words[i])
    for i in range(length - node_length):
        current_node = current_node.next_node()
        if current_node is None:
            break
        generated_text.append(current_node.words[node_length-1])
    return generated_text

try:
    with open("text.txt") as my_file:
        data = my_file.read()
    print(generate_text(data, node_length=3, start_string="went to the"))
except FileNotFoundError:
    print("Sorry! File was not found")
