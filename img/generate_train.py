import os
f= open('/home/gina/gastro_dataset/img/train.txt','w')
for filename in os.listdir('/home/gina/gastro_dataset/img/images/'):
    f.write('/home/gina/gastro_dataset/img/images/'+filename+'\n')
	
