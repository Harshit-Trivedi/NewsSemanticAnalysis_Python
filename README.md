# Overview

I have considered 700 news articles for this. I have fetched them from my MongoDB locally. Since the news articles are already cleaned, I have not cleaned them again.
I have considered 700 news articles and have created 700 documents (.txt format). These are created in a new directory named “News”. This new directory will be created 
in the project’s root directory. All these 700 documents have the title, description and content of the respective news article. Next, I calculated the TF-IDF 
(term frequency and inverse document frequency). For searching I have converted both the search words and the file contents in lower case in order to retrieve consistent
results. I have stored the results in a separate csv file named: semantic_pt1.csv. This file will also be found in the “News” directory. Also, the total documents (700)
will be displayed in the console and the output file (semantic_pt1.csv) as well. The data for total words and frequency of the word “Canada” is stored in a separate csv
file named: (semantic_pt2.csv). This file will also be found in the “News” directory. I also found that the document file18.txt that has the highest occurrence of the 
word “Canada”. Once calculated, this result is also displayed on the console. Finally, I have calculated and found that the news article having the highest relative 
frequency is document named: file562.txt. Once calculated, it will be displayed in the console as well. Also, the contents of this news article will be displayed on the 
console.
