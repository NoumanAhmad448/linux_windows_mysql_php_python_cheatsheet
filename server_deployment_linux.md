## SSH access
Read the public key from ```git bash```
```
cat ~/.ssh/id_rsa.pub
```
Create a ```config``` file in ```.ssh``` folder and add the following lines
```
Host 162.241.216.239
   HostName 162.241.216.239
   PreferredAuthentications publickey
   IdentityFile ~/.ssh/id_rsa.pub
```
ssh access command
```
ssh thesunr8@162.241.216.239
```

## apache server
1. apache status
```
 systemctl status httpd
```
apache configuration file validation command
```
apachectl configtest
```
```
nano conf/httpd.conf
```

apache configration command
```
apachectl -V | grep SERVER_CONFIG_FILE
```
