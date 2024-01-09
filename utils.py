import os
import json
import requests
import  shutil
import json
import requests
import re
import getpass
import pwinput


import openai
from github import Github

from rich import print, pretty
pretty.install()



allowed_extensions = ['c', 'h', 'cpp', 'hpp', 'java', 'py', 'html', 'css', 'js', 'php', 'ruby', 'swift', 'go', 'dart', 'kotlin', 'ts', 'tsx', 'csharp', 'vb', 'scala', 'r', 'rust', 'lua', 'shell', 'sh', 'bash', 'ps1', 'json', 'xml', 'yaml', 'toml', 'ini']
# prompt_text="Analyze the following code and give suggestion for Code Improvement,Code Optimization,Bug Identification and Resolution, suggest no more than 2-3 points per topic.\n\n"
repo_path=f"{os.path.dirname(os.path.realpath(__file__))}\\repo-downloads"
prompt_text="Please review the code below and identify any syntax or logical errors, suggest ways to refactor and improve code quality, enhance performance, address security concerns, and bug identification & fix. Limit your response to 2-3 suggestion per field."
codebase_ASCII_ART=""" 

 ______  ______  _____   ______  ______  ______  ______  ______       ______  __   __  ______  __      __  __  ______  ______  ______    
/\  ___\/\  __ \/\  __-./\  ___\/\  == \/\  __ \/\  ___\/\  ___\     /\  __ \/\ "-.\ \/\  __ \/\ \    /\ \_\ \/\___  \/\  ___\/\  == \   
\ \ \___\ \ \/\ \ \ \/\ \ \  __\\  \  __<\ \  __ \ \___  \ \  __\     \ \  __ \ \ \-.  \ \  __ \ \ \___\ \____ \/_/  /_\ \  __\\\ \  __<   
 \ \_____\ \_____\ \____-\ \_____\ \_____\ \_\ \_\/\_____\ \_____\    \ \_\ \_\ \_\\"\_ \ \_\ \_\ \_____\/\_____\/\_____\ \_____\ \_\ \_\ 
  \/_____/\/_____/\/____/ \/_____/\/_____/\/_/\/_/\/_____/\/_____/     \/_/\/_/\/_/ \/_/\/_/\/_/\/_____/\/_____/\/_____/\/_____/\/_/ /_/ 
                                                                                                                                         

            
"""