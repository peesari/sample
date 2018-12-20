--It must start with a 4,5 or 6


total_count = int(raw_input())
numbers_list = []
#refernece list to check the starting series
start_list = [4,5,6]

for count in range(total_count):
    numbers_list.append(raw_input())

#condition 1, validates the starting series
def val_start(num):
    if int(num[0]) in start_list:
        return True
    else:
        return False
		
		
--It must contain exactly  digits.

def val_len(num):
    check = num
    check2 = True
    if "-" in num:
        check = "".join(num.split("-"))
        check2 = val_group(num)

    if ((len(check) == 16) and check2):
        return True
    else:
        return False
	
	
-- It must only consist of digits (0-9). 


--It may have digits in groups of , separated by one hyphen "-". 
def val_rep(num):
    res = "".join(num.split("-"))
    for i in range(len(res)):
        try:
            if (res[i] == res[i+1]):
                if (res[i+1] == res[i+2]):
                    if (res[i+2] == res[i+3]):
                        return False
        except IndexError:
           pass
    return True

for num in numbers_list:
    #returns all the values into a list
    result = [val_start(num), val_len(num),val_isdigit(num), val_rep(num)]
    if False in result:
        print("Invalid")
    else:
        print("Valid")