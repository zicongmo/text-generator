from random import randint


class Node(object):
    # Number of words stored per node
    length = 0

    # words: list of the words that are in the node
    # next_nodes: list of all the nodes that the current node can lead to
    # next_frequency: list of the number of times transitioned from current to next node
    # num_connected: number of different nodes connected to current = len(next_nodes)
    # total_frequency: sum of all numbers in next_frequency
    def __init__(self, word_list):
        self.length = len(word_list)

        self.words = word_list
        self.next_nodes = []
        self.next_frequency = []
        self.num_connected = 0
        self.total_frequency = 0

        self.print_words()

    # Returns true if the words in self and other are the same
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        for i in range(len(self.words)):
            if self.words[i] != other.words[i]:
                return False
        return True

    # Prints up to num words in node on one line separated by spaces, followed by newline
    # Stops if num > Node.length
    def print_words(self, num=10):
        for i in range(len(self.words)):
            if i == num:
                break
            print(self.words[i], end=" ")
        print()

    # Prints all words in node in addition to all words in attached nodes and frequencies
    def print_full(self):
        print("Words in Node")
        self.print_words()
        print("Connections:")
        for i in range(self.num_connected):
            for j in range(len(self.next_nodes[i].words)):
                print(self.next_nodes[i].words[j], end=" ")
            print(self.next_frequency[i])

    # Adds the input node to the current node's list of connections
    # Returns the new node if a new connection was created, None if the node already existed
    def add_node(self, n):
        # Search list of nodes to see if node already exists
        for i in range(self.num_connected):
            if n == self.next_nodes[i]:
                # Increment the frequency of this particular node and total frequency
                self.next_frequency[i] += 1
                self.total_frequency += 1
                return None
        self.next_nodes.append(n)
        self.next_frequency.append(1)
        self.num_connected += 1
        self.total_frequency += 1
        return n

    # Adds word_list as if it were a node containing those words
    # Returns the new node if a new node was created, None otherwise
    def add_words(self, word_list):
        # Search list of nodes to see if these words are already in an attached node
        for i in range(self.num_connected):
            if self.next_nodes[i].words == word_list:
                # Increment the frequency of this particular node
                self.next_frequency[i] += 1
                self.total_frequency += 1
                return None
        # This series of words hasn't come up yet, create a new Node and connect it
        print("Creating new node:")
        new_node = Node(word_list)
        self.next_nodes.append(new_node)
        self.next_frequency.append(1)
        self.num_connected += 1
        self.total_frequency += 1
        return new_node

    # Returns the next node to use based on the relative frequencies in next_frequency
    def next_node(self):
        if self.total_frequency == 0:
            return None
        r = randint(1, self.total_frequency)
        total = 0
        # Keep adding frequencies until they exceed the random number
        for i in range(self.num_connected):
            total += self.next_frequency[i]
            if total >= r:
                return self.next_nodes[i]
