# Dharma Bot Iteration 1

This bot logs discord message activities into a database to keep track of  
user activity.  
The data can be accessed via a simple website.


# Quickstart

## System Requirements:

- Python 3.6 or newer!
- A local mysql database needs to be running:
  - Change the class [MysqlConfiguration](./mysql_interface/mysql_constants.py) according to your systems configuration!


To install python package requirements, please run the following command:

```sh
pip install -r requirements.txt
```

## First startup:
You need to create a file named "botToken.py" inside the root folder of this project via the following scheme:
```py
# Insert your discord bot token.
token = ''
```


# TODO

General (Feature Complete):
- Create mapping for custom commands
- Log every message directly into the database
- update user/server database accordingly

Nice to have:
- Being able to change the prefix of commands
