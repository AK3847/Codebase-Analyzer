# Python-tool made by Abdul-Kadir ;)
# Github - https://github.com/AK3847
# A python-script to analyze your GitHub repository via ChatGPT LLM 
# for code improvements, bug fixes, security improvement etc.

from utils import *
from gihutb_fetch import fetch_github_repo
from analyze_codebase import analyze_codebase
from rich.console import Console
codebase_path=repo_path

#function imported from github_fetch.py
def github_Repository():
    if(fetch_github_repo()):
        console.print("Repository Downloaded Succesfully!!\n",style="Bold #42855B")
        console.print("Now sending files to LLM for analyzing....",style="#5272F2")
    else:
        console.print("Repository Not Downloaded, Please try again.\n",style="#CF0A0A")
        return
    console.print("Give your OpenAI API Key",style="#5272F2")
    apikey=pwinput.pwinput(prompt='API Key: ' ,mask='*')
    os.environ['API_KEY'] = apikey
    analyze_codebase(codebase_path)
#user-defined function to call the github_repository function and start the tool
def start():
    console.print(codebase_ASCII_ART,style="#5272F2",justify="left")
    github_Repository()


#main function
if __name__=='__main__':
    console=Console()
    start()