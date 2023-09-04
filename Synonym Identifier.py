#####################################################################################
##
## CS 101
## Program #6
## Ethan McFarland
## Em463@mail.umkc.edu
##
## PROBLEM: Build an intelligent system that can read novels and find the similarity
##          between words in order to find synonyms
##
## ALGORITHM: 
##      1.For file in files
##          1.With file open as 'text', for line in text
##              1.Assign return of line in function get_sentence_lists in function
##                build_semantic_descriptors to semantic_descriptors
##      2.Pass test.txt to function run_similarity_test
##      3.Print percetn guessed correctly
## 
## ERROR HANDLING:
##      None
##
## OTHER COMMENTS:
##      None
##
#####################################################################################

import re
import math
import os

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 2.
    '''
    
    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    '''Return the cosine similarity of sparse vectors vec1 and vec2,
    stored as dictionaries as described in the handout for Project 2.
    '''
    
    dot_product = 0.0  # floating point to handle large numbers
    for x in vec1:
        if x in vec2:
            dot_product += vec1[x] * vec2[x]
    
    return dot_product / (norm(vec1) * norm(vec2))


def get_sentence_lists(text : str) -> list:
    '''Return a list which contains lists of strings, one list for
    each sentence in the string text'''
    
    word_list = []
    strt = 0
    text = [word.lower() for word in text.split()]
    
    for word, end in zip(text, range(len(text))):
        if ('.' in word) or ('?' in word) or ('!' in word):
            end += 1
            string = text[strt:end]
            for num, i in enumerate(string):
                string[num] = re.sub('[^a-zA-Z]','', i)
            word_list.append(string)
            strt = end
                   
    if len(word_list) == 0:
        return [text]
    else:
        return word_list

    
def get_sentence_lists_from_files(filenames : list) -> list:
    '''Return list of every sentence contained in all the text files
    in filenames, in order.'''
    
    with open(filenames) as file:
        for num, line in enumerate(file):
            if (num < 100) and (len(line) > 1):
                return get_sentence_lists(line)


def build_semantic_descriptors(sentences : list, word_dict = {}) -> dict:
    '''Return dictionary d such that for every word w that appears in
    at least one of the sentences, d[w] is itself a dictionary which
    represents the semantic descriptor of w'''

    for sentence in sentences:
        for word1 in sentence:
            word_dict[word1] = word_dict.get(word1, {})
            for word2 in sentence:
                if word1 != word2:
                    word_dict[word1][word2] = word_dict[word1].get(word2, 0) + 1
    
    return word_dict 


def most_similar_word(word : str, choices : list) -> float:
    '''Return the element of choices which has the largest semantic
    similarity to word'''

    similarity_scores = {}
    temp_score = 0

    for i in choices:
        try:
            if temp_score <= cosine_similarity(semantic_descriptors[word],semantic_descriptors[i]):
                temp_score = cosine_similarity(semantic_descriptors[word],semantic_descriptors[i])
            similarity_scores[word] = (i,temp_score)
        except KeyError:
            similarity_scores[word] = (i,-1)
       
    for key,val in similarity_scores.items():
        if val == max(list(similarity_scores.values())):
            return max(list(similarity_scores.values()))[0]


def run_similarity_test(filename : str0) -> str:
    '''Return percentage of questions on which most_similar_word()
    guesses the answer correctly using the semantic descriptors
    stored in semantic_descriptors'''

    global correct
    
    with open(filename) as file:
        for num,line in enumerate(file,1):
            line = line.strip('\n').split()
            prediction = most_similar_word(line[0], line[1:])
            print('#{} Word : {}, Predicted : {}, Correct : {}'.format(num,line[0],prediction,line[1]))
            if prediction == line[1]:
                correct += 1

semantic_descriptors = {}
correct = 1

if __name__ == "__main__":

    files = os.listdir('Text')
    
    for file in files:
        with open(file) as text:
            for line in text:
                semantic_descriptors = build_semantic_descriptors(get_sentence_lists(line))

    run_similarity_test('test.txt')
        
    print('\nThe program predicted {:.3f}% of the synonyms correctly'.format(correct/40*100))
