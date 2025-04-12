#!/usr/bin/env python3

from write import Writer
from detector import ASLDetector

# The class wordWriter takes in a word and sends each letter to Writer class.
class wordWriter:
    def __init__(self):
        self.writer_obj = Writer()
        self.detector = ASLDetector()

    def get_word(self):
        text = self.detector.detect_asl()
        return text

    def write_word(self, word):
        y_offset = -0.05 #-0.09 -0.065
        z_offset = 0.4
        last = False
        for i in range(len(word)):
            if word[i] == " ":
                y_offset = -last_y + 0.02 #y_offset+= 0.018
                continue
            if i == len(word)-1:
                last = True
            last_y = self.writer_obj.write(word[i], y_offset, z_offset, last)
            print("last y:", last_y)
            y_offset = -last_y + 0.03

if __name__ == "__main__":
    obj = wordWriter()
    #word = obj.get_word()
    word = "ZHI"
    print("word", word)
    obj.write_word(word)

