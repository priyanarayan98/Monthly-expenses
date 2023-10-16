import pyrebase

conf = {
   "apiKey": "AIzaSyBEdvlOtmVVGt32OEgY_iKVcJlrfb4LN8o",
  "authDomain": "weeklyexpenses-dc10c.firebaseapp.com",
  "databaseURL": "https://weeklyexpenses-dc10c-default-rtdb.firebaseio.com",
  "projectId": "weeklyexpenses-dc10c",
  "storageBucket": "weeklyexpenses-dc10c.appspot.com",
  "messagingSenderId": "470370758215",
  "appId": "1:470370758215:web:8518887ca3611cdbf48b62",
  "measurementId": "G-WCS2H9RGH4"
}

firebase = pyrebase.initialize_app(conf)
database = firebase.database()

#Asking the user to enter the name of the person along with the expenses he made during this month.
n = int(input("Enter number of Users:"))
for i in range(n):
  Name = input("Enter a name of a person:")
  Rent = int(input("Enter rent he spent for particular month:"))
  Power_Bill = int(input("Enter power bill of a person:"))
  Groceries = int(input("Enter how much money he spent for groceries:"))
  data = {"Name":Name, "Rent":Rent, "Power Bill": Power_Bill, "Groceries": Groceries}
  database.child("Users").set(data)
  priya = database.child("Users").get()
  d = priya.val()
  sum = 0 
  categories = ["Rent","Power Bill","Groceries"]

  for i in categories:
      if i in d:
        sum += d[i]
  print("Total Monthly Expenses is",sum)
  database.child("Users").update({"Total expenses":sum})
