# ml-application-19
Machine Learning Application Project Seminar for SS19 West

create_embeding_data <br> params:  glove ../../ml-application-19/glove_model2.txt -d ../data/embeddings/ <br>
convert-text <br> params:  ../data/raw/dblp-scholar ../data/converted/dblp-scholar ../data/embeddings/glove-300.map -v <br>
make-split <br> params:  ../data/converted/dblp-scholar/ ../data/split/dblp-scholar/ -npr 100 -v <br>
