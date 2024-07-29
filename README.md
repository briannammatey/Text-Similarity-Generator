# TextSimulatorGenerator
The point of this code is to generate simularity percentages between styles of texts, using dictionaries and file processing.

## Motivation
The motivation behind this code, is so anyone can explore and find similarities between texts they like. For example I tested this code using Lin Manuel Miranda musicals and compared them with each other

## Features
### compare_dictionaries function
compares the two dictionaries d1 and d2  and returns their log simularity score;
Inputs:d1 and d2
### stem function
accepts a string as a parameter and returns the stem.
### clean_txt function
takes in a text and removes punctuations, splits the txt and lowercases all the letters
### TextModel class
 constructs a new TextModel object by accepting a string
model_name as a parameter and initializing , 
name: a string that is a label for this text model
words- a dictionary that records the number of times each word appears in the text
word_lengths- a dictionary that records  the numer of times each word length appears
### add_string function
adds a string of text s to the model by augmenting the feature dictionaries defined in the constructor. 

### add_file function
 adds all of the text in the file identified by filename to the model. It should not explicitly return a value.
input:filename
### save_model function
 saves the Textmodel object self by writing its various feature dictionaries to file
### read model function
   reads the stored dictionaries for the TextModel object from their files and assigns them to attributes
### similarity_scores
 computes and returns a list of log similarity scores measuring the simularity of self and other
           
### classify function
compares TextModel object to other source TextModel objects and determines which of these other Text Models is morelikely source of Text Model
inputs: source1; source2
### test function
 given function to tests the code
### run_tests function
 runs tests to compares sources and identify the classification score to other texts
 ##Test example
 This is when compring scripts from musicals "In the Heights", "Hamilton", "Encanto", "Moana", and "BeetleJuice"

 
