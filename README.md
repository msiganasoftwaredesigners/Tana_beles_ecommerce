Msigana ecommerce

"
i have done three step can you show me the next spte please"
i have done the first two step"Yes, I understood that you are deploying your Django application on a DigitalOcean droplet. The instructions provided are intended for a Ubuntu-based droplet on DigitalOcean. 

Here's a brief overview of the steps:

1. **SSH into your DigitalOcean droplet.**
2. **Update your server and install necessary packages including Python, pip, venv, git, and PostgreSQL.**
3. **Clone your Django project onto the droplet and set up a Python virtual environment.**
4. **Install your project's dependencies using pip.**
5. **Set up your PostgreSQL database.**
6. **Configure your Django project for production.**
7. **Install and test Gunicorn, a Python WSGI HTTP Server.**
8. **Install and configure Nginx as a reverse proxy for Gunicorn.**
9. **Set up a Gunicorn systemd service to ensure that Gunicorn automatically starts on boot.**
10. **Finalize your Nginx configuration to communicate with Gunicorn via Unix sockets.**

Please follow the detailed steps provided in the previous responses. If you encounter any issues, feel free to ask for further assistance."
can you show me the next step"
" can show me step by setp of number five 


# SSH keya authentication

## Generate ssh key

```
ssh-keygen
```

## get ssh key to server

```

cat ~/.ssh/id_rsa.pub

```

# to connect digital ocean to local terminal 

```

ssh root@your_droplet_ip (143.244.179.85)

```


## clone the projecct 

```
cd var/www 
```

```
git clone git@github.com:msiganasoftwaredesigners/Tana_beles_ecommerce.git

```

```
python3 -m venv venv
```

```
pip install -r requirements.txt
```

# DATABASE CONFIGURATION

```
sudo apt-get install postgresql postgresql-contrib
```

```
sudo -u postgres psql
```

```
CREATE DATABASE tanabeles;
```

```
ALTER USER your_username WITH PASSWORD 'new_password';
```

```
ALTER USER postgres PASSWORD 'new_password';
```

```
GRANT ALL PRIVILEGES ON DATABASE your_database TO your_username;
```

```
sudo -u postgres psql -c "SHOW hba_file;"
```

```
sudo nano /etc/postgresql/versionofpostgres/main/pg_hba.conf
```

```
# TYPE  DATABASE        USER            ADDRESS                 METHOD
local   all             postgres                                peer to md5




```
sudo service postgresql restart
```

```
psql -U postgres -h localhost -d storage/development_postgres
````

```
python manage.py collectstatic
```

```
python manage.py migrate    