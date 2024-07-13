from english_polish_dictionaries import aughts, ten_thru_teens, tens

# function for returning the English words for numbers 0 to 1,000,000

def return_words(num):
    
    if num < 10:
        return aughts[num]
    
    elif num < 20:
        return ten_thru_teens[num]
    
    elif num < 100:
        if num%10==0:
            return tens[num]
        else:
            return tens[(num//10)*10] + '-' + aughts[num%10]
        
    elif num < 1000:
        if num%100==0:
            return aughts[num//100] + ' hundred'
    
        else:
            return aughts[num//100] + ' hundred ' + return_words(num%100)
    
    elif num < 10000:
        if num%1000==0:
            return aughts[num//1000] + ' thousand'
            
        else:
            return aughts[num//1000] + ' thousand ' + return_words(num%1000)
            
    elif num < 100000:
        if num%1000==0:
            return return_words(num//1000) + ' thousand'
        
        else:
            return return_words(num//1000) + ' thousand ' + return_words(num%1000)
        
    elif num < 1000000:
        if num%1000==0:
            return return_words(num//1000) + ' thousand'
        else:
            return return_words(num//1000) + ' thousand ' + return_words(num%1000)

    elif num == 1000000:
        
        return "one million"
