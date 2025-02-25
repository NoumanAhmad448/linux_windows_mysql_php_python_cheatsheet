### Step 1: Gather Necessary Information
Before starting, ensure you have the following:
- Domain name registered with Namecheap.
- Hosting account details (IP address, SSH access credentials, etc.).
- Access to the hosting control panel or SSH access to the server.

### Step 2: Update Domain DNS Settings on Namecheap
1. **Log in to Namecheap**: Access your Namecheap account.
2. **Navigate to Domain List**: Click on "Domain List" from the left sidebar.
3. **Select Your Domain**: Click on the "Manage" button next to your domain.
4. **Update DNS Settings**:
   - Find the "Nameservers" section.
   - Choose "Custom DNS" and enter the nameservers provided by your hosting provider.
   - Save changes.

### Step 3: Connect to Hosting via SSH
1. **Generate SSH Key** (if not already done):
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
2. **Copy Public Key**:
   ```bash
   cat ~/.ssh/id_rsa.pub
   ```
3. **Configure SSH**:
   - Create a `config` file in the `.ssh` directory:
     ```bash
     nano ~/.ssh/config
     ```
   - Add the following lines:
     ```plaintext
     Host ip_addr
        HostName ip_addr
        PreferredAuthentications publickey
        IdentityFile ~/.ssh/id_rsa.pub
     ```
4. **SSH Access**:
   ```bash
   ssh usr@ip
   ```
#### Troubleshooting
- access your server via VNC
- open the /etc/ssh/sshd_config file for editing
- make sure the "PermitRootLogin" parameter is set to "Yes"
- save and exit the file
- run the following command: systemctl restart sshd
  
### Step 4: Configure Web Server (Apache)
1. **Check Apache Status**:
   ```bash
   systemctl status httpd
   ```
2. **Validate Apache Configuration**:
   ```bash
   apachectl configtest
   ```
3. **Edit Apache Configuration**:
   ```bash
   nano /etc/httpd/conf/httpd.conf
   ```
4. **Restart Apache**:
   ```bash
   systemctl restart httpd
   ```

### Step 5: Database Configuration (MySQL)
1. **Connect to MySQL**:
   ```bash
   mysql -h 127.0.0.1 -P 3306 -u your_db_user -p
   ```
2. **Check Data Directory**:
   ```bash
   mysql -u your_db_user -p -e 'SHOW VARIABLES WHERE Variable_Name LIKE "%dir"'
   ```
3. **Restart MySQL**:
   ```bash
   systemctl restart mysql
   ```

### Step 6: File Permissions and Ownership
1. **Change Group Ownership**:
   ```bash
   chgrp user_name file/folder
   ```
2. **Change User Ownership**:
   ```bash
   chown user_name file/folder
   ```
3. **Change Permissions**:
   ```bash
   chmod 755 file/folder
   ```
### Verify the Actual Domain Path Using Domain List in cPanel

#### **1. Access cPanel**
1. Log in to **Namecheap** and access **cPanel**.

#### **2. Use the Domain List Option**
1. In cPanel, search for the **Domains** section.
2. Click on **Domains** or **Domain List**.
3. You will see a list of all domains (primary, addon, and subdomains).
4. Check the **Document Root** column for each domain to see the actual file path. Example:
   - Primary domain: `/home/username/public_html`
   - Addon domain: `/home/username/public_html/addondomain.com`
   - Subdomain: `/home/username/public_html/subdomain.yourdomain.com`

### **2. Configure FTP Account**
1. In cPanel, search for the **FTP Accounts** tool.
2. Under **Add FTP Account**:
   - Enter a username (e.g., `yourdomain_user`).
   - Enter a strong password.
   - Set the directory to the domain's root path (e.g., `/home/username/public_html`).
3. Click **Create FTP Account**.
4. Use the provided FTP credentials (username, password, and server address) to connect via an FTP client like FileZilla.

#### **3. Connect via FTP Client**
1. Open your FTP client (e.g., FileZilla).
2. Enter the following details:
   - **Host**: `yourdomain.com` or the server IP.
   - **Username**: `yourdomain_user` (full FTP username, e.g., `yourdomain_user@yourdomain.com`).
   - **Password**: The password you set.
   - **Port**: `21` (default FTP port).
3. Click **Quickconnect** to access your domain's files.

#### **4. Verify Access**
- Once connected, you should see the files in the directory you specified (e.g., `public_html`).


### Step 7: Verify Domain Connection
1. **Check Hostname**:
   ```bash
   hostname
   ```
2. **Test Website**: Open your web browser and navigate to your domain to ensure it loads correctly.

# Troubleshooting Documentation

This section provides detailed troubleshooting steps for common issues encountered during development and deployment. Each subsection focuses on a specific area, such as Apache, MySQL, PHP, and more.

---

## Apache Troubleshooting

### 1. **Check Apache Status**
To check if Apache is running:
```bash
systemctl status httpd
```

### 2. **Restart Apache**
If Apache is not running or needs a restart:
```bash
systemctl restart httpd
```

### 3. **Validate Apache Configuration**
Check for syntax errors in the Apache configuration file:
```bash
apachectl configtest
```

### 4. **Locate Apache Configuration File**
Find the path to the Apache configuration file:
```bash
apachectl -V | grep SERVER_CONFIG_FILE
```

### 5. **Edit Apache Configuration**
Edit the Apache configuration file:
```bash
nano /etc/httpd/conf/httpd.conf
```

### 6. **Common Errors**
- **Port Conflict**: Ensure no other service is using port 80 or 443.
- **Permission Issues**: Check file permissions for the web root directory.
- **Module Errors**: Ensure required modules (e.g., `mod_rewrite`) are enabled.

---

## MySQL Troubleshooting

### 1. **Check MySQL Status**
To check if MySQL is running:
```bash
systemctl status mysql
```

### 2. **Restart MySQL**
If MySQL is not running or needs a restart:
```bash
systemctl restart mysql
```

### 3. **Locate MySQL Configuration File**
Find the path to the MySQL configuration file:
```bash
mysql --verbose --help | grep "Default options"
```

### 4. **Edit MySQL Configuration**
Edit the MySQL configuration file:
```bash
nano /etc/my.cnf
```

### 5. **Check MySQL Logs**
Find and check MySQL error logs:
```bash
my_print_defaults --mysqld | grep log-error
```
Or:
```bash
nano /var/lib/mysql/hostname.err
```

### 6. **Common Errors**
- **Connection Issues**: Verify MySQL credentials in `.env`.
- **Permission Issues**: Ensure the MySQL user has proper permissions.
- **Corrupted Tables**: Run `mysqlcheck` to repair corrupted tables.

---

## PHP Troubleshooting

### 1. **Check PHP Version**
To check the installed PHP version:
```bash
php -v
```

### 2. **Locate PHP Configuration File**
Find the path to the PHP configuration file:
```bash
php --ini
```

### 3. **Edit PHP Configuration**
Edit the PHP configuration file:
```bash
nano /etc/php.ini
```

### 4. **Common Errors**
- **File Upload Issues**: Increase `upload_max_filesize` and `post_max_size` in `php.ini`.
- **Memory Limit**: Increase `memory_limit` in `php.ini`.
- **Extensions Missing**: Enable required extensions (e.g., `curl`, `pdo_mysql`).

---

## Laravel Troubleshooting

### 1. **Clear Laravel Cache**
Clear configuration and application cache:
```bash
php artisan config:clear
php artisan cache:clear
```

### 2. **Check Laravel Logs**
View Laravel logs for errors:
```bash
nano storage/logs/laravel.log
```

### 3. **Common Errors**
- **Environment File**: Ensure `.env` is correctly configured.
- **Permissions**: Set proper permissions for `storage` and `bootstrap/cache`.
- **Database Migrations**: Run `php artisan migrate` to apply database changes.

### Troubleshooting: Files Being Downloaded Instead of Executed

If files are being downloaded from the website instead of being executed, it typically indicates that PHP is not running or Apache/Nginx is not properly configured. Follow these steps to resolve the issue:

1. **Check `.htaccess` Files**  
   Ensure the `.htaccess` files in both the **root** and **public** folders are correctly configured.

   - **Root `.htaccess`**:
     ```apache
     <IfModule mod_rewrite.c>
         RewriteEngine On
         RewriteRule ^(.*)$ public/$1 [L]
     </IfModule>
     ```

   - **Public `.htaccess`**:
     ```apache
     <IfModule mod_rewrite.c>
         RewriteEngine On
         RewriteCond %{REQUEST_FILENAME} !-d
         RewriteCond %{REQUEST_FILENAME} !-f
         RewriteRule ^ index.php [L]
     </IfModule>
     ```

2. **Verify Apache Configuration**  
   Ensure Apache is properly configured to handle PHP files and that the `AllowOverride` directive is set to `All` in your Apache configuration file.

   - Open your Apache configuration file:
     ```bash
     sudo nano /etc/apache2/sites-available/yourdomain.conf
     ```
   - Ensure the following settings are present:
     ```apache
     <Directory /path/to/your/laravel/project/public>
         AllowOverride All
         Require all granted
     </Directory>
     ```
   - Enable `mod_rewrite` if it is not already enabled:
     ```bash
     sudo a2enmod rewrite
     sudo systemctl restart apache2
     ```

3. **Verify Nginx Configuration (if applicable)**  
   If you are using Nginx, ensure the configuration file is correctly set up to handle PHP files.

   - Open your Nginx configuration file:
     ```bash
     sudo nano /etc/nginx/sites-available/yourdomain
     ```
   - Ensure the following settings are present:
     ```nginx
     server {
         listen 80;
         server_name yourdomain.com;
         root /path/to/your/laravel/project/public;

         index index.php index.html index.htm;

         location / {
             try_files $uri $uri/ /index.php?$query_string;
         }

         location ~ \.php$ {
             include snippets/fastcgi-php.conf;
             fastcgi_pass unix:/var/run/php/php8.1-fpm.sock; # Adjust PHP version if needed
             fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
             include fastcgi_params;
         }

         location ~ /\.ht {
             deny all;
         }
     }
     ```
   - Test the Nginx configuration and restart the server:
     ```bash
     sudo nginx -t
     sudo systemctl restart nginx
     ```

4. **Verify PHP is Running**  
   Ensure PHP is installed and running on your server. You can test this by creating a `phpinfo.php` file in the `public` directory:
   ```php
   <?php
   phpinfo();
   ```
   Access `http://yourdomain.com/phpinfo.php` in your browser. If PHP is running, you will see the PHP information page. Delete this file after testing for security reasons.

5. **Check File Permissions**  
   Ensure the correct file permissions are set for the Laravel project:
   ```bash
   # Set directory permissions to 755
   find /path/to/your/laravel/project -type d -exec chmod 755 {} \;

   # Set file permissions to 644
   find /path/to/your/laravel/project -type f -exec chmod 644 {} \;

   # Set permissions for storage and bootstrap/cache
   chmod -R 775 /path/to/your/laravel/project/storage
   chmod -R 775 /path/to/your/laravel/project/bootstrap/cache
   ```


---

## Node.js Troubleshooting

### 1. **Check Node.js Version**
To check the installed Node.js version:
```bash
node -v
```

### 2. **Install Dependencies**
Install Node.js dependencies:
```bash
npm install
```

### 3. **Run Development Server**
Start the development server:
```bash
npm run watch
```

### 4. **Common Errors**
- **Version Mismatch**: Ensure the correct Node.js version is installed.
- **Missing Modules**: Reinstall dependencies using `npm install`.

---

## Git and GitHub Troubleshooting

### 1. **Check Git Status**
To check the current Git status:
```bash
git status
```

### 2. **Pull Latest Changes**
Pull the latest changes from the remote repository:
```bash
git pull origin main
```

### 3. **Resolve Merge Conflicts**
If there are merge conflicts, resolve them manually and commit:
```bash
git add .
git commit -m "Resolved merge conflicts"
```

### 4. **Common Errors**
- **Authentication Issues**: Ensure SSH keys are correctly configured.
- **Branch Issues**: Verify you are on the correct branch.

---

## File Permissions Troubleshooting

### 1. **Change File Ownership**
Change the owner of a file or directory:
```bash
chown user_name:group_name file_or_directory
```

### 2. **Change File Permissions**
Change file permissions:
```bash
chmod 755 file_or_directory
```

### 3. **Common Errors**
- **Permission Denied**: Ensure the user has proper permissions.
- **Read-Only Filesystem**: Remount the filesystem with write permissions.

---

## Server Logs Troubleshooting

### 1. **Check Apache Logs**
View Apache error logs:
```bash
nano /var/log/httpd/error_log
```

### 2. **Check MySQL Logs**
View MySQL error logs:
```bash
nano /var/lib/mysql/hostname.err
```

### 3. **Check Laravel Logs**
View Laravel logs:
```bash
nano storage/logs/laravel.log
```

---

## Cloudflare Troubleshooting

### 1. **Check DNS Settings**
Ensure DNS records are correctly configured in Cloudflare.

### 2. **Clear Cloudflare Cache**
Clear the Cloudflare cache to reflect changes:
1. Log in to Cloudflare.
2. Navigate to **Caching** > **Configuration** > **Purge Cache**.

### 3. **Common Errors**
- **SSL Issues**: Ensure SSL is properly configured in Cloudflare.
- **DNS Propagation**: Wait for DNS changes to propagate.

---

## General Troubleshooting Tips

### 1. **Check Disk Space**
Check available disk space:
```bash
df -h
```

### 2. **Check Memory Usage**
Check memory usage:
```bash
free -m
```

### 3. **Check Running Processes**
View running processes:
```bash
top
```


