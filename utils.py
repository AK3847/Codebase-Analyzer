import os
import json
import requests
import  shutil
import json
import requests


import openai
from github import Github

from rich import print, pretty
pretty.install()



allowed_extensions = ['c', 'h', 'cpp', 'hpp', 'java', 'py', 'html', 'css', 'js', 'php', 'ruby', 'swift', 'go', 'dart', 'kotlin', 'ts', 'tsx', 'csharp', 'vb', 'scala', 'r', 'rust', 'lua', 'shell', 'sh', 'bash', 'ps1', 'json', 'xml', 'yaml', 'toml', 'ini']
prompt_text="Analyze the following code and give suggestion for Code Improvement,Code Optimization,Bug Identification and Resolution\n\n"
repo_path=f"{os.path.dirname(os.path.realpath(__file__))}\\repo-downloads"