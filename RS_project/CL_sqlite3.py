# Allow users to ececute SQL commands for python-sqlitee3 white the execute()
# fuction


import sqlite3
database = raw_input('Enter the name of db with name.db\n')
conn = sqlite3.connect(database)#(":memory:")
conn.isol
ation_level = None
cur = conn.cursor()


buffer =""

print "Enter your SQL commands to Execute sqlite3"
print "Enter a blank line to exit."

while True:
    line =  raw_input()
    if line == "":
        break
    buffer = buffer + line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print cur.fetchall()
        except sqlite3.Error, e:
            print "An error occured: ", e.args[0]
        buffer = ""
con.close()

            
