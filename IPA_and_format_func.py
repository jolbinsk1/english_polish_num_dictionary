# function for returning the IPA prnunciation of a polish number

def return_IPA(num):
    
    if num < 10:
        return aughts_PL_IPA[num]
    
    elif num < 20:
        return ten_thru_teens_PL_IPA[num]
    
    elif num <100:
        if num%10==0:
            return tens_PL_IPA[num]
        else:
            return tens_PL_IPA[(num//10)*10]+aughts_PL_IPA[num%10]
        
    elif num < 1000:
        if num%100==0:
            return hundreds_PL_IPA[num]
        else:
            if num%10==0:
                return hundreds_PL_IPA[(num//100)*100] + tens_PL_IPA[num%100]
            else:
                return hundreds_PL_IPA[(num//100)*100] + tens_PL_IPA[(num%10)*10] + aughts_PL_IPA[num%10]
            
    elif num < 10000:

        if num % 1000 == 0:
            if num // 1000 == 1:
                return 'ˈtɨ.ɕɔnt͡s'
            elif num // 100 in ten_thru_teens_PL_IPA:
                return ten_thru_teens_PL_IPA[num // 100] + ' tɨˈɕɛnt͡sɨ'
            else:
                return aughts_PL_IPA[num // 100] + ' tɨˈɕɛnt͡sɨ'

        elif num // 1000 == 1:
            return 'ˈtɨ.ɕɔnt͡s ' + return_IPA(num % 1000)

        elif num % 100 == 0:
            return aughts_PL_IPA[num // 1000] + ' ˈtɨˈɕɛnt͡sɨ ' + ten_thru_teens_PL_IPA[num // 100]

        else:
            return aughts_PL_IPA[num // 1000] + ' ˈtɨˈɕɛnt͡sɨ ' + return_IPA(num % 1000)
    
    elif num < 100000:
        if num%1000==0:
            return return_IPA(num//1000) + ' tɨˈɕɛnt͡sɨ'
        else:
            return return_IPA(num//1000) + ' tɨˈɕɛnt͡sɨ ' + return_IPA(num%1000)
    
    elif num < 1000000:
        if num%1000==0:
            return return_IPA(num//1000) + ' tɨˈɕɛnt͡sɨ'
        else:
            return return_IPA(num//1000) + ' tɨˈɕɛnt͡sɨ ' + return_IPA(num%1000)
    
    elif num == 1000000:
        
        return "ˈmi.lʲɔn"            
    
    
# function for returning the correctly formatted IPA pronunciation
    
def IPA_format(num):
    
    return '/ '+return_IPA(num)+' /'
        
