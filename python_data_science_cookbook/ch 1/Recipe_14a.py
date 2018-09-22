from string import punctuation

def pipeline_wrapper(func):

    def to_lower(x):
        return x.lower()
    
    def remove_punc(x):
        for p in punctuation:
            x = x.replace(p,'')
        return x
        
    def wrapper(*args,**kwargs):
        x = to_lower(*args,**kwargs)
        x = remove_punc(x)
        return func(x)
    return wrapper
        
@pipeline_wrapper        
def tokenize_whitespace(inText):
    return inText.split()

s = "string. With. Punctuation?"    
print tokenize_whitespace(s)
