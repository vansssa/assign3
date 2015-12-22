
def sorted_str_and_sum(file):
	
	with open(file,'r') as f :
		 return_result=[]
		 for line in f :
			li=line.replace("\"","").split(',')
			for l in sorted(li) :
				result=0
			 	for i in range(0,len(l),1) :
			 		result =result + (ord(l[i:i+1])-64)
			 	
			 	return_result=return_result+[result]
			
			return return_result


sorted_str_and_sum('a2.txt')




