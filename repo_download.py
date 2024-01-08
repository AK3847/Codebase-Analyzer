from utils import *
from rich.progress import Progress
from rich.console import Console
console=Console()
def clear_subdirectories(folder_path):
    if os.path.exists(folder_path):
        entries = os.listdir(folder_path)
        with Progress(console=console, transient=True) as progress:
            task = progress.add_task("[{#CD1818}]Clearing subdirectories...", total=len(entries))
            for entry in entries:
                entry_path = os.path.join(folder_path, entry)
                if os.path.isdir(entry_path):
                    try:
                        shutil.rmtree(entry_path)
                        progress.update(task, advance=1, description=f"Clearing: {entry}")
                        console.print(f"The subdirectory {entry_path} and its contents have been cleared.",style="#CF0A0A")
                    except Exception as e:
                        console.print(f"Failed to clear {entry_path}: {e}",style="#CF0A0A")
                else:
                    try:
                        os.remove(entry_path)
                        progress.update(task, advance=1, description=f"Deleting: {entry}")
                        console.print(f"The file {entry_path} has been deleted.",style="#CF0A0A")
                    except Exception as e:
                       console.print(f"Failed to delete {entry_path}: {e}",style="#CF0A0A")
    else:
        console.print(f"The folder {folder_path} does not exist.",style="Italic #CF0A0A")


def download_repo(g, repo_name, destination_folder, allowed_extensions):
    repo = g.get_repo(repo_name)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    destination_folder_path = os.path.join(script_dir, destination_folder)
    clear_subdirectories(destination_folder)
    def download_contents(contents, current_path=""):
        for content in contents:
            if content.type == "file":
                file_extension = os.path.splitext(content.name)[1][1:]
                if file_extension in allowed_extensions:
                    file_content = repo.get_contents(content.path)
                    decoded_content = file_content.decoded_content
                    local_file_path = os.path.join(destination_folder_path, current_path, content.name)
                    os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
                    with open(local_file_path, 'wb') as f:
                        f.write(decoded_content)
                    console.print(f"Downloaded: {content.path}",style="#42855B")
            elif content.type == "dir":
                subdir_contents = repo.get_contents(content.path)
                download_contents(subdir_contents, os.path.join(current_path, content.name))

    root_contents = repo.get_contents("")
    download_contents(root_contents)
