# a function that returns the English and Polish numbers, together with their Polish pronunciation

def answer(num):
    
    print('\n')
    print('\033[1m'+'English: '+'\033[0m'+return_words(num))
    print('\n')
    print('\033[1m'+'Polish: '+'\033[0m'+return_words_PL(num))
    print('\033[1m'+'   '+'* '+ 'English pronunciation: '+'\033[0m'+ENG_pro(num))
    print('\033[1m'+'   '+'* '+'IPA pronunciation: '+'\033[0m'+IPA_format(num))

# finally, we have the function that asks for a number between 0 and 1,000,000

def number_translate():
    while True:
        try:
            num = int(input('Please enter an integer from 0 to 1,000,000 (do not include commas or periods): '))
            if 0 <= num <= 1000000:
                return answer(num)
            else:
                print('The integer must be between 0 and 1,000,000.')
                continue
        except ValueError:
            print('That is not valid. Please enter an integer from 0 to 1,000,000 (do not include commas or periods):')
            continue
        else:
            break



    
