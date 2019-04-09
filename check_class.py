from bs4 import BeautifulSoup
import requests
import re

class_dict = {}
class_dict['EECS 442'] = "https://www.lsa.umich.edu/cg/cg_detail.aspx?content=2260EECS442001&termArray=f_19_2260"
# class_dict['EECS 491'] = "https://www.lsa.umich.edu/cg/cg_detail.aspx?content=2260EECS491001&termArray=f_19_2260"
# class_dict['EECS 497'] = "https://www.lsa.umich.edu/cg/cg_detail.aspx?content=2260EECS497001&termArray=f_19_2260"
# class_dict['TECH COM'] = "https://www.lsa.umich.edu/cg/cg_detail.aspx?content=2260TCHNCLCM497001&termArray=f_19_2260"
# class_dict['ARTDES 173'] = "https://www.lsa.umich.edu/cg/cg_detail.aspx?content=2260ARTDES173001&termArray=f_19_2260"

for course, class_link in class_dict.items():
	r = requests.get(class_link)
	data = r.text
	soup = BeautifulSoup(data, "lxml")
	output = course + "\n"
	items = soup.find_all(attrs={"class": "clsschedulerow"})
	for item in items:
		text = item.getText()
		cleaned_text = re.sub('[\s+]','',text)
		section = re.search('Section:(\d+)', cleaned_text)
		if section:
			output += 'Section: ' + section.group(1) + '\t'
		classno = re.search('ClassNo:(\d+)', cleaned_text)
		if classno:
			output += 'ClassNo: ' + classno.group(1) + '\t'
		is_open = re.search('EnrollStat:(.*)OpenSeats', cleaned_text)
		if is_open:
			output += 'Status: ' + is_open.group(1) + '\t'
			if is_open.group(1) == 'Closed':
				waitlist = re.search('Waitlist:(\d+)', cleaned_text)
				if waitlist:
					output += 'Waitlist: ' + waitlist + '\t'
				else:
					output += 'Waitlist: -' + '\t'
			else:
				open_seats = re.search('OpenSeats:(\d+)', cleaned_text)
				if open_seats:
					output += 'Open Seats: ' + open_seats.group(1) + '\t'
		output += "\n"
	print(output)
