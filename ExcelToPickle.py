import pickle
import pandas as pd

df = pd.read_csv('words.csv', encoding = "ISO-8859-1")
print("df.shape : ",df.shape)

words_list = []
for index, row in df.iterrows():
    words_list.append(row['cleaned_lower'])
#     print(row['cleaned_name'])

print("Words from Excel :",len(words_list))

custom_words = ['How', 'can', 'What', 'When', 'Which', 'would', 'should', 'Why', 'being', 'do', 'to', 'my', 'i', 'know','of', 'how', 'do', 'they', 'that', 'the', 'I', 'a', 'i', 'o', 'u', 'you', 'yours', 'A', 'E', 'I', 'U', 'an', 'Whats', 'whats']
print("custom_words : ",len(custom_words))

words_list.extend(custom_words)

#Remove Duplicates 
words_list = list(set(words_list))
words_list.sort()
# print(stop_words_list)

filepath = 'words.txt'
filepath_pickle = "words.pickle"

print("There are {} words in total ".format(len(words_list)))

f = open(filepath_pickle, 'wb')   # 'wb' instead 'w' for binary file
pickle.dump(words_list, f, -1)       # -1 specifies highest binary protocol
f.close() 

print("Pickle created {}".format(filepath_pickle))

print("printing few contents of {}".format(filepath_pickle))


objects = []
with (open(filepath_pickle, "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break

print("{} words written to pickle file ".format(len(objects[0])))        
#Display how contents of pickle look like
print(objects[0][0:5])


