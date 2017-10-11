from Node import Node
from nltk import word_tokenize
from collections import deque


class NodeList(object):
    def __init__(self, text, node_length=2):
        self.length = 0
        self.nodes = []
        self.node_length = node_length

        self.process_text(text)

    # Returns the index of the node holding words if found, -1 otherwise
    def contains(self, words):
        if len(words) != self.node_length:
            return -1
        for i in range(self.length):
            equal = True
            for j in range(self.node_length):
                if words[j] != self.nodes[i].words[j]:
                    equal = False
                    break
            if equal:
                return i
        return -1

    # Updates nodes with the text provided in word_list
    def process_list(self, word_list):
        if len(word_list) < self.node_length:
            return []
        init_list = []
        for i in range(self.node_length):
            init_list.append(word_list[i])

        index = self.contains(init_list)
        if index == -1:
            current_node = Node(init_list)
            self.append_node(current_node)
        else:
            current_node = self.nodes[index]

        # Runtime is probably the same as with a list since I have to convert this back into list anyway
        w = deque(init_list)

        for i in range(self.node_length, len(word_list)):
            w.append(word_list[i])
            w.popleft()

            index = self.contains(list(w))
            if index == -1:
                new_node = current_node.add_words(list(w))
                self.append_node(new_node)
                current_node = new_node
            else:
                new_node = current_node.add_node(self.nodes[index])
                if new_node is None:
                    current_node = self.nodes[index]
                else:
                    current_node = new_node

    # Updates nodes with the provided raw text
    def process_text(self, text):
        self.process_list(word_tokenize(text))

    def get(self, index):
        if index >= self.length:
            return None
        return self.nodes[index]

    def print_nodes(self):
        for i in range(self.length):
            self.nodes[i].print_full()

    def append_node(self, node):
        self.nodes.append(node)
        self.length += 1
