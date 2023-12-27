import MySQLdb

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'justice',
    'passwd': 'jaycode-233',
    'db': 'PDTEST4',
}

# Create a connection to the database
conn = MySQLdb.connect(**db_config)
