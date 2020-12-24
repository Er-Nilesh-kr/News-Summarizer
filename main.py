import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article


def summarize():
    url = url_text.get('1.0', "end").strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert(
        '1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity>0 else "negative" if analysis.polarity<0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x650')

title_label = tk.Label(root, text="Title")
title_label.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

author_label = tk.Label(root, text="Author")
author_label.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

publication_label = tk.Label(root, text="Date of Publication")
publication_label.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

summary_label = tk.Label(root, text="Summary")
summary_label.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

url_label = tk.Label(root, text="URL")
url_label.pack()

url_text = tk.Text(root, height=1, width=140)
url_text.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()
