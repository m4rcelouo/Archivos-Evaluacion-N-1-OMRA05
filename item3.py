aclnum = int (input("Cual es el numero IPv4 ACL "))
if aclnum >= 1 and aclnum <99:
	print("Este es un ACL IPv4 estandar.")
elif aclnum >=100 and aclnum <= 199:
	print("Este es un ACL IPv4 extendida.")
else:
	print("Esta ACL IPv4 no es extendida o estandar")