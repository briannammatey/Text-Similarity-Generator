#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 22:31:26 2023

@author: briannamatey
"""
import math
def compare_dictionaries(d1, d2):
    """
    compares the two dictionaries d1 and d2 and
    and returns their log simularity score
    Inputs:d1 and d2
    """
    
    if d1 == {}:
       added_score=-50
    else:
        added_score=0
        total=0
        for w in d1:
            total += d1[w]
            
        for w in d2:
            
            if w in d1:
                added_score += math.log(d1[w]/total) * d2[w]
                
            else:
                added_score += math.log(0.5/total) * d2[w]
             
    return added_score
                
        
        
        
            
            
        



def stem(s):
    """
accepts a string as a parameter
funcyion should return the stem of s
input:s 
    """
    if s[-1]=="s":
        if s[-2:]=="es":
            newstem=s[:-2]
        else:  
            newstem=s[:-1]
         
    elif s[-3:]=='ing':
       
       new=s[:-3]
       if new[-1]==new[-2]:
           newstem=new[:-1]
       else:
           newstem=new
    elif s[-1]=='e':
            newstem=s[:-1]
        
    elif s[-2:]=='er':
        newstem=s[:-2]
    elif s[-1]=='y':
        if s[-2:]=='ly':
            newstem=s[:-2] +'i'
        else:
            newstem=s[:-1] + 'i'
    elif s[-2:]=='ed':
        newstem=s[:-2]
    elif s[-3:]=='ful':
        newstem=s[:-3]
    return newstem
    
        
        




def clean_text(txt):
    """
    removes punctuations, splits the txt
    and lowercases all the letters
    inputs:txt
    """
    cleaned=[]
    words=txt
    words=txt.lower().split()
    for i in range(len(words)):
        for symbol in """.,?"'!;:""":
            words[i]= words[i].replace(symbol, "")
        cleaned+=[words[i]]
    return cleaned
        
def sample_file_write(filename):
     """A function that demonstrates how to write a
     Python dictionary to an easily-readable file.
     inputs:filename
     """
     d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
     f = open(filename, 'w')      # Open file for writing.
     f.write(str(d))              # Writes the dictionary to the file.
     f.close()                    # Close the file.
 
def sample_file_read(filename):
     """A function that demonstrates how to read a
     Python dictionary from a file.
     inputs:filename
     """
     f = open(filename, 'r')    # Open for reading.
     d_str = f.read()           # Read in a string that represents a dict.
     f.close()

     d = dict(eval(d_str))      # Convert the string to a dictionary.

     print("Inside the newly-read dictionary, d, we have:")
     print(d)

                 
    

    
class TextModel:
        """
        constructs a new TextModel object by accepting a string
model_name as a parameter and initializing , name: a string that is a label for this text model
words- a dictionary that records the number of times each word appears in the text
word_lengths- a dictionary that records  the numer of times each word length appears
        """
        def __init__(self, model_name):
            """
            constructer variable to build attributes, name, words, 
            and word lengths
            input:model_name
            """
            self.name=model_name
            self.words={}
            self.word_lengths={}
            self.stems={}
            self.sentence_lengths={}
            self.numbers={}          #added feature
            
            
        def __repr__(self):
          """
          assigns a string representation of the outputs 
          """
          s = 'text model name: ' + self.name + '\n'
          s += '  number of words: ' + str(len(self.words)) + '\n'
          s += '  number of word lengths: '+ str(len(self.word_lengths)) +'\n'
          s += '  number of stems: ' + str(len(self.stems))+ '\n'
          s += '  number of sentence lengths: '+ str(len(self. sentence_lengths))+'\n'
          s += '  number of numbers: '+ str(len(self.numbers))+'\n'
          return s
       
        def add_string(self, s):
                    """
                    adds a string of text s to the model by
                    augmenting the feature dictionaries defined in the constructor. 
                    input: s
                    """
                    punctuation=[',', '.', '!','?']
                    number=['1','2','3', '4', '5', '6', '7', '8', '9', '0']
                    t=s.split()
                    sentence=0
                    for word in t:
                        
                        
                        if word[-1] not in punctuation:
                            sentence+=1
                            
                        else:
                            sentence+=1
                            if sentence not in self.sentence_lengths:
                                self.sentence_lengths[sentence]=1
                                sentence=0
                            else:
                                self.sentence_lengths[sentence]+=1
                                sentence=0
                        if word in number:
                            
                            if word in self.numbers:
                                self.numbers[word]+=1
                            else:
                                    self.numbers[word]=1
        
                        
                    
                    cleaned_string =clean_text(s)
                    #print(cleaned_string)
                    word_list=cleaned_string
        
                    for w in word_list:
                        if w not in self.stems:
                            self.stems[w]=1
                        else:
                            self.stems[w] += 1
                        #if w in self.stems:
                            #self.stems[w] +=1
                        #else:
                            #self.stems[w] =1
                        if w in self.words:
                            self.words[w]+=1
                        else:
                            self.words[w]=1
                        
                        if len(w) in self.word_lengths:
                            self.word_lengths[len(w)]+=1
                        else:
                            self.word_lengths[len(w)]=1
        
        def add_file(self, filename):
            """
           adds all of the text in the file identified by filename to the model. It should not explicitly return a value.
           input:filename
            """

            f = open(filename, 'r', encoding='utf8', errors='ignore')
            for line in f:
                line=line[:-1]
                self.add_string(line)
                
        def save_model(self):
            """
        saves the Textmodel object self by writing its various
        feature dictionaries to file
            """
           
            filename=self.name+'-'+'words'
            file_name=self.name+'-'+ 'word_lengths'
            files_name=self.name+'-' + 'stems'
            filez=self.name + '-' + "sentence_lengths"
            flies=self.name+'-' +'numbers'
            n=open(flies, 'w')
            
            k=open(filez, 'w')
            n.write(str(self.numbers))
            n.close()
            k.write(str(self.sentence_lengths))
            k.close()
            s=open(files_name,'w')
            s.write(str(self.stems))
            s.close()
            
            f=open(filename, 'w')
            
            f.write(str(self.words))
            f.close()
            r=open(file_name, 'w')
            r.write(str(self.word_lengths))
            r.close()
            
        def read_model(self):
            """
            reads the stored dictionaries for the TextModel
            object from their files and assigns them to attributes
        
            """
            filename=self.name+'-'+'words'
            file_name=self.name+'-'+ 'word_lengths'
            files_name=self.name +'-' +'stems'
            filez=self.name + '-' + 'sentence_lengths'
            flies=self.name +'-'+'numbers'
            n=open(flies,'r')
            k=open(filez, 'r')
            s=open(files_name,'r')
            d=open(file_name,'r')
            f=open(filename,'r')
            d5=n.read()
            d4=k.read()
            d3=s.read()
            d2=d.read()
            d1=f.read()
            n.close()
            f.close()
            d.close()
            s.close()
            k.close()
            d5=dict(eval(d5))
            d4=dict(eval(d4))
            d3=dict(eval(d3))
            
            d1=dict(eval(d1))
            d2=dict(eval(d2))
            self.numbers=d5
            self.sentence_lengths=d4
            self.stems=d3
            self.words=d1
            self.word_lengths=d2
            print("Inside the newly-read dictionary, d, we have:")
            print(self.words)
            print(self.word_lengths)
            print(self.stems)
            print(self.sentence_lengths)
            print(self.numbers)
        def similarity_scores(self, other):
            """
            computes and retyurns a list of log similarity
            scores measuring the simularity of self and other
            input:other
            """

            
            list_words=[]
            word_score = compare_dictionaries(other.words, self.words)
            wordlengths_score= compare_dictionaries(other.word_lengths, self.word_lengths)
            stem_score= compare_dictionaries(other.stems, self.stems)
            sentence_lengths=compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
            numbers=compare_dictionaries(other.numbers, self.numbers)
            list_words+= [word_score]+[wordlengths_score] + [stem_score] + [sentence_lengths] +[numbers]
            
            return list_words
        
        def classify(self, source1, source2):
            """
            compares TextModel object to other source TextModel
            objects and determines which of these other Text Models is more
            likely source of Text Model
            inputs: source1; source2
            
            """
            scores1 = self.similarity_scores(source1)
            scores2 = self.similarity_scores(source2)
            print('scores for '+ source1.name +': '  + str(scores1))
            print('scores for '+source2.name +': ' + str(scores2))
            weighted_sum1 = 10*scores1[0] + 5*scores1[1] + 4*scores1[2] + 3*scores1[3]+ 2*scores1[4]
            weighted_sum2 = 10*scores2[0] + 5*scores2[1] + 4*scores2[2] + 3*scores2[3] + 2*scores2[4]
            if weighted_sum1 > weighted_sum2:
                print(self.name,'is more likely to have come from', source1.name)
            else: 
                
                print(self.name,'is more likely to have come from', source2.name)
                
            
def test():
    """ given function to tests the code"""
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

def run_tests():
    """ runs tests to compares sources and identify the classification score to other texts """
    source1 = TextModel('hamilton')
    source1.add_file('hamilton.txt')

    source2 = TextModel('intheheights')
    source2.add_file('intheheights.txt')

    new1 = TextModel('encanto')
    new1.add_file('encanto.txt')
    new1.classify(source1, source2)   
    
    new2 = TextModel('coco')
    new2.add_file('coco.txt')
    new2.classify(source1, source2)     
    
    new3 = TextModel('moana')
    new3.add_file('moana.txt')
    new3.classify(source1, source2) 
    
    new4 = TextModel('beatlejuice')
    new4.add_file('beatlejuice.txt')
    new4.classify(source1, source2) 
    
    
                   
                        
          
          
                  
                
                      