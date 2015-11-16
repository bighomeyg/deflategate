import commands

def make_august():
	root_filename='deflategate_201508'
	files_for_day=[]
	for day in range(3,32):
		files_for_day.append(''.join('deflategate_201508' + "%02d"%day + '*'))
	for n in range(0,len(files_for_day)):
	 	tweets_per_day=commands.getoutput(''.join("wc -l " + files_for_day[n] + "| grep total | awk '{print $1}'"))
		print tweets_per_day
		
def make_sept():
	root_filename='deflategate_201509'
	files_for_day=[]
	for day in range(1,12):
		files_for_day.append(''.join('deflategate_201509' + "%02d"%day + '*'))
	for n in range(0,len(files_for_day)):
	 	tweets_per_day=commands.getoutput(''.join("wc -l " + files_for_day[n] + "| grep total | awk '{print $1}'"))
		print tweets_per_day

make_august()		
make_sept()


