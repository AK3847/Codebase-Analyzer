from utils import *
def download(text):
    with open('suggestions.txt','w') as file:
        file.write(f'{text}')
    print(f'All suggestions are downloaded to suggestions.txt!')