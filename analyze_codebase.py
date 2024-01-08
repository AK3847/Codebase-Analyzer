from utils import *
from rich.console import Console
from rich.progress import Progress
from suggestion_download import download
suggestion_load=""
def prompt(content,apikey):
    headers = {"Authorization": f"Bearer {apikey}"}
    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": f"{prompt_text}{content} ",
        "chatbot_global_action": "Act as an assistant",
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 2000,
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    # print(result['openai']['generated_text'])
    return result['openai']['generated_text']

def analyze_file(path,apikey):
    with open(path,'r') as file:
        content=file.read()
    suggestion=prompt(content,apikey)
    return suggestion

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
        task = progress.add_task("[cyan]Analyzing Codebase...", total=len(filesto_send))
        for file_path in filesto_send:
            progress.update(task, advance=1)
            suggestion = analyze_file(file_path, apikey)
            console.print()
            console.print(f"Suggestion for {file_path}:\n{suggestion}\n", style="italic #b98200")
            console.print("---------------------------------------------------------------")
            suggestion_load += f"Suggestion for {file_path}:\n{suggestion}\n---------------------------------------------------------------\n\n"
        
    download(suggestion_load)