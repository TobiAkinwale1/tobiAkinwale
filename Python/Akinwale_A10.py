import re
import os


def motif(count):
    f = open("sequence.txt", "r")
    s = f.read()
    x = re.search(m, s)
    if x:
        print("Motif found")
    else:
        print("Motif not found")


m = input('Enter motif sequence here')
motif(count=input("Enter filename"))


# 2
def repeat_f(line):
    for i in range(len(line) - 5):
        if line[i:i + 6] == "ATATAT":
            return True


file = open("Test.txt")
lines = file.read().split("\n")
seq_start = False
found = 0
for line in lines:
    if len(line) == 0:
        break
    if seq_start:
        if line[0] == ">":
            seq_start = False
            continue
        else:
            if repeat_f(line):
                print('AT exists in here')
                found = 1
                break
    else:
        if line != "Testseq":
            continue
        else:
            seq_start = True
            continue
if found == 0:
    print("No AT repeats")
file.close()
