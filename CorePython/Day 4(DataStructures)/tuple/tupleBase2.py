addr="monthly@python.org"
uname,domain=addr.split('@')
print(type(addr))

print(uname)
print(domain)
tup=uname,domain
print(type(tup))


quot,rem=divmod(7,3)
print(type(quot),type(rem))
print(quot)
print(rem)