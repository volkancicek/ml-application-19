# Reference Matching
A record linkage solution for academic references using bi-directional recurrent neural networks (RNNs) with long short term
memory (LSTM) hidden units and word embeddings.


## Commands
create_embeding_data <br> params:  glove ../../ml-application-19/glove_model2.txt -d ../data/embeddings/ <br>
convert-text <br> params:  ../data/raw/dblp-scholar ../data/converted/dblp-scholar ../data/embeddings/glove-300.map -v <br>
make-split <br> params:  ../data/converted/dblp-scholar/ ../data/split/dblp-scholar/ -npr 100 -v <br>

To run with fasttext:

Download https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M.vec.zip put in  *ml-application-19/data/* then run <br>
**create_embeding_data** <br> **params:**<br>  *fasttext ../../ml-application-19/data/crawl-300d-2M.vec -d ../data/embeddings/* <br>
**convert-text**<br> **params:** <br>  *../data/raw/crossref/cermine/ ../data/converted/crossref/cermine/ ../data/embeddings/fasttext-300.map -v* <br>
**make-split**<br> **params:**<br> *../data/converted/crossref/cermine/ ../data/split/crossref/cermine/ -npr 100 -v* <br>


