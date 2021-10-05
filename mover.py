import serial
from time import sleep 
step = serial.Serial('/dev/ttyUSB0',115200)

ser = serial.Serial('/dev/ttyUSB1',115200)

tim=0.37 #0.4  servo
#tim=1.2

timr=0.075   #rotate
timf=0.075  #flip 0.31
timm=0.085		#motor



def U():
	
	
	step.write(b'm')
	sleep(timf)
	ser.write(b'#1P2112T10#3P806T10!')
	sleep(tim)
	step.write(b'l') 
	sleep(timf)   
	step.write(b'g')	 
	sleep(timf)
	ser.write(b'#1P1446T10#3P1504T10!')    
	sleep(tim) 
    
	    
	step.write(b'F')
	sleep(timm)
	ser.write(b'#2P2250T10!')
	sleep(tim)
	step.write(b'G')
	sleep(timm)
	ser.write(b'#2P1528T10!')   
	sleep(tim)
    
	ser.write(b'#1P2112T10#3P806T10!')   
	sleep(tim)  
	step.write(b'f')
	sleep(timf)
	step.write(b'm')
	sleep(timf)
	ser.write(b'#1P1446T10#3P1504T10!')  
	sleep(tim)
	step.write(b'l')    
	sleep(timf)
      
    
    
    
	
	

    
    
    
    
def UA():
    step.write(b'm')
    sleep(timf)
    ser.write(b'#1P2112T10#3P806T10!')
    sleep(tim)
    step.write(b'l') 
    sleep(timf)   
    step.write(b'g')	 
    sleep(timf)
    ser.write(b'#1P1446T10#3P1504T10!')    
    sleep(tim) 
    
	    
    step.write(b'F')
    sleep(timm)
    ser.write(b'#2P789T10!')
    sleep(tim)
    step.write(b'G')
    sleep(timm)
    ser.write(b'#2P1528T10!')   
    sleep(tim)
    
    ser.write(b'#1P2112T10#3P806T10!')   
    sleep(tim)  
    step.write(b'f')
    sleep(timf)
    step.write(b'm')
    sleep(timf)
    ser.write(b'#1P1446T10#3P1504T10!')  
    sleep(tim)
    step.write(b'l')    
    sleep(timf)
    
    

def UU():
    step.write(b'm')
    sleep(timf)
    ser.write(b'#1P2112T10#3P806T10!')
    sleep(tim)
    step.write(b'l') 
    sleep(timf)   
    step.write(b'g')	 
    sleep(timf)
    ser.write(b'#1P1446T10#3P1504T10!')    
    sleep(tim) 
    
	    
    step.write(b'G')
    sleep(timm)
    ser.write(b'#2P817T10!')
    sleep(tim)
    step.write(b'F')
    sleep(timm)
    ser.write(b'#2P2216T10!')   
    sleep(tim*2)    
    step.write(b'G')
    sleep(timm)
    ser.write(b'#2P1504T10!')
    sleep(tim)

    
    
    ser.write(b'#1P2112T10#3P806T10!')   
    sleep(tim)  
    step.write(b'f')
    sleep(timf)
    step.write(b'm')
    sleep(timf)
    ser.write(b'#1P1446T10#3P1504T10!')  
    sleep(tim)
    step.write(b'l')    
    sleep(timf)
    


def D():
	
	
	step.write(b'm')
	sleep(timf)
	ser.write(b'#1P735T10#3P2184T10!')
	sleep(tim)
	step.write(b'l') 
	sleep(timf)   
	step.write(b'g')	 
	sleep(timf)
	ser.write(b'#1P1446T10#3P1504T10!')    
	sleep(tim) 
    
	    
	step.write(b'F')
	sleep(timm)
	ser.write(b'#2P2250T10!')
	sleep(tim)
	step.write(b'G')
	sleep(timm)
	ser.write(b'#2P1528T10!')   
	sleep(tim)
    
	ser.write(b'#1P735T10#3P2184T10!') 
	sleep(tim)  
	step.write(b'f')
	sleep(timf)
	step.write(b'm')
	sleep(timf)
	ser.write(b'#1P1446T10#3P1504T10!')  
	sleep(tim)
	step.write(b'l')    
	sleep(timf)
      
    
    
    
	
	

    
    
    
    
def DA():
    step.write(b'm')
    sleep(timf)
    ser.write(b'#1P735T10#3P2184T10!')
    sleep(tim)
    step.write(b'l') 
    sleep(timf)   
    step.write(b'g')	 
    sleep(timf)
    ser.write(b'#1P1446T10#3P1504T10!')    
    sleep(tim) 
    
	    
    step.write(b'F')
    sleep(timm)
    ser.write(b'#2P789T10!')
    sleep(tim)
    step.write(b'G')
    sleep(timm)
    ser.write(b'#2P1528T10!')   
    sleep(tim)
    
    ser.write(b'#1P735T10#3P2184T10!') 
    sleep(tim)  
    step.write(b'f')
    sleep(timf)
    step.write(b'm')
    sleep(timf)
    ser.write(b'#1P1446T10#3P1504T10!')  
    sleep(tim)
    step.write(b'l')    
    sleep(timf)
    
    

def DD():
    step.write(b'm')
    sleep(timf)
    ser.write(b'#1P735T10#3P2184T10!')
    sleep(tim)
    step.write(b'l') 
    sleep(timf)   
    step.write(b'g')	 
    sleep(timf)
    ser.write(b'#1P1446T10#3P1504T10!')    
    sleep(tim) 
    
	    
    step.write(b'G')
    sleep(timm)
    ser.write(b'#2P817T10!')
    sleep(tim)
    step.write(b'F')
    sleep(timm)
    ser.write(b'#2P2216T10!')   
    sleep(tim*2)    
    step.write(b'G')
    sleep(timm)
    ser.write(b'#2P1504T10!')
    sleep(tim)
    
    
    
    ser.write(b'#1P735T10#3P2184T10!')
    sleep(tim)  
    step.write(b'f')
    sleep(timf)
    step.write(b'm')
    sleep(timf)
    ser.write(b'#1P1446T10#3P1504T10!')  
    sleep(tim)
    step.write(b'l')    
    sleep(timf)
    
    
    
    
        
    
    



def L():
    ser.write(b'#1P2170T10!')
    sleep(tim)
    step.write(b'M')
    sleep(timm)
    ser.write(b'#1P1446T10!')
    sleep(tim)
    step.write(b'L')
    sleep(timm)
    
def LA():
    ser.write(b'#1P740T10!')
    sleep(tim)
    step.write(b'M')
    sleep(timm)
    ser.write(b'#1P1446T10!')
    sleep(tim)
    step.write(b'L')
    sleep(timm)

def LL():
    step.write(b'M')
    sleep(timm)
    ser.write(b'#1P735T10!')
    sleep(tim)
    step.write(b'L')
    sleep(timm)
    ser.write(b'#1P2170T10!')
    sleep(tim*2)
    step.write(b'M')
    sleep(timm)
    ser.write(b'#1P1446T10!')
    sleep(tim)
    step.write(b'L')
    sleep(timm)

def R():
    ser.write(b'#3P2230T10!')
    sleep(tim)
    step.write(b'S')
    sleep(timm)
    ser.write(b'#3P1470T10!')
    sleep(tim)
    step.write(b'R')
    sleep(timm)
    
    

def RA():
    ser.write(b'#3P800T10!')
    sleep(tim)
    step.write(b'S')
    sleep(timm)
    ser.write(b'#3P1489T10!')
    sleep(tim)
    step.write(b'R')
    sleep(timm)
    
    
def RR():
   
    step.write(b'S')
    sleep(timm)
    ser.write(b'#3P2184T10!')
    sleep(tim)
    step.write(b'R')
    sleep(timm)    
    ser.write(b'#3P790T10!')
    sleep(tim*2)
    step.write(b'S')
    sleep(timm)
    ser.write(b'#3P1478T10!')
    sleep(tim)
    step.write(b'R')
    sleep(timm)
    
   
   
def F():
    ser.write(b'#4P2200T10!')
    sleep(tim)
    step.write(b'E')
    sleep(timm)
    ser.write(b'#4P1458T10!')
    sleep(tim)
    step.write(b'D')
    sleep(timm)


def FA():
    ser.write(b'#4P751T10!')
    sleep(tim)
    step.write(b'E')
    sleep(timm)
    ser.write(b'#4P1458T10!')
    sleep(tim)
    step.write(b'D')
    sleep(timm)
    
def FF():
    step.write(b'E')
    sleep(timm)
    ser.write(b'#4P2176T10!')
    sleep(tim)
    step.write(b'D')
    sleep(timm)    
    ser.write(b'#4P750T10!')
    sleep(tim*2)
    step.write(b'E')
    sleep(timm)
    ser.write(b'#4P1458T10!')
    sleep(tim)
    step.write(b'D')
    sleep(timm)
    
def B():
    ser.write(b'#2P2250T10!')
    sleep(tim)
    step.write(b'V')
    sleep(tim)
    ser.write(b'#2P1528T10!')
    sleep(tim)
    step.write(b'U')
    sleep(tim)


def BA():
    ser.write(b'#2P789T10!')
    sleep(tim)
    step.write(b'V')
    sleep(timm)
    ser.write(b'#2P1528T10!')
    sleep(tim)
    step.write(b'U')
    sleep(timm)

def BB():
    step.write(b'V')
    sleep(timm)
    ser.write(b'#2P2230T10!')
    sleep(tim)
    step.write(b'U')
    sleep(timm)    
    ser.write(b'#2P807T10!')
    sleep(tim*2)
    step.write(b'V')
    sleep(timm)
    ser.write(b'#2P1528T10!')
    sleep(tim)
    step.write(b'U')
    sleep(timm)
    
    
def RT():
    step.write(b'm')
    sleep(timr)
    ser.write(b'#2P2200T10#4P779T10!')   
    sleep(tim)
    step.write(b'l')
    sleep(timr)    
    step.write(b'g')
    sleep(timr)
    ser.write(b'#2P1528#4P1458T10!')
    sleep(tim)
    step.write(b'f')
    sleep(timr)
def FRT():
    step.write(b'g')
    sleep(timr)
    ser.write(b'#1P735T10#3P2184T10!')
    sleep(tim)
    step.write(b'f')
    sleep(timr)    
    step.write(b'm')
    sleep(timr)
    ser.write(b'#1P1446#3P1478T10!')
    sleep(tim)
    step.write(b'l')
    sleep(timr)   
    
def FFRT():
	step.write(b'm')
	sleep(timf)
	ser.write(b'#1P2112T10#3P806T10!')  
	sleep(tim)
	step.write(b'l')
	sleep(timf)
	step.write(b'g')
	sleep(timf)
	ser.write(b'#1P735T10#3P2184T10!')   
	sleep(tim*2)
	step.write(b'f')
	sleep(timf)    
	step.write(b'm')
	sleep(timf)
	ser.write(b'#1P1446#3P1478T10!')
	sleep(tim)
	step.write(b'l')
	sleep(timf)  
	
	
def BACK():
    step.write(b'g')
    sleep(timb)
    ser.write(b'#1P735T10#3P2184T10!')#
    sleep(timb)
    step.write(b'f')
    sleep(timb)    
    step.write(b'm')
    sleep(timb)
    ser.write(b'#1P1446#3P1478T10!')
    sleep(timb)
    step.write(b'l')
    sleep(timb)
    step.write(b'g')
    sleep(timb)
    ser.write(b'#2P817T10#4P2176T10!')
    sleep(timb)
    step.write(b'f')
    sleep(timb)
    step.write(b'm')
    sleep(timb)
    ser.write(b'#2P2216T10#4P779T10!')   
    sleep(timb*2)
    step.write(b'l')
    sleep(timb)
    
    step.write(b'g') 
    sleep(timb)
    ser.write(b'#2P1528T10#4P1458T10!')      
    sleep(timb)
    ser.write(b'#1P2112T10#3P806T10!')
    sleep(timb)
    step.write(b'f')
    sleep(timb)    
    step.write(b'm')
    sleep(timb)
    ser.write(b'#1P1446#3P1478T10!')
    sleep(timb)
    step.write(b'l')
    
     
	
		      
while 0:
    #read_serial=ser.readline()
    #s[0] = str(int (ser.readline(),16)
  # U F2 B U' F' R' D2 L2 F L' B' D F2 B2 U' F2 L2 U B2 R2", '(20
   # sleep(1)
   
    
    D()    
    sleep(1)    
    DA()  
    sleep(1100)   
    FF()
    sleep(tim)
    B()
    sleep(tim) 
    RR()    
    sleep(tim)    
    FF()
    sleep(tim)
    BB()  
    sleep(tim)
    
    sleep(1)   
    RA()    
    sleep(tim)    
    LL()
    sleep(tim)
    UU()
    sleep(tim) 
    BB()    
    sleep(tim)    
    F()
    sleep(tim)
    DD()
    #sleep(tim) 
    
    
    sleep(tim) 
    F()    
    sleep(tim)    
    B()
    sleep(tim)
    U()
    sleep(tim) 
    L()    
    sleep(tim)    
    R()
    sleep(tim)
    sleep(111)
    
