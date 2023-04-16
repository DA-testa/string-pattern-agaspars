# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    choice = input().strip().upper()
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    if choice == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif choice == 'F':
        filename = 'tests/' + input().strip()
        with open(filename, 'r') as test:
            pattern = test.readline().rstrip()
            text = test.readline().rstrip()
    # return both lines in one return
    # this is the sample return, notice the rstrip function
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    occurrences = []
    patternLen, textLen = len(pattern), len(text)
    patternHash = hash(pattern)
    for i in range(textLen - patternLen + 1):
        if hash(text[i:i+patternLen]) == patternHash and text[i:i+patternLen] == pattern: #check whether the hash values of chosen text part and pattern are equal, and characters in the pattern and the substring are equal
            occurrences.append(i)   #occurence met
    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

