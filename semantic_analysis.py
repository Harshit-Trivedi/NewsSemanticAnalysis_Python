import csv
import math
import os
import pymongo

# setup connection to mongoDB
host = "mongodb://localhost:27017/"
database = "Asgmt3"
my_client = pymongo.MongoClient(host)
my_db = my_client[database]
data = my_db.news
newsList = data.find()

# lowercase every word, so that search result are optimum. I have also lower cased every word in the documents.
search_word = ["canada", "university", "dalhousie university", "halifax", "business"]
os.makedirs('News')             # create a new directory to store all news documents and tables
fileIndex = 0                   # will use this index to create multiple documents
for item in newsList:
    fileIndex = fileIndex + 1
    # creating N number of documents in the new directory named News
    output = open('News/file' + str(fileIndex) + '.txt', 'wb')
    if item["title"] is not None:
        # writing news Title in the document
        output.write("Title:" + item["title"] + "\n")
    if item["description"] is not None:
        # writing news Description in the document
        output.write("Description:" + item["description"] + "\n")
    if item["content"] is not None:
        # writing news Content in the document
        output.write("Content:" + item["content"] + "\n")
    output.close()
N = str(fileIndex)                          # N = total number of documents
print "Created " + N + " documents"
print "N = " + N + "\n"

document_number = 0                         # will be used to check if all documents are processed
df = 0                                      # Document containing term
os.chdir('News/')                           # going into 'News' directory which has the N number of documents
file1 = open("semantic_pt1.csv", "wb")      # creating a new file for df, N/df and Log10(N/df)
writer1 = csv.writer(file1)
writer1.writerow(["Total Documents", N])
writer1.writerow(["Search Query", "Document containing term(df)", "Total Documents(N)/ number of documents term "
                                                                  "appeared (df)", "Log10(N/df)"])
for word in search_word:
    # iterating through all the N documents in the 'News' directory (current directory)
    # syntax reference: http://carrefax.com/new-blog/2017/1/16/draft
    for filename in os.listdir(os.getcwd()):
        document_number = document_number + 1
        # reading all documents for the search word 'Canada'
        with open('file' + str(document_number) + '.txt', 'r') as f:
            # terminating when all documents are processed
            if document_number == int(N):
                break
            f_reader = f.readlines()
            for lines in f_reader:
                if word in lines.lower():       # lowercase every word, so that search result are optimum
                    # incrementing value when match found
                    df = df + 1
                    break
    # computing log reference: https://www.tutorialspoint.com/python3/number_log10.htm
    writer1.writerow([word, df, str(document_number) + "/" + str(df), math.log10(document_number / df)])
    document_number = 0
    df = 0
print "File with table 1 created, file name = News\\semantic_pt1.csv\n"
file1.close()

# table2 (Canada appeared in, Total words m, frequency f)
file_no = 0
frequency = 0               # find frequency of search word
max_frequency = 0           # find maximum frequency of search word
doc_hq = 0                  # document with highest frequency
relativeFrequency = 0
highest_article = 0         # document with highest relative frequency
file2 = open("semantic_pt2.csv", "wb")
writer = csv.writer(file2)
# writing the first row in output file
print "File with table 2 created, file name = News\\semantic_pt2.csv\n"
writer.writerow(["Term", "Canada"])
# writing the second row in output file
writer.writerow(["Canada appeared in below documents", "Total Words(m)", "Frequency"])
# iterating through all the N documents in the 'News' directory
for filename in os.listdir(os.getcwd()):
    file_no = file_no + 1
    # break when all files are read and iterated
    if file_no == int(N) + 1:
        break
    # counting the total of 'Canada' in respective file
    sum = 0
    # reading through all the news documents
    with open('file' + str(file_no) + '.txt', 'r') as f:
        f_reader = f.readlines()
        for lines in f_reader:
            res = sum
            sum = res + len(lines.split())      # tracking total words (m)
            if "canada" in lines.lower():
                frequency = frequency + 1
    if frequency != 0:
        writer.writerow(['file' + str(file_no) + '.txt', sum, frequency])
        if frequency > max_frequency:
            max_frequency = frequency
            doc_hq = file_no                    # document with highest frequency of 'Canada'
        if float(frequency) / float(sum) > relativeFrequency:
            relativeFrequency = float(frequency) / float(sum)
            highest_article = file_no           # document with highest relative frequency
    frequency = 0
print "Document having the highest occurence of the word 'Canada': file" + str(doc_hq) + ".txt\n"
print "News document having the highest relative frequency (" +str(relativeFrequency)+") is : file" + str(highest_article) + ".txt.\n"
print "It's contents are:"
with open('file' + str(highest_article) + '.txt', 'r') as f:
    # printing news article that has the highest relative frequency
    print f.read()
file2.close()
