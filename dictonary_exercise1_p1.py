# Problem 1
def main():
    # Open the file Kennedy.txt
    infile = open("Kennedy.txt")

    # Create an empty list to store each line of the text file as an element.
    file_lines = []

    # Append each line into file lines list.
    for line in infile:
        file_lines.append(line)

    # Uses two different functions to obtain each word and the lines the word in stated in. 
    words_in_lines = create_word_dict(file_lines)
    print(words_in_lines)

    # Sort the words in alphabetical order and their line number progressively.
    word_line_nums = sorted([(word, sorted(list(file_lines))) for word, file_lines in words_in_lines.items()])
    print(word_line_nums)

    # Closes the Kenneday.txt file.
    infile.close()

    # Opens an outfile that is a txt file that contains each word in the exerpt 
    # and the lines which the word is mentioned. 
    outfile = open("word_index.txt","w")

    # For loop to go through each word and the lines the word is mentioned.
    for word, lines in word_line_nums:

        # Writes each word to the out file/
        outfile.write(word + ": ")

        # Nested for loop to write each line number that the word is mentioned in.
        for line_number in lines:

            # Writes the line numbers to each word in the outfile.
            outfile.write(str(line_number) + " ")

        # Create a separate line for each word and their line numbers. 
        outfile.write("\n")

    # Close the outfile when finished with the program. 
    outfile.close()

# Function to create the words in the txt file into a dictionary.
def create_word_dict(file_lines):

    # Counter variable to iterate through each line. 
    line_number = 1

    # Create an empty dictionary to store each word in the txt file.
    words_in_lines = {}

    # For loop to interate through each line in the file.
    for line in file_lines:

        # Strips each line for the words and separates each word.
        words = line.strip().lower().split()

        # Runs a function to find the lines where each word is used.
        find_word_lines(words,words_in_lines,line_number)

        # Once a line is iterated through, this will move on to the next line.
        line_number += 1

    # Return the dictionary.
    return words_in_lines

# Function to find the lines where each word is mentioned.
def find_word_lines(words,words_in_lines,line_number):

    # For loop go iterate through each word in each line.
    for word in words:

        # Conditional statement to indicate if a word is in a ceratain line,
        # to add the line numbers where the word is present. 
        if word in words_in_lines:
            words_in_lines[word].add(line_number)
        else:
            words_in_lines[word] = {line_number}

main()

