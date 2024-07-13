from english_polish_dictionaries import aughts_PL, ten_thru_teens_PL, tens_PL, hundreds_PL

# function for returning Polish written words for numbers 0 to 1,000,000

def return_words_PL(num):
    
    if num < 10:
        return aughts_PL[num]
    
    elif num < 20:
        return ten_thru_teens_PL[num]
    
    elif num <100:
        if num%10==0:
            return tens_PL[num]
        else:
            return tens_PL[(num//10)*10]+aughts_PL[num%10]
        
    elif num < 1000:
        if num%100==0:
            return hundreds_PL[num]
        else:
            if num%10==0:
                return hundreds_PL[(num//100)*100] + tens_PL[num%100]
            else:
                return hundreds_PL[(num//100)*100] + tens_PL[(num%10)*10] + aughts_PL[num%10]
            
    elif num < 10000:
        if num == 1000:
            return 'tysiąc'

        elif num % 1000 == 0:
            if num // 1000 == 1:
                return 'tysiąc'
            elif num // 100 in ten_thru_teens_PL:
                return ten_thru_teens_PL[num // 100] + ' tysięcy'
            else:
                return aughts_PL[num // 100] + ' tysięcy'

        elif num // 1000 == 1:
            return 'tysiąc ' + return_words_PL(num % 1000)

        elif num % 100 == 0:
            return aughts_PL[num // 1000] + ' tysiąc ' + ten_thru_teens_PL[num // 100]

        else:
            return aughts_PL[num // 1000] + ' tysiąc ' + return_words_PL(num % 1000)
    
    elif num < 100000:
        if num%1000==0:
            return return_words_PL(num//1000) + ' tysięcy'
        else:
            return return_words_PL(num//1000) + ' tysięcy ' + return_words_PL(num%1000)
        
    elif num < 1000000:
        if num%1000==0:
            return return_words_PL(num//1000) + ' tysięcy'
        else:
            return return_words_PL(num//1000) + ' tysięcy ' + return_words_PL(num%1000)
    
    elif num == 1000000:
        
        return "milion"            
        
