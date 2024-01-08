# Codebase-Analyzer
A python-script to analyze your github repository via LLM for code improvements,bug fixes etc.

## How to use?
- First clone and unzip this repository.
  
```terminal
 git clone https://github.com/AK3847/Codebase-Analyzer.git
```
- Navigate to  `Codebase-Analyzer` folder and run following command in the terminal:
  
```terminal
python main.py
```
- You will get an ouput like below in the terminal: <br>
  ![image](https://github.com/AK3847/Codebase-Analyzer/assets/94222544/f62d6383-8c5a-4d61-9e08-9dad642f3c0f) <br>
- Kindly provide a _GITHUB Authorization Token_ ( you can get one from <a href="https://github.com/settings/tokens target=__blank">here</a>) <br>
- Next provide _Username_ and _Repository Name_: <br>
![Screenshot 2024-01-08 170353](https://github.com/AK3847/Codebase-Analyzer/assets/94222544/344f521b-15c3-4c08-96c7-ad807ffe412f) <br>
- Now the script will download all the files from repository in the `repo-downloads` folder <br>
  ![image](https://github.com/AK3847/Codebase-Analyzer/assets/94222544/56a675ff-c045-4492-ac4a-9e336a7d08c9) <br>
- Next provide _Eden AI API Key_ ( register <a href="https://app.edenai.run/user/login" target=__blank>here</a> for free to get one): <br>
  ![Screenshot 2024-01-08 170955](https://github.com/AK3847/Codebase-Analyzer/assets/94222544/afb6ca5e-b2df-4f5b-becf-76a333a8e208) <br>
- Now the LLM will start to analyze code files one-by-one and output is shown in terminal: <br>
![image](https://github.com/AK3847/Codebase-Analyzer/assets/94222544/bd5c1ef3-49e8-472a-a1e5-49b1083ea18c) <br>
- At last all the suggestions will be stored in `suggestions.txt` file: <br>
  ![image](https://github.com/AK3847/Codebase-Analyzer/assets/94222544/c2f84f8d-7d89-4cc9-ad1b-07880fc41a43)

## How it works?
- First using the provided Github authorization token we fetch the repository using `Github` module of python, this is done in <kbd>github_fetch.py<kbd>
- Next we download all the files such as c,c++,java,python,html,css etc from the repository into our  `repo-downlaods` local folder.
  > The file extensions to be selected can be modified via <kbd>utils.py</kbd>
  
  > In case the folder is not empty, the tool automatically clears all the folder content to avoid file-mismatch.
- We connect with the Eden AI which in turn provides us free access to ChatGPT 3.5 turbo via API.
- Then all files are sent to LLM one by one via `requests` module of python with a `prompt`, this is done in <kbd>analyze_codeabase.py</kbd>
  > The prompt can be modified via <kbd>utils.py</kbd>
- All suggestions are stored in `suggestions.txt` file for later use.
