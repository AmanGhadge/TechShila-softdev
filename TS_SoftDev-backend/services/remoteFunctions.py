import environ
import psycopg2


env = environ.Env(
    DEBUG=(bool, False)
)

# reading .env file
environ.Env.read_env()

con = psycopg2.connect(database=env('POSTGRES_DB'), user=env('POSTGRES_USER'), password=env('POSTGRES_PASSWORD'), host=env('POSTGRES_HOST'), port=env('POSTGRES_PORT'))
cur = con.cursor()


# check if table exist else create

def tableCheck():
    cur.execute(
        "select exists(select * from information_schema.tables where table_name=%s)", ('commands',))
    if not cur.fetchone()[0]:
        cur.execute('''CREATE TABLE commands
                        (id TEXT PRIMARY KEY     NOT NULL,
                        passcode TEXT NOT NULL,
                        one         TEXT   NOT NULL,
                        two         TEXT   NOT NULL,
                        three       TEXT   NOT NULL,
                        four        TEXT   NOT NULL,
                        five        TEXT   NOT NULL,
                        uidLatest   TEXT   NOT NULL);''')
        con.commit()


def tableCheck_for_response():
    cur.execute(
        "select exists(select * from information_schema.tables where table_name=%s)", ('responses',))
    if not cur.fetchone()[0]:
        cur.execute('''CREATE TABLE responses
                        (id    TEXT  NOT NULL,
                        passcode TEXT  NOT NULL,
                        command  TEXT  NOT NULL,
                        response       TEXT   NOT NULL,
                        uid         TEXT   NOT NULL);''')
        con.commit()

# app creates a session id and user creates a passcode

def createSession(id, passcode):
    try:
        tableCheck()
        cur.execute(str("INSERT INTO commands (id,passcode,one,two,three,four,five,uidLatest) VALUES (\'" +
                        str(id)+"\', \'"+str(passcode)+"\','','', '','','', '')"))
        con.commit()
    except:
        print('user exist,overwriting')
        con.rollback()

# take 'command' and every ith command is pushed to i+1,and command is placed in i=0.Last command removed. Returns command List then.

def setCommand(id, passcode, command, uidLatest):
    createSession(id, passcode)
    commandsGet = commandList(id, passcode)
    # case of get
    if command == '':
        return commandsGet[2:]
    # case of set if no uidLatest
    if uidLatest == '':
        return commandsGet[2:]
    # else
    count = 0
    # store current commands
    current = command
    # to commonds to be returned
    final = []
    # shift all comands by 1.
    for t in commandsGet:
        if count >= 2:
            final.append(current)
            current = t
        count = count+1
    # set these in DB
    nos = ['one', 'two', 'three', 'four', 'five']
    for t, r in zip(final, nos):
        cur.execute(str("UPDATE commands set "+r +
                        " = \'"+t+"\' where id=\'"+id+"\'"))
        con.commit()
    cur.execute(str("UPDATE commands set "+"uidLatest" +
                    " = \'"+uidLatest+"\' where id=\'"+id+"\'"))
    con.commit()
    return final

# get command list -> client calls function

def commandList(id, passcode):
    cur.execute(str(
        "SELECT id,passcode,one,two,three,four,five,uidLatest from commands where id=\'"+id+"\'"))
    rows = cur.fetchall()
    commands = []
    for r in rows:
        for t in r:
            commands.append(t)
    print(commands)
    con.commit()
    return commands

def checkUser(id,passcode):
    cur.execute(str("SELECT id,passcode from commands where id=\'" + \
            id+"\' AND passcode=\'"+passcode+"\'"))
    row=cur.fetchall()
    command = []
    for r in row:
        for t in r:
            command.append(t)
    con.commit()
    return command

# to close cursor
def close():
    con.close()
    
# to send list of uids after and including the current uid

def list_uids(responses, uid):
    keys_list = list(responses)
    for i in range(len(keys_list)):
        if keys_list[i] == uid:
            return keys_list[i:]

# returns nothing but recieves a responses and saves it.

def saveResponse(id, passcode, command, response, uid):
    # create table if not exists then storing the respone in it
    tableCheck_for_response()
    cur.execute(str("INSERT INTO responses (id,passcode,command,response,uid) VALUES (\'"+str(id) +
                    "\',\'"+str(passcode)+"\',\'"+str(command)+"\',\'"+str(response)+"\', \'"+str(uid)+"\')"))
    con.commit()

# Recieves a uid, returns response list(of uids after that uid) else just latest response (along with the commands and uid).

def returnResponses(id, passcode, uid):
    cur.execute(str("SELECT uid,response from responses where id=\'" +
                    id+"\' AND passcode=\'"+passcode+"\'"))
    rows = cur.fetchall()
    responses = []
    for r in rows:
        for t in r:
            responses.append(t)
    uids = list_uids(responses, uid)
    if uids:
        t = tuple(uids)
        query = "SELECT uid,response,command from responses where id=\'" +\
            id+"\' AND passcode=\'"+passcode+"\' AND uid IN{}".format(t)
        cur.execute(query)
        rowss = cur.fetchall()
        responsess = []
        for r in rowss:
            for t in r:
                responsess.append(t)
        con.commit()
        return responsess
    else:
        return []



