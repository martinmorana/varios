#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd 
systemctl enable httpd
echo "<html><body>Esto es un server web </body></html> >> /var/www/html/index.html
