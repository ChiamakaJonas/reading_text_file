# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}




def read_file_content(filename):
    # [assignment] Add your code here 
    # f = open("story.txt", "r")
    with open("story.txt") as f:
        return f.read()


    
# read_file_content()



def count_words():
    text = read_file_content("./story.txt")
     # [assignment] Add your code here
    story_list = text.split()
    count_dict = {}
    for word in story_list:

        count_dict[word] = story_list.count(word)
    return count_dict


count = count_words()

print(count)



    # return {"as": 10, "would": 20}