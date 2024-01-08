# Tool made by Abdul-Kadir ;)
# Github - https://github.com/AK3847

from utils import *
from gihutb_fetch import fetch_github_repo
from analyze_codebase import analyze_codebase
from rich.console import Console
codebase_path=repo_path

def github_Repository():
    if(fetch_github_repo()):
        console.print("Repository Downloaded Succesfully!!\n",style="Bold #42855B")
        console.print("Now sending files to LLM for analyzing....",style="#5272F2")
    else:
        console.print("Repository Not Downloaded, Please try again.\n",style="#CF0A0A")
        return
    console.print("Give your Eden AI API Key: ",style="#5272F2")
    apikey=input()
    analyze_codebase(codebase_path,apikey)
    

def start():
    console.print(codebase_ASCII_ART,style="#5272F2",justify="left")
    github_Repository()


if __name__=='__main__':
    console=Console()
    start()