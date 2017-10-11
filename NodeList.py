from Node import Node
from nltk import word_tokenize
from collections import deque


class NodeList(object):
    def __init__(self, text, node_length=2):
        self.length = 0
        self.nodes = []
        self.node_length = node_length

        self.process_text(text)

    # Updates nodes with the text provided in word_list
    def process_list(self, word_list):
        if len(word_list) < self.node_length:
            return []
        init_list=[]
        for i in range(self.node_length):
            init_list.append(word_list[i])

        # Runtime is probably the same as with a list since I have to convert this back into list anyway
        w = deque(init_list)
        current_node = Node(init_list)

        for i in range(self.node_length, len(word_list)):
            w.append(word_list[i])
            w.popleft()
            new_node = current_node.add_words(list(w))
            if new_node is not None:
                self.nodes.append(new_node)
                self.length += 1
                current_node = new_node

    # Updates nodes with the provided raw text
    def process_text(self, text):
        self.process_list(word_tokenize(text))
