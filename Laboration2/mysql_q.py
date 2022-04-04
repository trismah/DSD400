import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.8.128",
    user="python",
    password="passwd",
    database="testdb"
)
try:
    with mydb.cursor() as mycursor:
        who = input("> ")
        main = "SELECT unit, startdate, stopdate FROM reservations WHERE account = (SELECT user_id FROM users WHERE username =%s)"
        mycursor.execute(main, (who,))
        
        result = mycursor.fetchall()
        if result:
            for (unit, startdate, stopdate) in result:            
                print(f"The {unit} is reserved from {startdate} to {stopdate} by {who}")
        else:
            print(f"No reservations for {who}.")
except Exception as e:
    print(e)
