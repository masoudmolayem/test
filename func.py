import numpy  
ppi_2=numpy.array([[1,1],#0
                   [1,0],#1
                   [1,1],#2
                   [1,0],#3
                   [1,1],#4
                   [1,0],#5
                   [0,1],#6
                   [1,1],#7
                   [1,1],#8
                   [0,1],#9
                   [1,0],#10
                   [1,1],#11
                   [1,0],#12
                   [1,1],#13
                   [1,0],#14
                   [1,1]
                   ])



def number_of_one(list_1):
    s=0
    for i in list_1:
        if(i==1):
            s=s+1
    return(s)    

def code(L):
    index=0
    c=0
    for i in L:
        c+=(i*(2**index) )
        index+=1
    return(c)
      
def index_of_0_1(L):
    i=0
    indexs=[[],[]]
    for q in L:
        if q==1:
            indexs[1].append(i)
        else:
            indexs[0].append(i)
            
        i+=1    
    return(indexs)

    
def ppi_2_check(f,ppi):
    
    f_BC=[f[0],f[1],f[2],f[3]]
    f_AC=[f[0],f[1],f[4],f[5]]
    f_AB=[f[0],f[2],f[4],f[6]]
    n_BC=code(f_BC)
    n_AC=code(f_AC)
    n_AB=code(f_AB)
    if(ppi_2[n_BC][ppi[0]]==0 or ppi_2[n_AC][ppi[1]]==0 or ppi_2[n_AB][ppi[2]]==0):
        return(0)
    else:
        return(1)
    
    
def reverse(x):
    return(abs(x-1))    


def relation1_on_2(x,y):
    k=str(x)+str(y)
    if (k=='14' or k=='41'):
        return (5)
    elif(k=='12' or k=='21'):
        return(3)
    else:
        return(6)
    
def relation_cis_to(x,y):
    k=str(x)+str(y)
    if (k=='01' or k=='10'):
        return (3)
    elif(k=='02' or k=='20'):
        return(5)
    else:
        return(6)    
    
    
    
    

def p0(f_abstract,ppi,f_bin_number):#hich complexi vojud nadashte bashad
    help1=number_of_one(f_abstract[1]) #tedad 1 haye tanha
    if help1==0:
        number2=number_of_one(f_abstract[2]) #tedad 1haye 2taei
        if (number2==2 or number2==3):
            if f_abstract[3]==1 :
                return(1)
            else:
                return(0)
            
        else:    
            return (1)
    elif help1==1:
        index=index_of_0_1(f_abstract[1])
        m1=relation1_on_2(index[0][0], index[1][0])# moshtarake 0 va 1
        m2=relation1_on_2(index[0][1],index[1][0])# moshtarake 0 va 1
        m3=relation1_on_2(index[0][0],index[0][1])# moshtarake 2 ta 0
        if(f_bin_number[m1]==1 and f_bin_number[m2]==1 ):
            if (f_abstract[3]==1):
                return(1)   
            else:
                return(0)
        elif(f_bin_number[m3]==1 ):
            if(f_abstract[3]==1):
                return(1)
            else:
                return(0)
        elif(f_abstract[3]==0)    :
            return(1)
        else:
            return(0)
        
    elif help1==2:
        index=index_of_0_1(f_abstract[1])
        m1=relation1_on_2(index[0][0], index[1][0])
        m2=relation1_on_2(index[0][0],index[1][1])
        #m3=relation1_on_2(index[0][0],index[0][1])        
        if (f_bin_number[m1]==0 and f_bin_number[m2]==0):
            if (f_abstract[3]==0):
                return(1)
            else:
                return(0)
        else:
            if(f_abstract[3]==1):
                return(1)
            else:
                return(0)
            
        
    elif f_abstract[3]==1:
        return(1)
    return(0)


def p1(f_abstract,ppi,f_bin_number):# 1 complex vojud dashte bashad
    ppi_index=index_of_0_1(ppi)
    other=[4,2,1]#indexe TFhaei ke complex nadarand bar asase ppi mojud
    f_help=[f_bin_number[0], f_abstract[2][ppi_index[1][0]],f_bin_number[other[ppi_index[1][0]]],f_bin_number[7] ]
    f_ind=code(f_help)
    if ppi_2[f_ind][0]==1:
        return(1)
    else:
        return(0)
    
def p2(f_abstract,ppi,f_bin_number): # 2 complex vojud dashte bashe
    ind=index_of_0_1(ppi)
    
    if (f_abstract[2][ind[1][0]]==0 or f_abstract[2][ind[1][1]]==0 or f_abstract[3]==1):
        return (1)
    else:
        if (f_abstract[2][ind[0][0]])==0:#inja
            return(1)
        else:
            return(0)
        
        
    return
def p3():# 3 complex vojud dashte bashad
    return (1)
    