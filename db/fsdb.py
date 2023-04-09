from sqlalchemy import URL, create_engine

# This file will include db core helper methods
# fsdb.select, delete, insert, etc.
# Each of these will open a connection and execute the SQL with preparements


def init():
    url_object = URL.create(
        "postgresql",
        username="username",
        password="password",
        host="localhost?",
        database="fsdb"
    )
    # These values will come once from Azure Key Vault
    engine = create_engine(url_object)
    
    return engine
