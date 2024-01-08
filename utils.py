import os
import json
import requests
import  shutil
import json
import requests
import re


import openai
from github import Github

from rich import print, pretty
pretty.install()



allowed_extensions = ['c', 'h', 'cpp', 'hpp', 'java', 'py', 'html', 'css', 'js', 'php', 'ruby', 'swift', 'go', 'dart', 'kotlin', 'ts', 'tsx', 'csharp', 'vb', 'scala', 'r', 'rust', 'lua', 'shell', 'sh', 'bash', 'ps1', 'json', 'xml', 'yaml', 'toml', 'ini']
prompt_text="Analyze the following code and give suggestion for Code Improvement,Code Optimization,Bug Identification and Resolution\n\n"
repo_path=f"{os.path.dirname(os.path.realpath(__file__))}\\repo-downloads"

codebase_ASCII_ART=""" 

 ______  ______  _____   ______  ______  ______  ______  ______       ______  __   __  ______  __      __  __  ______  ______  ______    
/\  ___\/\  __ \/\  __-./\  ___\/\  == \/\  __ \/\  ___\/\  ___\     /\  __ \/\ "-.\ \/\  __ \/\ \    /\ \_\ \/\___  \/\  ___\/\  == \   
\ \ \___\ \ \/\ \ \ \/\ \ \  __\\  \  __<\ \  __ \ \___  \ \  __\     \ \  __ \ \ \-.  \ \  __ \ \ \___\ \____ \/_/  /_\ \  __\\\ \  __<   
 \ \_____\ \_____\ \____-\ \_____\ \_____\ \_\ \_\/\_____\ \_____\    \ \_\ \_\ \_\\"\_ \ \_\ \_\ \_____\/\_____\/\_____\ \_____\ \_\ \_\ 
  \/_____/\/_____/\/____/ \/_____/\/_____/\/_/\/_/\/_____/\/_____/     \/_/\/_/\/_/ \/_/\/_/\/_/\/_____/\/_____/\/_____/\/_____/\/_/ /_/ 
                                                                                                                                         

            
"""