#!/usr/bin/env python3

from write import Writer


class wordWriter:
    def __init__(self):
        self.writer_obj = Writer()

    def write_word(self, word):
        y_offset = -0.09 #-0.12 - 0.062    -0.085
        z_offset = 0.4
        last = False
        for i in range(len(word)):
            if word[i] == " ":
                y_offset += 0.018
                continue
            if i == len(word)-1:
                last = True
            last_y = self.writer_obj.write(word[i], y_offset, z_offset, last)
            print("last y:", last_y)
            y_offset = -last_y + 0.03
            #if i < len(word)//2:
            #    z_offset += 0.03
            #else:
            #    z_offset -= 0.03


if __name__ == "__main__":
    word = "aaaaaa"
    obj = wordWriter()
    obj.write_word(word)

