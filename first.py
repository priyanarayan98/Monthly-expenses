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

data = {"Name": "Priya", "Rent":300, "Power Bill":10, "Groceries": 70}

# database.child("Users").child("FirstPerson").set(data)

priya = database.child("Users").child("FirstPerson").get()
d = priya.val()
sum = 0 
categories = ["Rent","Power Bill","Groceries"]

for i in categories:
    if i in d:
        sum += d[i]
print("Total Monthly Expenses is",sum)

database.child("Users").child("FirstPerson").update({"Total expenses":sum})