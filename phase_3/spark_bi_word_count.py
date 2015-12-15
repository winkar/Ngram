from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('WikiBiWordCount')
sc = SparkContext(conf=conf)

tri_word_file = sc.textFile('hdfs://cluster.hpc.org:9000/users/rocks1/12307130174/wiki_triword00/part-00000')

counts = tri_word_file.map(lambda line: tuple(line.strip().split(" ")[:2])) \
                      .map(lambda word: (word, 1)) \
                      .groupByKey() \
                      .count()

print "bi_word counts: ", counts
