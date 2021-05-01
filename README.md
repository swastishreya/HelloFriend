# HelloFriend

> REST API created using Django and Neo4j.

## Build Setup

``` bash
# Create virtual environement
pip install virtualenv
virtualenv env
env\Scripts\activate

# Install requirements
pip install -r requirements.txt

# For adding new requirements 
pip freeze > requirements.txt

# Create constraints
python manage.py install_labels 

# Run api server
python manage.py runserver [host-server-ip:host-server-port]

# Run Django shell 
python manage.py shell
```
