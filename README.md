# Codebase-Analyzer
A python-script to analyze your github repository via ChatGPT LLM for code improvements,bug fixes etc.
- [How to use?](https://github.com/AK3847/Codebase-Analyzer/edit/main/README.md#how-to-use)
- [How it works?](https://github.com/AK3847/Codebase-Analyzer/tree/main#how-it-works)
- [Python Modules used](https://github.com/AK3847/Codebase-Analyzer/tree/main?tab=readme-ov-file#python-modules-used)
## 🚀 How to use?
- First clone and unzip this repository.
  
```terminal
 git clone https://github.com/AK3847/Codebase-Analyzer.git
```
- Navigate to  `Codebase-Analyzer` folder and run following command in the terminal:
  
```terminal
python main.py
```
- You will get an ouput like below in the terminal: <br>
  ![Screenshot 2024-01-09 023242](https://github.com/AK3847/Codebase-Analyzer/assets/94222544/7310c561-f2d8-4397-83bc-06fd8728edea) <br>
  
- Kindly provide a _GITHUB Authorization Token_ ( you can get one from [here](https://github.com/settings/token) ) <br>

- Next chose either one of the option : <br>
  ![image](https://github.com/AK3847/Codebase-Analyzer/assets/94222544/779e8e3b-6d69-49f4-9dbe-f06302c091fa)<br>
  
- Now the script will download all the files from repository in the `repo-downloads` folder <br>
  ![image](https://github.com/AK3847/Codebase-Analyzer/assets/94222544/56a675ff-c045-4492-ac4a-9e336a7d08c9) <br>
  
- Next provide _OpenAI API Key_ ( register <a href="https://platform.openai.com/signup">here</a> to start with initial free credits): <br>
  ![Screenshot 2024-01-09 024135](https://github.com/AK3847/Codebase-Analyzer/assets/94222544/a1f12ace-8ea2-4c4d-a0ef-2cf9bee29c38)


- Now the LLM will start to analyze code files one-by-one and output is shown in terminal: <br>
![image](https://github.com/AK3847/Codebase-Analyzer/assets/94222544/bd5c1ef3-49e8-472a-a1e5-49b1083ea18c) <br>

- At last all the suggestions will be stored in `suggestions.txt` file: <br>
  ![image](https://github.com/AK3847/Codebase-Analyzer/assets/94222544/c2f84f8d-7d89-4cc9-ad1b-07880fc41a43)

## ✨ How it works?
- First using the provided Github authorization token we fetch the repository using `Github` module of python, this is done in <kbd>github_fetch.py<kbd>
- Next we download all the files such as c,c++,java,python,html,css etc from the repository into our  `repo-downlaods` local folder.
  > The file extensions to be selected can be modified via <kbd>utils.py</kbd>
  
  > In case the folder is not empty, the tool automatically clears all the folder content to avoid file-mismatch.
- We connect with the Eden AI which in turn provides us free access to ChatGPT 3.5 turbo via API.
- Then all files are sent to LLM one by one via `requests` module of python with a `prompt`, this is done in <kbd>analyze_codeabase.py</kbd>
  > The prompt can be modified via <kbd>utils.py</kbd>
- All suggestions are stored in `suggestions.txt` file for later use.

## 🐍 Python Modules used:
```
  os
  json
  requets
  shutil
  json
  requests
  re
  openai
  github
  rich
```
_All of this are imported in_ `utils.py`
