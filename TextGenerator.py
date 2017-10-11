from Node import Node
from random import sample


# Generates up to len words of text using the given node list
# Stops if there are no more connections that can be followed
def generate_text(node_list, length=100):
    current_node = sample(node_list)
    generated_text = []
    for i in range(Node.length):
        if i == length:
            break
        generated_text.append(current_node.words[i])
    for i in range(length - Node.length):
        current_node = current_node.next_node()
        generated_text.append(current_node.words[Node.length-1])
    return generated_text

try:
    with open("text.txt") as my_file:
        data = my_file.read()
    print(data)
except FileNotFoundError:
    print("Sorry! File was not found")
