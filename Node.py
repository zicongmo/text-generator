class Node(object):
    # words: list of the words that are in the node
    # next_nodes: list of all the nodes that the current node can lead to
    # next_frequency: list of the number of times transitioned from current to next node
    # num_connected: number of different nodes connected to current = len(next_nodes)
    # total_frequency: sum of all numbers in next_frequency
    def __init__(self, word_list):
        self.words = word_list
        self.next_nodes = []
        self.next_frequency = []
        self.num_connected = 0
        self.total_frequency = 0

    # Returns true if the words in self and other are the same
    def __eq__(self, other):
        if other is not Node:
            return False
        for i in range(len(self.words)):
            if self.words[i] != other.words[i]:
                return False
        return True

    # Prints all words in node on one line separated by spaces, followed by newline
    def print_words(self):
        for i in range(len(self.words)):
            print(self.words[i], end=" ")
        print()

    # Prints all words in node in addition to all words in attached nodes and frequencies
    def print_full(self):
        self.print_words()
        for i in range(self.num_connected):
            for j in range(len(self.next_nodes[i])):
                print(self.next_nodes[i].words[j], end=" ")
            print(self.next_frequency[i])

    def add_node(self, n):
        for i in range(len(self.next_nodes)):
            if n == self.next_nodes[i]:
                self.next_frequency[i] += 1
                self.total_frequency += 1

lst = ["How", "are", "you", "today"]
node_1 = Node(lst)
node_1.print_words()
