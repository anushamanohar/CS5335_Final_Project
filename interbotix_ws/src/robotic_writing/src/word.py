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

    def pad_string(self, s):
        if len(s) < 7:
            spaces_needed = 7 - len(s)
            front_spaces = spaces_needed // 2 + (spaces_needed % 2)
            return "_" * front_spaces + s
        else:
            return s

    def write_word(self, word):
        print(word)
        word = self.pad_string(word)
        y_offset = -0.09 #-0.09 -0.065
        z_offset = 0.4
        last = False
        limit = min(7, len(word))
        last_y = -y_offset
        for i in range(limit):
            if word[i] == " ":
                y_offset = y_offset + 0.03 #y_offset+= 0.018
                continue
            if word[i] == "_":
                y_offset = -last_y + 0.025
                continue
            if i == len(word)-1:
                last = True
            last_y = self.writer_obj.write(word[i], y_offset, z_offset, last)
            y_offset = -last_y + 0.03

if __name__ == "__main__":
    obj = wordWriter()
    word = obj.get_word()
    print("word", word)
    obj.write_word(word)

