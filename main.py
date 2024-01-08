from utils import *
from gihutb_fetch import fetch_github_repo
from analyze_codebase import analyze_codebase

codebase_path=repo_path

def github_Repository():
    print("API KEY verified!")
    if(fetch_github_repo()):
        print("Repository Downloaded Succesfully!!\nNow sending files to LLM for analyzing.....")
    else:
        print("Repository Not Downloaded, Please try again.\n")
        return
    apikey=input("Give your Eden AI API Key: ")
    analyze_codebase(codebase_path,apikey)
    

def start():
    print("///////////////Welcome to CodeBase Analyzer////////////")
    github_Repository()


if __name__=='__main__':
    start()