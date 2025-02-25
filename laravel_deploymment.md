# Laravel Project Deployment Guide

This guide provides a step-by-step process for deploying a Laravel project. It includes instructions for file permissions, `.env` configuration, MySQL connection, email setup, Laravel logs, domain configuration, FTP setup, and Apache configuration. Follow the steps in sequence to ensure a successful deployment.

---

## 1. **File Permissions**
Ensure the correct file permissions are set for the Laravel project.

```bash
# Navigate to the project directory
cd /path/to/your/laravel/project

# Set directory permissions to 755
find . -type d -exec chmod 755 {} \;

# Set file permissions to 644
find . -type f -exec chmod 644 {} \;

# Set permissions for storage and bootstrap/cache
chmod -R 775 storage bootstrap/cache

# Set ownership to the web server user (e.g., www-data for Apache)
chown -R www-data:www-data /path/to/your/laravel/project
```

---

## 2. **.env File Configuration**
Update the `.env` file with the correct environment variables.

```env
APP_ENV=production
APP_KEY=base64:your_generated_app_key
APP_DEBUG=false
APP_URL=http://yourdomain.com

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=your_database_name
DB_USERNAME=your_database_user
DB_PASSWORD=your_database_password

MAIL_MAILER=smtp
MAIL_HOST=your_smtp_host
MAIL_PORT=587
MAIL_USERNAME=your_email@domain.com
MAIL_PASSWORD=your_email_password
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS=your_email@domain.com
MAIL_FROM_NAME="${APP_NAME}"
```

---

## 3. **MySQL Connection and Verification**
Verify the MySQL connection using SSH.

```bash
# Connect to MySQL
mysql -u your_database_user -p

# Verify the database
USE your_database_name;
SHOW TABLES;
```

---

## 4. **Email Configuration**
Ensure the email settings in `.env` are correct. Test the email functionality using Laravel's `tinker`.

```bash
php artisan tinker
\Mail::raw('Test email', function ($message) {
    $message->to('test@example.com')->subject('Test Email');
});
```

---

## 5. **Laravel Logs Configuration**
Configure Laravel logs to ensure proper logging.

```bash
# Ensure the storage/logs directory is writable
chmod -R 775 storage/logs

# Check the log file
tail -f storage/logs/laravel.log
```

---

## 6. **Domain Configuration with PHP Version**
Configure the domain to use the correct PHP version in the `php.ini` manager.

1. Log in to cPanel.
2. Navigate to **MultiPHP INI Editor**.
3. Select your domain.
4. Set the PHP version to the required version (e.g., PHP 8.1).
5. Update the following settings:
   ```ini
   upload_max_filesize = 100M
   post_max_size = 100M
   memory_limit = 256M
   ```

---

## 7. **FTP Configuration**
Configure FTP and verify the port.

```bash
# Check if FTP port 21 is listening
sudo netstat -tuln | grep :21

# Locate the FTP configuration file (e.g., vsftpd.conf)
sudo nano /etc/vsftpd.conf

# Increase file size limits in the FTP configuration
max_client=50
max_per_ip=10
local_max_rate=10485760
anon_max_rate=10485760
```

---

## 8. **Storage Directory Configuration**
Ensure the `storage/framework` directory has the required subdirectories.

```bash
# Create necessary directories
mkdir -p storage/framework/{sessions,views,cache}

# Set permissions
chmod -R 775 storage/framework
```

---

## 9. **Apache Configuration**
Ensure Apache is listening to the correct folder and executing PHP files.

1. Locate the Apache configuration file:
   ```bash
   sudo nano /etc/apache2/sites-available/yourdomain.conf
   ```
2. Update the `DocumentRoot` and `Directory` settings:
   ```apache
   <VirtualHost *:80>
       ServerAdmin webmaster@yourdomain.com
       DocumentRoot /path/to/your/laravel/project/public
       <Directory /path/to/your/laravel/project/public>
           AllowOverride All
           Require all granted
       </Directory>
       ErrorLog ${APACHE_LOG_DIR}/error.log
       CustomLog ${APACHE_LOG_DIR}/access.log combined
   </VirtualHost>
   ```
3. Restart Apache:
   ```bash
   sudo systemctl restart apache2
   ```

---

## 10. **.htaccess Configuration**
Ensure `.htaccess` files in the root and `public` folders point to the correct PHP version.

1. Root `.htaccess`:
   ```apache
   <IfModule mod_rewrite.c>
       RewriteEngine On
       RewriteRule ^(.*)$ public/$1 [L]
   </IfModule>
   ```
2. Public `.htaccess`:
   ```apache
   <IfModule mod_rewrite.c>
       RewriteEngine On
       RewriteCond %{REQUEST_FILENAME} !-d
       RewriteCond %{REQUEST_FILENAME} !-f
       RewriteRule ^ index.php [L]
   </IfModule>
   ```

---

## 11. **Update PHP Settings in cPanel and WHM**
Increase file size limits in both cPanel and WHM.

1. **cPanel:**
   - Navigate to **MultiPHP INI Editor**.
   - Update:
     ```ini
     upload_max_filesize = 100M
     post_max_size = 100M
     memory_limit = 256M
     ```

2. **WHM:**
   - Navigate to **PHP INI Editor** under **Software**.
   - Update the same settings as above.

---

## 12. **Verify Deployment**
1. Access your domain in a browser to ensure the Laravel application loads.
2. Check the Laravel logs for any errors:
   ```bash
   tail -f storage/logs/laravel.log
   ```
3. Test file uploads and email functionality.

# Laravel Project Deployment Guide (Continued)

This section provides additional steps and troubleshooting tips to ensure a smooth deployment process. Each step is clearly outlined for easy reference.

---

## 13. **Remove `.env` Command from GitHub Actions**
If the `.env` file is not being uploaded to the server via GitHub Actions, ensure it is excluded from the deployment process. Update your `.github/workflows/deploy.yml` file to remove any commands related to `.env`.

Example `.github/workflows/deploy.yml`:
```yaml
name: Deploy Laravel App

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Install dependencies
        run: composer install --no-dev --optimize-autoloader

      - name: Set up environment
        run: |
          cp .env.example .env
          php artisan key:generate

      # Remove the following step if .env is not being uploaded
      # - name: Upload .env
      #   run: scp .env user@your_server:/path/to/your/laravel/project/.env

      - name: Deploy to server
        run: rsync -avz --exclude='.env' --exclude='.git' ./ user@your_server:/path/to/your/laravel/project
```

---

## 14. **Troubleshooting: Check `.htaccess` File**
If files are being downloaded instead of executed, the `.htaccess` file may not be configured correctly. Follow these steps to verify and fix the issue:

1. **Check the Root `.htaccess` File**:
   Ensure the root `.htaccess` file redirects requests to the `public` directory:
   ```apache
   <IfModule mod_rewrite.c>
       RewriteEngine On
       RewriteRule ^(.*)$ public/$1 [L]
   </IfModule>
   ```

2. **Check the Public `.htaccess` File**:
   Ensure the `public/.htaccess` file is configured to handle Laravel routing:
   ```apache
   <IfModule mod_rewrite.c>
       RewriteEngine On
       RewriteCond %{REQUEST_FILENAME} !-d
       RewriteCond %{REQUEST_FILENAME} !-f
       RewriteRule ^ index.php [L]
   </IfModule>
   ```

3. **Enable `mod_rewrite` in Apache**:
   If `mod_rewrite` is not enabled, activate it and restart Apache:
   ```bash
   sudo a2enmod rewrite
   sudo systemctl restart apache2
   ```

4. **Verify Apache Configuration**:
   Ensure the `AllowOverride` directive is set to `All` in your Apache configuration file:
   ```apache
   <Directory /path/to/your/laravel/project/public>
       AllowOverride All
       Require all granted
   </Directory>
   ```

---

## 15. **Verify File Permissions**
Incorrect file permissions can cause issues with file access and execution. Ensure the following permissions are set:

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

## 16. **Check Apache Logs for Errors**
If the application is not working as expected, review the Apache error logs for details:
```bash
sudo tail -f /var/log/apache2/error.log
```

---

## 17. **Verify PHP Version**
Ensure the correct PHP version is being used by creating a `phpinfo.php` file in the `public` directory:
```php
<?php
phpinfo();
```
Access `http://yourdomain.com/phpinfo.php` in your browser to verify the PHP version. Delete the file after verification.

---

## 18. **Check FTP Configuration**
If you encounter issues with FTP, verify the FTP service is running and the port is open:
```bash
# Check if FTP service is running
sudo systemctl status vsftpd

# Check if port 21 is open
sudo netstat -tuln | grep :21
```

---

## 19. **Verify MySQL Connection**
If the application cannot connect to the database, verify the MySQL credentials in the `.env` file and test the connection:
```bash
mysql -u your_database_user -p -h your_database_host -e "USE your_database_name; SHOW TABLES;"
```

---

## 20. **Check Laravel Logs**
If the application throws errors, check the Laravel logs for details:
```bash
tail -f /path/to/your/laravel/project/storage/logs/laravel.log
```

---

## 21. **Verify Email Configuration**
If emails are not being sent, test the email configuration using Laravel's `tinker`:
```bash
php artisan tinker
\Mail::raw('Test email', function ($message) {
    $message->to('test@example.com')->subject('Test Email');
});
```

---

## 22. **Check File Upload Limits**
If file uploads fail, ensure the following settings are updated in both `php.ini` and `.htaccess`:
- `upload_max_filesize`
- `post_max_size`
- `memory_limit`

Example `.htaccess`:
```apache
php_value upload_max_filesize 100M
php_value post_max_size 100M
php_value memory_limit 256M
```
