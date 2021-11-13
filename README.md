# book-to-wordcloud

This tool can be used to generate a word cloud by providing the public domain book name. Book name will be searched from project gutenberg's website and appropriate book will be downloaded in text format. After downloading the book in text format, licence information is removed for better accuracy. Book text will be processed and based on the frequency of each word, word cloud will be generated as "image.png" file in the working directory.




## Installation

Activate python virtualenv and run following command to install the requirements:

```
pip install -r requirements.txt
```
    
## Usage

After activating the virtualenv, run the script file with book name:
```
python script.py [book name]
```

After running the script, book will be downloaded in text format, will be processed and word cloud image will be generated in current directory.

## Screenshot
<img width="1334" alt="Screenshot 2021-11-13 at 10 56 58 PM" src="https://user-images.githubusercontent.com/28351545/141653274-126b10bd-2977-4e2c-844c-ce2817ad0a34.png">

