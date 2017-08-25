#!/usr/bin/env python

# '' is the same "" but, for order and unification, you should use one type of them. 

server_name = "Hektor"
server_type = 'cygwin'

print server_name 
server_type

server_desc = """ My laboratory test server
at Home laboratory """

print "My server name: %s" % (server_name)
print "Full server's description is: %s" % (server_desc)

len(server_desc)

server_desc = "Server " + server_name + " is running " + server_type
print server_desc

server_desc = " ".join(("Server", server_name, "is running", server_type))
print server_desc

print "cygwin" in server_type
print "debian" in server_desc

print server_desc[0:4]
print server_desc[:3]
print server_desc[4:]

print server_desc[server_desc.find("is"):]

server_desc = server_desc.replace('cygwin','Debian')
print server_desc
print server_desc.find('Debian')
print server_desc[server_desc.find('Debian'):]

