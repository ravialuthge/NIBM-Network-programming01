sum=0
p=0
n=0
discount=0
def cal():
        if sum>=2000:
            discount=sum*0.10
            n=sum-discount
            print("discount :",discount)
            print("net total :",n)
            return file1(discount,n)
        elif sum>=1500:
            discount=sum*0.07
            n=sum-discount
            print("discount :",discount)
            print("net total :",n)
            return file1(discount,n)
        elif sum>=1000:
            discount=sum*0.05
            n=sum-discount
            print("discount :",discount)
            print("net total :",n)
            return file1(discount,n)
        elif sum<1000:
            print("no discount")
            discount=0
            n=sum
            print("net total :",n)
            return file1(discount,n)

def file1(discount,n):
        
        file=open("C:\\Users\\Ravi\\Documents\\bill.txt",'a+')
        file.write("\n")
        file.write(str(discount))
        file.write("\n")
        file.write(str(n))
        file.close()

while True:
    try:
        p=float(input("enter price :"))
        sum=sum+p
    except:
        print("total sum:",sum)
        break  
cal()
file1(discount,n)



                                    

        
        

                                    
    
             






