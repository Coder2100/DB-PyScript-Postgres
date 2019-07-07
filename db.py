#!/usr/bin/python
import psycopg2
import sys
 
def main():
	#Define our connection string
	#I USED ROOT USER SO YOUR PASSWORD MIGHT BE THE SUDO PASSWORD AS ME OR OTHERWISE
	conn_string = "host='localhost' dbname='flights' user='apexcure' password='#'"
 
	# print the connection string we will use to connect
	print("Connecting to database\n	->%s" % (conn_string))
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print("Connected!\n")
	cursor.execute("SELECT id, origin, destination, duration FROM flights")#.
	flights = cursor.fetchall()
	print("\nShow me the databases:\n")
	for flight in flights:
		#print( "   ", flight[0], flight[1],flight[2], flight[3])
		print(f"Flight {flight[0]}: {flight[1]} to {flight[2]}, {flight[3]} minutes.")

if __name__ == "__main__":
	main()
