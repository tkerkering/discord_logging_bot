import mysql_interface.mapping as mapping


class MysqlConfiguration():
    host = "localhost"
    user = "root"
    password = ""
    port = "3306"


def __get_base_database_uri():
    # Base Database Uri that all other uris will format
    return 'mysql+mysqlconnector://' + \
           MysqlConfiguration.user + ':' + \
           MysqlConfiguration.password + '@' + \
           MysqlConfiguration.host + ':' + \
           MysqlConfiguration.port + '/{database}'


def create_database_uri_by_string(name): return __get_base_database_uri().format(
    database=name)
