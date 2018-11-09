#calcolytaaar
a=0
while a<100 :
    print("/"*97)
    def add(NB1,NB2):
        print(NB1+NB2)
    def sub(NB1,NB2):
        print(NB1-NB2)
    def multi(NB1,NB2):
        print(NB1*NB2)
    def div(NB1,NB2):
        print(NB1/NB2)
    C=input("what Operation u wanna do ? :" )
    
    A=int(input("NB1:"))
    B=int(input("NB2:"))
    
    if C=="add" :
          add(A,B)
    elif C=="sub" :
          sub(A,B)
    elif C=="multi":
          multi(A,B)
    elif C=="div":
          div(A,B)
    else :
        print("PLZ insert one off the fowilling operations (add , sub , multi or div)")
        
    
                        
          
