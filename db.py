import mysql.connector



mydb = mysql.connector.connect(
  host="3306",
  user='root',
  password='Rjchauhan@18',
  database="bank"
)

print(mydb)
mycursor = mydb.cursor(dictionary=True)
print("connection done")



# mycursor.execute("CREATE TABLE GTU_NOTOFICATION (id INT AUTO_INCREMENT PRIMARY KEY,Date DATE,notification VARCHAR(255), link VARCHAR(255))")
def insert_notification(notification,link):

    sql = "INSERT INTO GTU_NOTOFICATION (notification, link) VALUES ( %s,%s)"
    val = (notification,link)
    mycursor.execute(sql, val)
    mydb.commit()
# insert_notification('notification3','link3')

def last_notification():
    mycursor.execute("SELECT * FROM GTU_NOTOFICATION ORDER BY id desc limit 1")

    myresult = mycursor.fetchone()
    myresult['link']
    return myresult['link']


