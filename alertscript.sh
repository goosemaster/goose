#!/bin/bash                                                                                                                                                                                                                      
                                                                                                                                                                                                                                 
echo -e "How many minutes do you want to wait before the alarm goes off?\n"                                                                                                                                                      
                                                                                                                                                                                                                                 
read minutes;                                                                                                                                                                                                                    
seconds=$[$minutes*60];                                                                                                                                                                                                          
for i in $seconds; do                                                                                                                                                                                                            
        sleep $i;                                                                                                                                                                                                                
        mplayer /home/prannon/Downloads/Sound\ Effects/tng_red_alert1.mp3;                                                                                                                                                      
done;  
