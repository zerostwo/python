def transcribing_DNA(string):
    t = {"A":"A", "T":"U", "C":"C", "G":"G"}
    return "".join(t[i] for i in string)
