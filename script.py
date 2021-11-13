from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import os,re,sys
import requests
import urllib.parse

#TODO: Add command link feature for providing book name

book_name=" ".join(sys.argv[1:])
if not book_name:
    # remove it
    book_name = "as a man thinketh"
print("bookname: '"+book_name+"'")

# ************************************************************************************************
# To grab book from project gutenberg
# ************************************************************************************************

query_url = "https://www.gutenberg.org/ebooks/search/?"+urllib.parse.urlencode({'query':book_name})
response = requests.get(query_url)
# print(response.content)

match = re.search(r'<li class="booklink">\\n<a class="link" href="/ebooks/(\d+)',str(response.content))
if match:
    book_number = match.group(1)
    print("FOUND!!! Ebook number "+book_number)

query_url = "https://www.gutenberg.org/files/"+book_number
response = requests.get(query_url)
# print(response.content)

match = re.search(r'alt="\[TXT\]"></td><td><a href="(.*\.txt)">',str(response.content))
if match:
    a_link_text = match.group(1)
    txt_link="https://www.gutenberg.org/files/"+book_number+"/"+a_link_text
    print("Link: "+txt_link)

content = requests.get(txt_link).content

try:
    os.remove('book.txt')
except:
    pass

open('book.txt', 'wb').write(content)
print("Downloaded")
# ************************************************************************************************
# Book is saved as book.txt at this point
# Process the text and save wordcloud image
# ************************************************************************************************
comment_words = ""
stopwords = set(STOPWORDS)

with open('book.txt', 'r') as file:
    content = file.read()

copyright_start = re.search(r"\*\*\* START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK", content)
if copyright_start:
    a=content.count('\n', 0, copyright_start.start())+1
    content=content.split("\n",a)[a]

copyright_end = re.search(r"\*\*\* END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK", content)
if copyright_end:
    a=content.count('\n', 0, copyright_end.start())
    content="\n".join(content.split("\n",a)[:a])

# try:
#     os.remove('book.txt')
# except:
#     pass
# finally:
#     open('book.txt', 'w').write(content)

tokens = content.split()

# Converts each token into lowercase
for i in range(len(tokens)):
    tokens[i] = tokens[i].lower()

comment_words += " ".join(tokens) + " "

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color="white",
    stopwords=stopwords,
    min_font_size=10,
).generate(comment_words)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

# plt.show()

plt.savefig(os.path.join(os.getcwd(),"image.png"))
