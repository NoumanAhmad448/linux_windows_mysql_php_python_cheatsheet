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

### Step 7: Verify Domain Connection
1. **Check Hostname**:
   ```bash
   hostname
   ```
2. **Test Website**: Open your web browser and navigate to your domain to ensure it loads correctly.


