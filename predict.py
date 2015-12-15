from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row


conf = SparkConf().setAppName('TriWordCount')
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

trigrams = sc.textFile('hdfs:///users/rocks1/12307130174/spark_probabilities_smoothed01/*')

trigrams = trigrams.map(lambda line: eval(line)) \
                        .map(lambda t: Row(word0 = t[0][0], word1=t[0][1], word2=t[0][2], prob=t[1]))

schemaTrigram= sqlContext.createDataFrame(trigrams)
schemaTrigram.registerTempTable("trigram")

sqlContext.cacheTable("trigram")
#schemaTrigram.cache()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("",54899))
s.listen(5)

while True:
    #word0, word1 = raw_input(">").split()
    print "in loop"
    client, _ = s.accept()
    print "acccpeted"
    recved = client.recv(1024)
    print "recived"
    #word0, word1 = "change", "the"
    word0, word1 = recved.strip().split()
    print "word received"
    query = "SELECT word2 FROM trigram WHERE word0='%s' AND word1='%s' ORDER BY prob LIMIT 100" % (word0,word1)
    print query
    candidate_words = sqlContext.sql(query).map(lambda p : p.word2)
    print "query make"

    client.send(str(' '.join(candidate_words.collect()) + '\n'))
    print "sended"


    
        

