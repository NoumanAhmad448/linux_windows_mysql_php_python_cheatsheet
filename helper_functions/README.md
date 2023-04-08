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
