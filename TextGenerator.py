from NodeList import NodeList
from random import sample


# Generates up to len words of text using the given node_list
# Stops if there are no more connections that can be followed
def generate_text(text, length=100, node_length=2):
    node_list = NodeList(text, node_length)
    current_node = sample(node_list)
    generated_text = []
    for i in range(node_length):
        if i == length:
            break
        generated_text.append(current_node.words[i])
    for i in range(length - node_length):
        current_node = current_node.next_node()
        generated_text.append(current_node.words[node_length-1])
    return generated_text

try:
    with open("text.txt") as my_file:
        data = my_file.read()
    print(data)
except FileNotFoundError:
    print("Sorry! File was not found")


