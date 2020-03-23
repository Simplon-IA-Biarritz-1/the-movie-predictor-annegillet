import os
import csv

class TSV:

    def __init__(self, file_path):
        # TODO : check if the file exists with th exists function
        self.fh = open(file_path, 'rt',  encoding = 'utf-8') #fh = file handler
        self.header = self.fh.readline() # TODO what if there is no header in the file ?

    def read_seq(self, number_of_lines = 100):
        lines = []
        counter = 0
        current_line = self.fh.readline()

        while (current_line) and (counter < number_of_lines):
            lines.append(current_line)
            counter += 1
            current_line = self.fh.readline()

        if len(lines) == 0:
            return None

        lines.insert(0, self.header)
        #print(lines)
        #exit()
        lines_as_dict = csv.DictReader(lines, delimiter = '\t', quoting = csv.QUOTE_NONE)

        return lines_as_dict
