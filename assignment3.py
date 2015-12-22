
def sorted_str_and_sum(file):
	
	with open(file,'r') as f :
		 return_result = 0
		 for line in f :
			li = sorted(line.replace("\"","").split(','))
			for l in li :
				result = 0
			 	for i in range(0,len(l),1) :
			 		result = result + (ord (l[i : i + 1 ]) - 64)
				
			 	result = result * (int((li.index(l))) + 1)
			 	return_result = result + return_result
				
			return return_result


print sorted_str_and_sum('a2.txt')




