from english_polish_dictionaries import aughts_ENG_pro, ten_thru_teens_ENG_pro, tens_ENG_pro, hundreds_ENG_pro

# function for returning the english prnunciation of a polish number

def ENG_pro(num):
    
    if num < 10:
        return aughts_PL_ENG_pro[num]
    
    elif num < 20:
        return ten_thru_teens_PL_ENG_pro[num]
    
    elif num <100:
        if num%10==0:
            return tens_PL_ENG_pro[num]
        else:
            return tens_PL_ENG_pro[(num//10)*10]+' '+aughts_PL_ENG_pro[num%10]
        
    elif num < 1000:
        if num%100==0:
            return hundreds_PL_ENG_pro[num]
        else:
            if num%10==0:
                return hundreds_PL_ENG_pro[(num//100)*100] + ' ' +tens_PL_ENG_pro[num%100]
            else:
                return hundreds_PL_ENG_pro[(num//100)*100] + ' ' +tens_PL_ENG_pro[(num%10)*10] + ' '+aughts_PL_ENG_pro[num%10]
            
    elif num < 10000:

        if num % 1000 == 0:
            if num // 1000 == 1:
                return 'TIH-shonts'
            elif num // 100 in ten_thru_teens_PL_ENG_pro:
                return ten_thru_teens_PL_ENG_pro[num // 100] + ' tih-SHEN-tsih'
            else:
                return aughts_PL_ENG_pro[num // 100] + ' tih-SHEN-tsih'

        elif num // 1000 == 1:
            return 'TIH-shonts ' + ENG_pro(num % 1000)

        elif num % 100 == 0:
            return aughts_PL_ENG_pro[num // 1000] + ' tih-SHEN-tsih ' + ten_thru_teens_PL_ENG_pro[num // 100]

        else:
            return aughts_PL_ENG_pro[num // 1000] + ' tih-SHEN-tsih ' + ENG_pro(num % 1000)
    
    elif num < 100000:
        if num%1000==0:
            return ENG_pro(num//1000) + ' tih-SHEN-tsih'
        else:
            return ENG_pro(num//1000) + ' tih-SHEN-tsih ' + ENG_pro(num%1000)
        
    elif num < 1000000:
        if num%1000==0:
            return ENG_pro(num//1000) + ' tih-SHEN-tsih'
        else:
            return ENG_pro(num//1000) + ' tih-SHEN-tsih ' + ENG_pro(num%1000)
    
    elif num == 1000000:
        
        return "ˈMEE-lyon"            
    
