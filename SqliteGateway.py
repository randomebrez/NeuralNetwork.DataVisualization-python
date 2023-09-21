import sqlite3
from sqlite3 import Error

dbConnection = None
initialized = False

# Initialization test
def is_initialized():
    if not initialized:
        print("You must first call 'create_connection' method to initialize the database connection")

    return initialized

# Db connexion creation
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

# Methods
def get_simulation_default_last(simulationId = 0):
    if not is_initialized():
        return

    string = "select * from simulations order by simulation_id desc limit 1"
    if simulationId != 0:
        string = "select * from simulations where simulation_id = {0}".format(simulationId)

    cursor = dbConnection.cursor()
    cursor.execute(string)
    row = cursor.fetchall()

    return row[0]

def get_generation_ids_for_simulation(simulationIndex):
    if not is_initialized():
        return

    result = []
    cursor = dbConnection.cursor()
    cursor.execute("select distinct generation_id from units where simulation_id = {0}".format(simulationIndex))
    genrationIds = cursor.fetchall()

    for generationId in genrationIds:
        result.append(generationId[0])

    return result

def get_generation_results(simulationIndex):
    if not is_initialized():
        return

    cursor = dbConnection.cursor()
    cursor.execute("select * from generation_results where simulation_id = {0}".format(simulationIndex))
    return cursor.fetchall()

def get_unit_steps_for_generation(simulationIndex, generationId):
    if not is_initialized():
        return

    result = {}
    cursor = dbConnection.cursor()
    # Fetch unit identifiers for this generation
    cursor.execute("select distinct unit_identifier from units where generation_id = {0} and simulation_id = {1}".format(generationId, simulationIndex))
    unitIds = cursor.fetchall()

    sqlRequestFilter = ""
    for unitId in unitIds:
        result[unitId[0]] = []
        sqlRequestFilter += "'{0}',".format(unitId[0])
    sqlRequestFilter = sqlRequestFilter[:-1]

    #Fetch unit steps for unit identifiers above
    cursor.execute("select * from unit_steps where unit_identifier in ({0})".format(sqlRequestFilter))
    steps = cursor.fetchall()

    for step in steps:
        result[step[1]].append(step)

    return result


def get_unit_steps_for_unit(unitId):
    if not is_initialized():
        return

    cursor = dbConnection.cursor()
    cursor.execute("SELECT * FROM unit_steps where unit_id = {0}".format(unitId))

    rows = cursor.fetchall()

    return rows
