## Windows Processes
1. Find a process using the string ```docker``` and kill it using ```taskkill ```
```
tasklist | findstr /i docker
```

2. Kill stop a process software application. You may find such proceses using ```tasklist``` command
```
taskkill /F /IM DockerDesktop.exe
```
