import sqlalchemy as sqlAlchemy
import sqlalchemy_utils.types.url

# Table names
messageLogTableName = "message_log"
userTableName = "user_mapping"
serverTableName = "server_mapping"

# Table List
tables = [messageLogTableName, userTableName, serverTableName]


def __message_log_table(metadata):
    return sqlAlchemy.Table(messageLogTableName, metadata,
                            sqlAlchemy.Column(
                                'Discord_Message_Id', sqlAlchemy.Integer, primary_key=True, autoincrement=True),
                            sqlAlchemy.Column(
                                'SendTime', sqlAlchemy.DateTime, nullable=False),
                            sqlAlchemy.Column(
                                'ReplyTime', sqlAlchemy.DateTime, nullable=False),
                            sqlAlchemy.Column(
                                'Request', sqlalchemy_utils.types.url.URLType, nullable=False),
                            sqlAlchemy.Column(
                                'Reply', sqlAlchemy.Text, nullable=False)
                            )


def __user_table(metadata):
    return sqlAlchemy.Table(userTableName, metadata,
                            sqlAlchemy.Column(
                                'Discord_User_Id', sqlAlchemy.Integer, primary_key=True),
                            sqlAlchemy.Column(
                                'Username', sqlalchemy_utils.types.url.URLType, nullable=False)
                            )


def __server_table(metadata):
    return sqlAlchemy.Table(serverTableName, metadata,
                            sqlAlchemy.Column(
                                'Discord_Server_Id', sqlAlchemy.Integer, primary_key=True),
                            sqlAlchemy.Column(
                                'Server_Name', sqlalchemy_utils.types.url.URLType, nullable=False)
                            )


def get_model_by_name(name, metadata):
    model_switcher = {
        messageLogTableName: __message_log_table,
        userTableName: __user_table,
        serverTableName: __server_table
    }
    switcherFunction = model_switcher.get(name)
    switcherFunction(metadata)
