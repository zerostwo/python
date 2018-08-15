def count_DNA(string):
    c = {"A":0, "T":0, "C":0, "G":0}
    for i in string:
        if i == "A":
            c["A"] += 1
        elif i == "T":
            c["T"] += 1
        elif i == "C":
            c["C"] += 1
        elif i == "G":
            c["G"] += 1
    return c
