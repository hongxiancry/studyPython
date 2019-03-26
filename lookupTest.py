def init(data):
	data['first']={}
	data['middle'] = {}
	data['last'] = {}
def lookup(data,label,name):
	return data[label].get(name)

def store(data,full_name):
	names = full_name.split()
	if len(names)==2:
		names.insert(1,'')
	labels = ['first','middle','last']
	for label,name in zip(labels,names):
		people = lookup(data,label,name)
		if people:
			people.append(full_name)
		else:
			data[label][name] = [full_name]
my_store_names = {}
init(my_store_names)
store(my_store_names,'lis di diong')
store(my_store_names,'lis ddddd')
print(my_store_names)
result = lookup(my_store_names,'middle','di')
print('result:',result)