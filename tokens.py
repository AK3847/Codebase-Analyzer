from utils import *
#user-defined function to convert length of a code file into tokens
def tokencount(content):
    encoding=tiktoken.get_encoding("cl100k_base")
    token_num=len(encoding.encode(content))
    if(token_num>1000):
        return False
    return True