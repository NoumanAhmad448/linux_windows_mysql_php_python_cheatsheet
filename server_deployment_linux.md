## SSH access
Read the public key from ```git bash```
```
cat ~/.ssh/id_rsa.pub
```
Create a ```config``` file in ```.ssh``` folder and add the following lines
```
Host ip_addr
   HostName ip_addr
   PreferredAuthentications publickey
   IdentityFile ~/.ssh/id_rsa.pub
```
ssh access command
```
ssh usr@ip
```

## Linux (ubuntu | centos)
create symbolink/link/shortcut in differnt folder
*PS: * bash is original path, /bin/sh is target path
```
sudo ln -sf bash /bin/sh
```
delete multiple lines in nano
```
use CTRL+Shift+6 to mark the beginning of your block
move cursor with arrow keys to end of your block, the text will be highlighted.
use CTRL+K to cut/delete block.
```

hostname finder
```
hostname
```
value
```
server1.lyskills.com
```
datadir finder
```
mysql -uusmansaleem234_lyskills_root5 -p -e 'SHOW VARIABLES WHERE Variable_Name LIKE "%dir"'
```
OR login to mysql and run the following
```
select @@datadir;
```
OR
```
mysqld --verbose --help | grep ^datadir
```

mysql connection
```
mysql -h 127.0.0.1 -P 3306 -u usmansaleem234_lyskills_root5 -p
```


mysql configuration
```
systemctl daemon-reload && systemctl restart mysql
```
```
systemctl status mysql
```
or

```
journalctl -xe
```
```
systemctl start mysql
```

```
nano /etc/my.cnf
```
change group ownership/permission
```
chgrp user_name file/folder
```
change user ownership/permission
```
chown user_name file/folder
```
change permission
```
chmod 666/777/+rwx/-rwx/+rw/-rw/ file/folder
```

## Apache server
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
