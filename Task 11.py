a = input()
b = a.find('h')
c = a.rfind('h')
d = a[b+1:c]
e = d.replace('h','H')
print(a[:b+1],e,a[c:], sep = '' )
