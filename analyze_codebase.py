from utils import *
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
    for file_path in filesto_send:
        suggestion=analyze_file(file_path,apikey)
        print(f"Suggestion for {file_path}:\n{suggestion}\n\n")
        print("---------------------------------------------------------------")
        suggestion_load+=f"Suggestion for {file_path}:\n{suggestion}\n\n---------------------------------------------------------------\n\n"
    download(suggestion_load)