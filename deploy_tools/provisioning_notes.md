Provisioning a new site
=======================

## Required packages

* nginx
* Python 3
* git
* pip
* virtualenv

eg, on Debian:
    ```
    sudo apt-get install nginx git python3 python3-pip
    sudo pip install virtualenv
    ```

## Nginx virtual host config

* see nginx.template.conf
* replace SITENAME with your domain name, eg. staging.my-domain.com

## Systemd service

* see gunicorn.template.service, gunicorn.template.socket
  and gunicorn.template.conf
* replace SITENAME with your domain name, eg. staging.my-domain.com
* replace USERNAME with your user that will start gunicorn
* replace GROUPNAME with your user's group that will start gunicorn
* rename the files, replacing `template` with domain name (SITENAME value)

## Automatically preparing config files

For automatic preparation of config files use `initial_deploy.sh` script:

```
initial_deploy.sh <sitename> <username> <groupname>
```

## Folder structure

Assume we have a user account at /home/USERNAME

/home/USERNAME/www
└── SITENAME
    ├── database
    ├── source
    ├── static
    └── virtualenv

## Deploy

Use provided Fabric script, eg:

    ```
    cd deploy_tools
    fab deploy:host=username@staging.my-domain.com
    ```

