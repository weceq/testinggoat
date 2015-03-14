Provisioning a new site
=======================

## Required packages

* nginx
* Python 3
* git
* pip
* virtualenv

eg, on Debian:
    sudo apt-get install nginx git python3 python3-pip
    sudo pip install virtualenv

## Nginx virtual host config

* see nginx.template.conf
* replace SITENAME with your domain name, eg. staging.my-domain.com

## Systemd service

* see gunicorn.template.service
* replace SITENAME with your domain name, eg. staging.my-domain.com

## Folder structure

Assume we have a user account at /home/username

/home/dawid/www
└── SITENAME
    ├── database
    ├── source
    ├── static
    └── virtualenv

5 directories, 0 files
