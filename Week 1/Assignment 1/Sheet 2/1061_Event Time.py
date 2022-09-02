a,d1 = map(str, input().split())
h1,a,m1,a,s1 = map(str, input().split())
a,d2 = map(str, input().split())
h2,a,m2,a,s2 = map(str, input().split())

d1=int(d1)
d2=int(d2)
h1=int(h1)
h2=int(h2)
m1=int(m1)
m2=int(m2)
s1=int(s1)
s2=int(s2)

s = s2 - s1
m = m2 - m1
h = h2 - h1
d = d2 - d1

if s<0:
	s+=60
	m-=1

if m<0:
	m+=60
	h-=1

if h<0:
	h+=24
	d-=1

print("{} dia(s)".format(d))
print("{} hora(s)".format(h))
print("{} minuto(s)".format(m))
print("{} segundo(s)".format(s))