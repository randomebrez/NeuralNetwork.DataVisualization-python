import sqlite3
from sqlite3 import Error

dbConnection = None
initialized = False


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    global dbConnection
    global initialized
    try:
        dbConnection = sqlite3.connect(db_file)
        initialized = True
    except Error as e:
        print(e)


def is_initialized():
    if not initialized:
        print("You must first call 'create_connection' method to initialize the database connection")

    return initialized


def get_last_units(batch_size=100):
    if not is_initialized():
        return

    cursor = dbConnection.cursor()
    cursor.execute("SELECT * FROM units ORDER BY unit_id desc limit {0}".format(batch_size))

    rows = cursor.fetchall()

    return rows

def get_generations(simulationIndex):
    if not is_initialized():
        return

    cursor = dbConnection.cursor()
    cursor.execute("select distinct generation_id from units where simulation_id = {0}".format(simulationIndex))

    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(row[0])

    return result


def get_unit_steps_for_generation(simulationIndex, generationId):
    if not is_initialized():
        return

    result = {}
    cursor = dbConnection.cursor()
    cursor.execute("select distinct unit_id from units where generation_id = {0} and simulation_id = {1}".format(generationId, simulationIndex))
    unitIds = cursor.fetchall()
    sqlRequest = ""
    for unitId in unitIds:
        result[unitId[0]] = []
        sqlRequest += "{0},".format(unitId[0])

    sqlRequest = sqlRequest[:-1]
    cursor.execute("select * from unit_steps where unit_id in ({0})".format(sqlRequest))
    steps = cursor.fetchall()
    for step in steps:
        if (len(step) <= 1):
            print(step)
        result[step[1]].append(step)
    return result

def get_unit_steps(unitId):
    if not is_initialized():
        return

    cursor = dbConnection.cursor()
    cursor.execute("SELECT * FROM unit_steps where unit_id = {0}".format(unitId))

    rows = cursor.fetchall()

    return rows

def get_last_simulation():
    if not is_initialized():
        return

    cursor = dbConnection.cursor()
    cursor.execute("select simulation_id from simulations order by simulation_id desc limit 1")
    row = cursor.fetchall()

    return row[0][0]
