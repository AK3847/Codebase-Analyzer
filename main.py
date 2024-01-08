from utils import *
from gihutb_fetch import fetch_github_repo
# from suggestion_download import download
from analyze_codebase import analyze_codebase

codebase_path=repo_path

def github_Repository(apikey):
    print("API KEY verified!")
    fetch_github_repo()
    analyze_codebase(codebase_path,apikey)
    

def start():
    print("///////////////Welcome to CodeBase Analyzer////////////")
    apikey=input("Give your Eden AI API Key: ")
    # print(codebase_path)
    github_Repository(apikey)


if __name__=='__main__':
    start()