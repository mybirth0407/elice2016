import re

def main():
    sentence = input()
    BOW = create_BOW(sentence)

    print(BOW)

def create_BOW(sentence):
    bow = {}
    
    # Exercise
    lower_sentence = sentence.lower()
    modified_str = replace_non_alphabetic_chars_to_space(lower_sentence)
    words = modified_str.split(' ')
    for word in words:
        if len(word) >= 1:
            if word in bow:
                bow[word] += 1 
            else:
                bow[word] = 1
    
    return bow

def replace_non_alphabetic_chars_to_space(sentence):
    return re.sub(r'[^a-z]+', ' ', sentence)

if __name__ == "__main__":
    main()
