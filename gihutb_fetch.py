from utils import *
from repo_download import download_repo
from rich.console import Console
console=Console()

data={"type":"all","sort":"full-name","direction":"asc"}
username=""
password=""
repo_selected=""
repo_url="https://github.com/AK3847/Flow-Field"
destination_folder=repo_path

# function to fetch a GITHUB repository using URL or Username & Repository name via GitHub Access token
def fetch_github_repo():
    console.print("Give GitHub Access Token",style="#5272F2")
    github_token=pwinput.pwinput(prompt='token: ' ,mask='*')
    os.environ['GITHUB_TOKEN'] = github_token
    g = Github(os.getenv('GITHUB_TOKEN'))
    console.print("How do you want to find the repository?",style="#5272F2")
    console.print("1. Using Username and Repository Name\n2. Using Repository URL",style="#5272F2")
    choice=int(input())
    #if user selects to give Username and Repository directly
    if(choice==1):
        console.print("Give username:",style="#5272F2")    
        username=input()
        console.print("Give Repository Name:",style="#5272F2")    
        repo_name = input()
    #if user gives repository URL we parse the Repository and username from it
    else:
        console.print("Give Repository URL:",style="#5272F2")
        url=input()    
        gitpattern=r'^https?://github\.com/([^/]+)/([^/]+)\.git$' #regular expression to extract repository and user name from URL
        match=re.match(gitpattern,url)
        if match:
            username=match.group(1)
            repo_name=match.group(2)
        else:
            console.print("Invalid URL!",style="#CF0A0A")
            return False
    repo_name=f"{username}/{repo_name}"
    download_repo(g,repo_name,destination_folder,allowed_extensions) #calling this function to download the repo
    return True
