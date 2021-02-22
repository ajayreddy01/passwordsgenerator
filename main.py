from itertools import combinations 

n = int(input("Enter The NUmber Length Of the password You Want To Make:"))
comb = combinations([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,!,@,$,#,%,^,&,*,(,),-,_,=,+,<,>,.,?,/,",',{,},\,|,~] n) 
#converting a tuple in to list
def convertTuple(tup): 
    str =  ''.join(tup) 
    f=open("customlist.txt", "a+")
    f.write(str)
    f.close()
 
# Print the obtained combinations 
for i in list(comb):  
    convertTuple(i)
    
