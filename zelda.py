import os
import urllib.request

BASE_URL = 'https://zeldamaps.com/tiles/botw/hyrule/'

output_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'zelda')

for i in range(0, 20):
	for j in range(0, 20):
		filename = '4_' + str(i) + '_' + str(j) + '.png'
		os.system('wget -q --max-redirect 0 -O {0} {1}'.format(os.path.join(output_dir, filename), BASE_URL + filename))