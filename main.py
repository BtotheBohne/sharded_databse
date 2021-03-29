import mysql.connector

mydb = mysql.connector.connect(
  host="10.0.0.20",
  user="maxuser",
  password="maxpwd",
  port="4006"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM zipcodes_one.zipcodes_one WHERE  Zipcode=(SELECT MAX(Zipcode) FROM zipcodes_one.zipcodes_one)")
print("The largest Zipcode from zipcodes_one is:")
for i in mycursor:
    print(i)
print("")

mycursor.execute("SELECT * FROM zipcodes_two.zipcodes_two WHERE Zipcode=(SELECT MIN(Zipcode) FROM zipcodes_two.zipcodes_two)")
print("The smallest Zipcode from zipcodes_two is:")
for i in mycursor:
    print(i)

print("")

mycursor.execute("SELECT * FROM zipcodes_two.zipcodes_two ORDER BY Zipcode LIMIT 10")
print("The Smallest 10 zipcodes from zipcodes_two are:")
for i in mycursor:
    print(i)

print('')

mycursor.execute("SELECT * FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 10")
print("The Largest 10 zipcodes from zipcodes_one are:")
for i in mycursor:
    print(i)