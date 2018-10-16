'''
Created on Oct 14, 2018

@author: lfko

    check, if a given string is a palindrome (it reads the same, irregardless of direction)
'''


def check_palindrome(word):
    """ """
    
    print(' checking the word ', word, ' right now!')
    word = word.lower();
    # count the words length
    wlen = len(word);
    
    print(' word length ', wlen);
    
    if wlen % 2 == 0:
        # even
        word_first_part = word[0:int(wlen / 2)];
        word_second_part = word[int(wlen / 2):]
        
        # print(word_first_part, word_second_part);
        if word_first_part == word_reverse(word_second_part):
            print(' we found a palindrome ', word);
    else:
        # odd
        word_first_part = word[0:int(wlen / 2)];
        word_second_part = word[int((wlen / 2) + 1):]

        print(word_first_part, word_reverse(word_second_part));
        if word_first_part == word_reverse(word_second_part):
            print(' we found a palindrome ', word);

    # or just reverse the word in question and check if the outcome is the same as the original word
    rvs_word = word_reverse(word);
    if(rvs_word == word):
        print(' palindrome found ');


def word_reverse(word):
    reverse = '';
    
    for c in reversed(word):
        reverse = reverse + c;
        
    return reverse;


if __name__ == '__main__':
    
    words = ['banane', 'lagerregal', 'zeitung', 'otto', 'pfanne', 'rentner', 'reliefpfeiler', 'anna', 'Dioid', 'Ebbe'];
    
    for word in words:
        check_palindrome(word);
        print('-----------------')
