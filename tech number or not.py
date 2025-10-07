n=2025
num_str=str(n)
if len(num_str) % 2 !=0:
    print(False)
else:
    half=len(num_str) // 2 
    first_half=int(num_str[:half])
    second_half=int(num_str[half:])   
if(first_half+second_half)**2==n:
    print("tech")
else:
    print("Not tech")