#pip install git+https://github.+com/ozgur/python-firebase
#import firebase
from firebase import firebase
#Connect to to database
firebase = firebase.FirebaseApplication('Database URL', None)

#create a dictionary of account data
account_data={
  1340005:["John","Rs.9000",8112],
  1340006:["Maria","Rs.7000",6789],
  1340007:["Daniel","Rs.500",8907],
  1340008:["Jack","Rs.5000",7896],
  1340009:["Ria","Rs.700",8903]}


#Create variable for "name" that holds the value "bank"
name="Bank"
#Assign "account_data" to a variable "data"
data=account_data
#Upload data to firebase
firebase.put("",name,data)


