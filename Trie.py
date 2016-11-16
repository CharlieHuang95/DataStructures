class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.links = {}
        self.is_end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        temp = self.root
        for letter in word:
            if letter in temp.links:
                temp = temp.links[letter]
            else:
                temp.links[letter] = TrieNode()
                temp = temp.links[letter]
        temp.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        temp = self.root
        for letter in word:
            if letter in temp.links:
                temp = temp.links[letter]
            else: return False
        if temp.is_end: return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        temp = self.root
        for letter in prefix:
            if letter in temp.links:
                temp = temp.links[letter]
            else: return False
        return True
