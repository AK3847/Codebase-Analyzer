from utils import *
from rich.console import Console
from rich.progress import Progress
from suggestion_download import download
from tokens import tokencount

suggestion_load=""

#function to analyze the given file using Eden AI (a third party AI which uses ChatGPT in the backend)
def prompt_edenai(content,apikey):
    headers = {"Authorization": f"Bearer {apikey}"}
    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": f"{prompt_text}{content} ",
        "chatbot_global_action": "Act as an assistant",
        "previous_history": [],
        "temperature": 0.25,
        "max_tokens": 3000,
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    # print(result['openai']['generated_text'])
    generated_text = result.get('openai', {}).get('generated_text', 'No suggestion available')
    return generated_text

#function to analyze a code file (content) via ChatGPT using given API KEY
def prompt_openai(content,apikey):
    headers={
        "Authorization":f"Bearer {apikey}",
        "Content-Type":"application/json"
    }
    url="https://api.openai.com/v1/chat/completions"
    payload={
        "model":"gpt-3.5-turbo",
        "messages":[{"role":"user","content":f"{prompt_text}{content}"}],
        "temperature":0.25,
        "max_tokens": 3000
        # "response-format":
    }
    response=requests.post(url,json=payload,headers=headers)
    result=json.loads(response.text)
    # print(result)
    generated_text=result.get('choices', [{}])[0].get('message', {}).get('content', 'No content available')
    return generated_text

#to analyze the file give in argument and return the suggestion given by ChatGPT
def analyze_file(path,apikey):
    with open(path,'r') as file:
        content=file.read()
    if(tokencount(content)):
        suggestion=prompt_openai(content,apikey)
        return suggestion
    else:
        return "The code length is more than 1000 token! Can't send it to ChatGPT for analyzing ( 4097 token limit)"


#function to analyze the whole codebase file-by-file
def analyze_codebase(path,apikey):
    global suggestion_load
    filesto_send=[]
    for root,dirs,files in os.walk(path):
        for file in files:
            file_path=os.path.join(root,file)
            if any(file_path.endswith(ext) for ext in allowed_extensions):
                filesto_send.append(file_path)
    console = Console()
    with Progress() as progress:
        task = progress.add_task("[#5272F2]Analyzing Codebase...", total=len(filesto_send))
        for file_path in filesto_send:
            suggestion = analyze_file(file_path, apikey)
            console.print("\n")
            console.print(f"\n[not italic]Suggestion for[/not italic] {os.path.basename(file_path)}:\n", style="italic #FFD95A")
            console.print(f"{suggestion}\n",style="italic #FCF5ED")
            console.print("---------------------------------------------------------------")
            progress.update(task, advance=1)
            suggestion_load += f"Suggestion for {os.path.basename(file_path)}:\n{suggestion}\n---------------------------------------------------------------\n\n"
        
    download(suggestion_load)