import openai
import os
import json
import requests
from utils import *
from gihutb_fetch import fetch_github_repo
codebase_path="downloads"

def prompt(content,apikey):
    # prompt=f"Analyze the following code and give suggestion:\n\n{content}"
    # response=openai.completions.create(
    #     model=model_engine,
    #     prompt=prompt,
    #     max_tokens=1024,
    #     n=1,
    #     stop=None,
    #     temperature=0.5,
    # )
    # suggestion=response.choices[0].text_strip()
    # return suggestion
    headers = {"Authorization": f"Bearer {apikey}"}

    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": f"Analyze the following code and give suggestion:\n\n{content} ",
        "chatbot_global_action": "Act as an assistant",
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 150,
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    print(result['openai']['generated_text'])

def analyze_file(path,apikey):
    with open(path,'r') as file:
        content=file.read()
    suggestion=prompt(content,apikey)
    return suggestion

def analyze_codebase(path,apikey):
    filesto_send=[]
    for root,dirs,files in os.walk(path):
        for file in files:
            file_path=os.path.join(root,file)
            if any(file_path.endswith(ext) for ext in allowed_extensions):
                filesto_send.append(file_path)
    for file_path in filesto_send:
        suggestion=analyze_file(file_path,apikey)
        print(f"Suggestion for {file_path}:\n{suggestion}")


def github_Repository(apikey):
    print("API KEY verified!")
    fetch_github_repo()
    analyze_codebase(codebase_path,apikey)
    # if(fetch_github_repo()):
    

def start():
    print("///////////////Welcome to CodeBase Analyzer////////////")
    print("Give your Eden AI API Key:")
    apikey=input()
    # print(f"Given API KEY {apikey}")
    github_Repository(apikey)


if __name__=='__main__':
    start()