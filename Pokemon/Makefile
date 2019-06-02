CC=gcc
CFLAGS=-Wall -g


SG : 
	scp -r gan.py ebensma@login.palmetto.clemson.edu:/scratch2/ebensma/workspaces/GAN/Pokemon/

GPOI : 
	scp -r ebensma@login.palmetto.clemson.edu:/scratch2/ebensma/workspaces/GAN/Pokemon/images/* images/

GPOD : 
	scp -r ebensma@login.palmetto.clemson.edu:/scratch2/ebensma/workspaces/GAN/Pokemon/analytics/* analytics/

SPID : 
	scp -r database/* ebensma@login.palmetto.clemson.edu:/scratch2/ebensma/workspaces/GAN/Pokemon/database/ 

clean:
	rm $(BINS)