## mysql
Mysql configuration file finder
```
which mysqld
```
```
/usr/sbin/mysqld --verbose --help | grep -A 1 "Default options"
```

mysql config
```
/etc/my.cnf
```

```
nano /var/lib/mysql/server1.nctest.net.err
```

mysql connection
```
mysql -h 127.0.0.1 -P 3306 -u usmansaleem234_lyskills_root5 -p
```
clear user table for local development
```
DELETE from users;
```

mysql check logs using os
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

check if mysql server is running or not
```
ss -ae | grep mysql
```

```
Connect to mysql using username and password
```
mysql -h 203.161.43.113 -P 3306 -u user_name -p
```
