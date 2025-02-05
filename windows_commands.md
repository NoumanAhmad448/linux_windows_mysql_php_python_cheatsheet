## Windows Processes
1. Find a process using the string ```docker``` and kill it using ```taskkill ```
```
tasklist | findstr /i docker
```

2. Kill stop a process software application. You may find such proceses using ```tasklist``` command
```
taskkill /F /IM DockerDesktop.exe
```


## SSH keys
powershell | Gitbash
```
ssh-keygen -t rsa -b 4096 -C "sign448free@outlook.com"
Start-Service ssh-agent
```
fetch/get SSH key from windows
```
cat ~/.ssh/id_rsa.pub | clip
```
Authenticate SSH key with github 
```
ssh -T git@github.com
```
