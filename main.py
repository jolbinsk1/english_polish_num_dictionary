# main.py
from english_return_function import return_words
from polish_return_function import return_words_PL
from polish_eng_pronunciation import ENG_pro
from IPA_and_format_func import return_IPA, IPA_format
from final_funcs import answer, number_translate

def main():
    return_words()
    return_words_PL()
    ENG_pro()
    return_IPA()
    IPA_format()
    answer()
    number_translate()

if __name__ == "__main__":
    main()
