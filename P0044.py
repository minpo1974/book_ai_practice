# pip install gensim
# conda install gensim
# pip install python-Levenshtein
# conda install python-Levenshtein
from gensim.models import word2vec

sentences = word2vec.Text8Corpus('wikiko_iso8859_1.gubun')
model = word2vec.Word2Vec(sentences, sg=1, vector_size=100, window=5)
model.save("wikiko.model")