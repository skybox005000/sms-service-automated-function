import os
import sqlite3

# Connect to a new database
conn = sqlite3.connect(os.getenv("CLIENT_INFORMATION_DB"))

# Close the connection
conn.close()