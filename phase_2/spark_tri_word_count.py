from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('TriWordCountProbability')
sc = SparkContext(conf=conf)

tri_words = tri_word_file.map(lambda line: tuple(line.strip().split(" ")))

tri_counts = tri_words.map(lambda tri_word: (tri_word, 1)) \
                      .reduceByKey(lambda a, b: a + b) \
                      .map(lambda word_count: (word_count[0][:2], (word_count[0][2], word_count[1])))
tri_counts.cache()

bi_counts = tri_counts.map(lambda tri_word: (tri_word[0], tri_word[1][1])) \
                      .reduceByKey(lambda a, b: a + b)

counts_join = tri_counts.join(bi_counts)

def get_probability(key_value):
    return ((key_value[0] + (key_value[1][0][0],)), float(key_value[1][0][1])/float(key_value[1][1]))

probabilities = counts_join.map(get_probability)

probabilities.saveAsTextFile("hdfs://cluster.hpc.org:9000/users/rocks1/12307130174/spark_probabilities01")
