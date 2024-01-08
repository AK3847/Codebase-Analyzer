from utils import *
from rich.console import Console
def download(text):
    console=Console()
    with open('suggestions.txt','w') as file:
        file.write(f'{text}')
    console.print("[not italic]All suggestions are downloaded to[/not italic] suggestions.txt",style="italic #F4BF96")