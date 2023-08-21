# Teaching Website

This project was part of my graduation project at Southwest University, and also part of the COMPSCI 780 project at the University of Auckland. It's a teaching website built on Django, specifically tailored for Introduction to Computer Science course. To get started using the site, you can log in with the username `admin` and password `password`.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.6.8 or higher
- Git

### Clone the Repository

First, you'll need to clone the repository. Open your command line or terminal and run:

```bash
git clone https://github.com/slin648/TeachingSite.git
```

### Change Directory

```bash
cd TeachingSite
```

### Run the Website

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Then open the browser and go to localhost:8000, and you should see the website running.


## Server Deployment Guide

This guide is for deploying the project on a CentOS SELinux 8 x64 system.

### SSH Key Reset (if the IP has changed)

```bash
ssh-keygen -R +[SERVER_IP]
```

### Logging into Host

```bash
ssh root@[SERVER_IP]
```

### Preinstalled System Requirements

- Python 3.6.8
- SQLite version 3.26.0

### Creating Virtual Environment

```bash
pip3 install virtualenv
virtualenv djangoenv
source ~/djangoenv/bin/activate
```

### Installing Required Packages

```bash
pip install django==3.1.7
pip install django-widget-tweaks
pip install Pillow
```

### File Transfer and Unzipping

- Zip the project directory on your local machine
- Send the `teachingsite.zip` file to `/root`
- Unzip the file

  ```bash
  unzip -o -d /root/tsite teachingsite.zip
  ```

### Firewall Configuration

```bash
sudo firewall-cmd --zone=public --permanent --add-port=8000/tcp
sudo firewall-cmd --reload
```

### Running the Website

Navigate to the project directory and execute the following:

```bash
cd tsite
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:80
```

Note: This allows external access. If you don't specify the IP and port, it will only be accessible locally.

### Running the Website After Disconnecting from SSH

1. Install `screen`

   ```bash
   sudo yum install epel-release
   sudo yum install screen
   ```

2. Create a screen session

   ```bash
   screen -S website
   ```

3. You can now run the site and then close the SSH remote connection window. To return, log in again and:

   ```bash
   screen -r website
   ```

### Other Screen Commands

- `Ctrl a+d`: Detach from current session temporarily
- `screen -ls`: List all screen sessions
- `exit`: Exit screen
- `screen -wipe website`: Delete session
