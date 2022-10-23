import nltk
from nltk.corpus import stopwords

stop = stopwords.words('english')

def nltk_process(document):
    document = " ".join([i for i in document.lower().split() if i not in stop])
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def main():
    file = open('article.txt', 'r')
    document = file.read()
    sentences = nltk_process(document)
    print(sentences)

if __name__ == '__main__':
    main()