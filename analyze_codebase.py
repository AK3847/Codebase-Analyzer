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
        "temperature": 0.25,
        "max_tokens": 3000,
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    # print(result['openai']['generated_text'])
    generated_text = result.get('openai', {}).get('generated_text', 'No suggestion available')
    return generated_text
    # return result['openai']['generated_text']

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
        task = progress.add_task("[#5272F2]Analyzing Codebase...", total=len(filesto_send))
        for file_path in filesto_send:
            progress.update(task, advance=1)
            suggestion = analyze_file(file_path, apikey)
            console.print("\n")
            console.print(f"\n[not italic]Suggestion for[/not italic] {os.path.basename(file_path)}:\n", style="italic #FFD95A")
            console.print(f"{suggestion}\n",style="italic #FCF5ED")
            console.print("---------------------------------------------------------------")
            suggestion_load += f"Suggestion for {file_path}:\n{suggestion}\n---------------------------------------------------------------\n\n"
        
    download(suggestion_load)