import re
import math

def main():
    # 1
    training_sentence = input()
    training_model = create_BOW(training_sentence)
    
    # 2
    testing_sentence = input()
    testing_model = create_BOW(testing_sentence)

    # 3
    alpha = float(input())

    print(calculate_doc_prob(training_model, testing_model, alpha))

def calculate_doc_prob(training_model, testing_model, alpha):
    # Implement likelihood function here...
    num_of_word_dict = len(training_model.keys())
    num_of_word_train = sum(training_model.values())
    
    logprob = 0
    
    for word in testing_model.keys():
        if word in training_model.keys():
            logprob += (math.log(training_model[word] + alpha) - math.log(num_of_word_train + (num_of_word_dict * alpha))) * testing_model[word]
        else:
            logprob += (math.log(alpha) - math.log(num_of_word_train + (num_of_word_dict * alpha))) * testing_model[word]
        
    return logprob

def create_BOW(sentence):
    bow = {}
    # Copy and paste your code from previous exercise
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
