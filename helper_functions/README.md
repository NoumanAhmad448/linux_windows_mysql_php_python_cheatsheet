```
def unzip_file(file_path: str, main_folder:str):
  """
  require:
  import zipfile 

  file_path: the given file path 
  main_folder: where you want to extract  
  """
  with zipfile.ZipFile(file_path, "r") as zip_file:
    zip_file.extractall(main_folder)
```

An Example of using the tqdm 
```
from tqdm.notebook import tqdm

for no in tqdm(range(1, 50000000), desc="title"):
  if( no == 50000000-1):
    print(no)
```

```
def download_file(file_name: str, download_resource: str):
  """
  download a file from the internet and save it locally 
  require: 
  import requests
  from pathlib import Path
  """
  file = requests.get(download_resource)
  if not(Path(file_name).is_file()):
      with open(file_name, "wb") as f:
        f.write(file.content)
      print(f"Given file {file_name} has downloaded and saved!")
```
