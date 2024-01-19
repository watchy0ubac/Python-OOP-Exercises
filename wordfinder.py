"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """
    def __init__(self, path):
        f = open(path, 'r')
        self.word_list = self.read(f)
        print(f"Your files includes {len(self.word_list)} words")
        f.close()
        
    def read(self, f):
        return [word.strip() for word in f]
    
    def random(self):
        return random.choice(self.word_list)
    
    def special_word_finder(self):
        self.new_word = self.random()
        while self.new_word == '' or self.new_word[0] == '#':
            self.new_word = self.random()
        
        return self.new_word
    