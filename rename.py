import os, sys, string, random
def id_generator(size = 10, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
path = '''SOME PATH'''
pathout = '''SOME PATH'''
helptext = 'Missing argument\n1. All random\n2. Specific prefix (prefix, start)\n3. Random prefix (start)'

if len(sys.argv) < 2:
	print(helptext)
	exit(0)

files = os.listdir(path)

# for all random names
if sys.argv[1] == '1':
	for filename in files:
		curr_name = id_generator()
		if ( not os.path.isfile( curr_name + filename[-4:] ) ):
			os.rename(path+'\\'+filename, curr_name+filename[-4:])

# for specific prefix
if sys.argv[1] == '2':
	if len(sys.argv) != 4:
		print('Need 3 arguments for specific prefix')
		print(helptext)
		exit(0)
	for filename in files:
		os.rename(path+'\\'+filename, sys.argv[2] + filename[int(sys.argv[3]):])

# for random prefix
if sys.argv[1] == '3':
	if len(sys.argv) != 3:
		print('Need 2 arguments for specific prefix')
		print(helptext)
		exit(0)
	curr_name = id_generator()
	for filename in os.listdir(pathout):
		if filename.startswith(curr_name):
			print('prefix already exists')
			break
	else:
		for filename in files:
			os.rename(path+'\\'+filename, curr_name + '_' +filename[int(sys.argv[2]):])
