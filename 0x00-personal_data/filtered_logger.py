#!/usr/bin/env python3
"""
filtered_logger.py
Task 0: Regex-int
"""
import re
import os
import mysql.connector
import logging
from typing import List

patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """Task 0
    """
    extract, replace = (patterns['extract'], patterns['replace'])
    return re.sub(extract(
        map(re.escape, fields), re.escape(separator)
        ), replace(redaction), message)


def get_logger() -> logging.Logger:
    """Get log
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Get Database
    """
    db_username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "")

    connection = mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        port=3306,
        database=db_name,
    )

    return connection


def main():
    # Set up logger
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Get database connection
    db = get_db()

    # Retrieve all rows in the users table
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Display each row under a filtered format
    for row in rows:
        filtered_data = {
            'name': '***',
            'email': '***',
            'phone': '***',
            'ssn': '***',
            'password': '***',
        }

        # Log the filtered data
        logger.info(f"{filtered_data}; ip={row['ip']}; last_login={row['last_login']}; user_agent={row['user_agent']}")

    # Close database connection
    cursor.close()
    db.close()


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Class constructor
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


if __name__ == "__main__":
    main()