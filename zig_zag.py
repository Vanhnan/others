import time

probel=True
space = 0

while True:
    if probel==True:        
        if space==20:
            probel=False
        print((" "*space)+"********")
        time.sleep(0.1)
        space = space + 1
    elif probel==False:
        if space==0:
            probel=True
        print((" "*space)+"********")
        time.sleep(0.1)
        space = space - 1


    
        
        
