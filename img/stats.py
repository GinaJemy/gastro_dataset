import os
count = [0,0,0,0,0,0,0,0,0] 
for filename in os.listdir('/home/gina/gastro_dataset/img/labels/'):
	if filename.endswith('txt'):
		with open(os.path.join('/home/gina/gastro_dataset/img/labels/',filename), 'r') as file:
			lines = file.readlines()
			for line in lines:
				count[int(line[0])] =  count[int(line[0])] + 1
        	
print(count)     	

