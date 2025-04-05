import re
from collections import Counter

from sklearn.feature_extraction.text import TfidfVectorizer
from celery import shared_task


@shared_task
def process_document_statistics(document_id):
    from .models import Document
    document = Document.objects.get(id=document_id)
    
    with document.file.open('r') as file:
        text = file.read().lower()

    
    cleaned_text = re.sub(r'[^а-яёa-z\s\.]', '', text)

    words = cleaned_text.replace('.', '').split()
    tf_counts = Counter(words)

    sentences = [sentence.strip() for sentence in cleaned_text.split('.') if sentence.strip()]
    vectorizer = TfidfVectorizer()
    vectorizer.fit(sentences)

    idf_values = dict(zip(vectorizer.get_feature_names_out(), vectorizer.idf_))

    stats = []
    for word, tf in tf_counts.items():
        idf = idf_values.get(word, 0)
        stats.append({'слово': word, 'tf': tf, 'idf': idf})

    top_50_stats = sorted(stats, key=lambda x: x['tf'], reverse=True)[:50]

    document.statistics = sorted(top_50_stats, key=lambda x : x['idf'], reverse=True)
    document.save()