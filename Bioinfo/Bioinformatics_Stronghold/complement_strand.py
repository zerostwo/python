def complement_strand(string):
    rules = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return "".join(rules[i] for i in string[::-1])
