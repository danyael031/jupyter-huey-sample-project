from huey import SqliteHuey


# Huey supports multiple types of brokers, including network brokers like Redis.
# For this sample project, we use SQLite as broker.
huey = SqliteHuey(filename="./broker/queuebroker.db")
