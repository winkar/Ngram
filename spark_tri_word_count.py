from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('TriWordCount')
sc = SparkContext(conf=conf)

tri_word_file = sc.textFile('hdfs://cluster.hpc.org:9000/users/rocks1/12307130174/wiki_triword00/part-00000')

counts = tri_word_file.map(lambda line: tuple(line.strip().split(" "))) \
                      .map(lambda tri_word: (tri_word, 1)) \
                      .reduceByKey(lambda a, b: a + b)

counts.saveAsTextFile("hdfs://cluster.hpc.org:9000/users/rocks1/12307130174/spark_tri_word_count03")
