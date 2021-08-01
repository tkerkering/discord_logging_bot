import discord
import logging
import botToken
import sqlalchemy as sqlAlchemy
import mysql_interface.integrity_helper as integrityHelper
import mysql_interface.mysql_constants as mysqlConstants
import mysql_interface.mapping as mysqlMapping


# Logging initialization
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)


def verify_database_integrity():
    # If no database found, exit
    if not integrityHelper.get_database_connection():
        exit()

    # Create all relevant databases
    for table in mysqlMapping.tables:
        databaseUri = mysqlConstants.create_database_uri_by_string(table)
        integrityHelper.create_database_if_not_exists(databaseUri)


# Check database integrity before starting the bot
verify_database_integrity()
messageEngine = sqlAlchemy.create_engine(
    mysqlConstants.create_database_uri_by_string(mysqlMapping.messageLogTableName))
messageEngine.connect()
integrityHelper.check_if_table_exists_on_db(
    messageEngine, mysqlMapping.messageLogTableName)

userEngine = sqlAlchemy.create_engine(
    mysqlConstants.create_database_uri_by_string(mysqlMapping.userTableName))
userEngine.connect()
integrityHelper.check_if_table_exists_on_db(
    messageEngine, mysqlMapping.userTableName)

serverEngine = sqlAlchemy.create_engine(
    mysqlConstants.create_database_uri_by_string(mysqlMapping.serverTableName))
serverEngine.connect()
integrityHelper.check_if_table_exists_on_db(
    messageEngine, mysqlMapping.serverTableName)


# Create discord client and register on events
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as "{0.user}"'.format(client))


@client.event
async def on_message(message):
    # All messages run into this function
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(botToken.token)
