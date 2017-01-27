import gensim

model = gensim.models.Word2Vec.load('brown_model')
print model.most_similar('mother')
print "#######"
print model.most_similar('king')
print "######"
print model.most_similar(positive=['breakfast', 'lunch'])
print model.doesnt_match("breakfast cereal dinner lunch".split())
print model.doesnt_match("cat dog table".split())

print len(model['human'])
