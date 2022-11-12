S , n = input().split()  #taking the first two numbers input and splitting it , cuz its row wise
 
l = list(input().split())   #taking the seats as input and splitting  it into list 
l.append(int(l[0]) + int(S))  #add a extra number because Seats S and 1 are also directly beside each other. so to get my formula valid                                #for 1st seat and S th position seats
ans = 0                         # to store answer and print it at last
# for-loop to iterate over the list of seats that we got in input , CHANGE it to WHILE-loop if u want => [ i = 1; while(i < len(l)) and add i += 1 in the body of while-loop ] and I am starting from position 1 not 0 because seats are listed as 1 , 2 .... , S in circular order
for i in range(1 ,len(l)):      
  #just check the gaps between the seats provided if its greater than 2 then we can let people sit and then we divide it by 2 because #we can't let 2 people sit side by side and we need atleast 1 gap in between
    gap = int(l[i]) - int(l[i-1])
    if(gap - 1 > 2): 
        ans += (gap - 2) // 2
print(ans)
 
