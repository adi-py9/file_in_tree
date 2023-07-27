#!/usr/bin/python3

from pathlib import Path
from termcolor import colored, cprint
import colorama
import operator
import os
import sys
import time

colorama.init()



class Tree():
    """docstring for Tree."""

    def __init__(self, showAll):
        self.currPath = Path(os.getcwd())
        self.showAll = showAll
        self.filesTraversed = 0
        self.popularFileDict = {}
        cprint((self.currPath.name), "blue")


    def print(self, indent = 4):
        allFiles = []
        for file in self.currPath.iterdir():
            if(file.is_dir()):
                if( not(file.name[0] == '.' and not self.showAll)):
                    spaces = ""
                    for i in range(indent-4):
                        if(i % 4 == 0):
                            spaces += '|'
                        else:
                            spaces += ' '

                    formatIndent = spaces + '\\' + '_' * 4

                    cprint(formatIndent, "white", end='')
                    cprint((file.name + '/'), "blue")

                    self.currPath = file;
                    self.print(indent + 4)
            elif( not(file.name[0] == '.' and not self.showAll)):
                ext = file.name.split('.')
                ext = ext[len(ext)-1]
                if(ext in self.popularFileDict):
                    self.popularFileDict[ext] += 1
                else:
                    self.popularFileDict[ext] = 1

                self.filesTraversed += 1
                allFiles.append(file.name)

        for file in allFiles:
            spaces = ""
            for i in range(indent-4):
                if(i % 4 == 0):
                    spaces += '|'
                else:
                    spaces += ' '

            formatIndent = spaces + '\\' + '__>'

            cprint(formatIndent, "white", end='')
            cprint(file, "green")


def main():
    showAll = False;
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "-a" or sys.argv[1] == "--all"):
            showAll = True
        elif(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
            print('''tree - v-0.0.1 (2020 Aug. 30)\n
Usage: tree [arguments] displays file structure.\n
Arguments:\n
-a  or  --all:    Include hidden files in tree visualization\n
-h  or  --help:   Print Help (this message) and exit''')
            sys.exit(1)
        else:
            print(f'''tree - v-0.0.1 (2020 Aug. 30)\n
Garbage after option argument: "{sys.argv[1]}"\n
More info with: "tree -h"''')
            sys.exit(1)

    tree = Tree(showAll)
    t0 = time.time()
    tree.print()
    totalTime = time.time() - t0

    popularFileType = max(tree.popularFileDict.items(), key=operator.itemgetter(1))[0];
    cprint(f"\nTraversed {tree.filesTraversed} file(s) in {round(totalTime, 2)} seconds", "cyan")
    cprint(f"This directory is mostly .{popularFileType} files", "cyan")


if __name__ == '__main__':
    main()
