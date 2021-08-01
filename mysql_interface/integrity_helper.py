import logging
import sqlalchemy as sqlAlchemy
import sqlalchemy_utils as sqlUtils
import mysql_interface.mapping as mysqlMapping
import mysql_interface.mysql_constants as mysqlConstants

logger = logging.getLogger('discord')


def __create_table(engine, table):
    metadata = sqlAlchemy.MetaData()
    mysqlMapping.get_model_by_name(table, metadata)
    metadata.create_all(engine)
    logger.info("Created " + table)


def create_database_if_not_exists(uri):
    if not sqlUtils.database_exists(uri):
        logger.info("Couldn't find " + uri + " database, creating it now.")
        sqlUtils.create_database(uri)
        logger.info("Created database at " + uri)
    else:
        logger.info("Found database at " + uri)


def get_database_connection():
    try:
        # Check connection to database
        logger.info("Connection to mysql server..")
        engine = sqlAlchemy.create_engine(
            mysqlConstants.create_database_uri_by_string(""))
        engine.connect()
        logger.info("Successfully connected to mysql server at " +
                    mysqlConstants.MysqlConfiguration.host + ":" + mysqlConstants.MysqlConfiguration.port)
        return True
    except:
        logger.fatal("Couldn't connect to mysql server at " +
                     mysqlConstants.create_database_uri_by_string(""))
        logger.fatal("Is MysqlConnector installed on client?")
        return False


def check_if_table_exists_on_db(engine, tableName):
    tableQuery = engine.execute('SHOW TABLES')
    tables = tableQuery.fetchall()
    for table in tables:
        if table._data[0] == tableName:
            logger.info("Successfully found " + tableName +
                        " table at above mentioned database")
            return
    logger.warn("Couldn't find " + tableName)
    logger.info("Creating it now..")
    __create_table(engine, tableName)
