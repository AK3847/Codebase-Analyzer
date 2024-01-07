from github import Github 
import json
import requests
import os
from repo_download import download_repo
from utils import *
data={"type":"all","sort":"full-name","direction":"asc"}
username=""
password=""
repo_selected=""
repo_url="https://github.com/AK3847/Flow-Field"
destination_folder = 'downloads'
def fetch_github_repo():
    github_token=input("Give github authorization token: ")
    username=input("Give username: ")
    repo_name = input("Give repo name: ")
    destination_folder = 'downloads'
    g = Github(github_token)
    repo_name=f"{username}/{repo_name}"
    download_repo(g,repo_name,destination_folder,allowed_extensions)
    return True
