#Likhita Japam
def likhita_nama_japam(num):
    s="Aum Sri Sairam"
    i=1
    while(i<=num+1):
        print(s,end='\n')
        i=i+1
    
    print("\n")
    print("\nJai Sai Ram")
    print("\n")
    print("\n")

try:
    n = int(input("Enter the number of times = "))
    likhita_nama_japam(n)

except ValueError:
    print("Error! Enter valid number")