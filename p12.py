def is_palindrome(supllied_word):
    reversed_word = ''
    for i in range(len(supllied_word)):
        reversed_word =reversed_word +  supllied_word[len(supllied_word)-i-1]
    if reversed_word == supllied_word:
        print("yes palindrome")
    else:
        print("not a palindrome")

palindrome_word = input("Enter the word to determine plaindrome: ")
is_palindrome(palindrome_word)