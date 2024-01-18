from utils import *
from rich.console import Console
#user-defined function to download all the suggestions given by ChatGPT into "suggestions.txt" file
def download(text):
    console=Console()
    with open('suggestions.txt','w') as file:
        file.write(f'{text}')
    console.print("[not italic]All suggestions are downloaded to[/not italic] suggestions.txt",style="italic #F4BF96")