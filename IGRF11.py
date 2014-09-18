f=open('/media/SOCRATES/Python27/mystuff/IGRF11.COF','r')

def get_the_title_info(alist):
	blist=[]
	i=0
	for elem in alist:
		if elem != '':
			blist.append(elem)
			i=i+1
		if i == 3:
			break
	year=int(float(blist[1]))
	level=int(float(blist[2]))
	return (year,level)


def get_the_coefficient(alist):
	blist=[]
	i=0
	for elem in alist:
		if elem != '':
			blist.append(float(elem))
			i=i+1
		if i == 4:
			break
	n=int(blist[0])
	m=int(blist[1])
	g=blist[2]
	h=blist[3]
	return [(n,m),(g,h)]


all_the_coefficient={}	
all_the_level={}	
while True:
	alist=f.readline().split(' ')
	if alist == ['']:break
	key=get_the_title_info(alist)
	all_the_coefficient[key[0]]={}
	all_the_level[key[0]]=key[1]
	effnum=key[1]*(key[1]+3)/2
	for i in range(effnum):
		alist=f.readline().split(' ')
		templist=get_the_coefficient(alist)
		all_the_coefficient[key[0]][templist[0]]=templist[1]

f.close()



year=int(raw_input("the year:"))
try:
	print all_the_level[year]
except KeyError:
	print 'no that year!'
n=int(raw_input("the n:"))
m=int(raw_input("the m:"))
try:
	print all_the_coefficient[year][(n,m)]
except KeyError:
	print 'no that level!'
	return
