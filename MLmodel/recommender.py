import tensorflow as tf
import csv
import numpy as np
import os
from sklearn.metrics.pairwise import pairwise_distances
import pandas as pd


HEIGHT = 224
WIDTH = 224
CHANNELS = 3

model = tf.keras.models.load_model(os.getcwd()+'\MLmodel\FinalFashion.h5')
model.compile(optimizer = tf.keras.optimizers.Adam(), 
                loss = 'categorical_crossentropy', 
                metrics = ['accuracy'])


def prepareImg(filename):
    image_string = tf.io.read_file(filename)
    image_decoded = tf.image.decode_jpeg(image_string, channels=CHANNELS)
    image_resized = tf.image.resize(image_decoded, [HEIGHT, WIDTH])
    image_normalized = image_resized / 255.0
    image_for_model = np.expand_dims(image_normalized, axis=0)
    return image_for_model

def readEmbedding():
    isifile = []
    with open(os.getcwd()+"\MLmodel\shirt_embedding.csv", 'r', encoding='UTF8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        line_count = 0
        for row in csv_reader:
            isifile.append(row)

    ids = []
    features = []
    for prediction in isifile:
        ids.append(prediction[0])
        features.append([float (x) for x in prediction[1:]])
    return ids,features


def getCosine_sim(feature_list):
    # Calcule DIstance Matrix
    cosine_sim = 1-pairwise_distances(pd.DataFrame(np.array(feature_list)), metric='cosine')
    return cosine_sim

def get_recommender(img, top_n = 6):
    pre = model.predict(prepareImg(img))
    ids,feature_list = readEmbedding()
    feature_list.insert(0,pre[0])
    cosine_sim = getCosine_sim(feature_list)
    sim_scores = list(enumerate(cosine_sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    index_rec  = [i[0]-1 for i in sim_scores]
    index_sim  = [i[1] for i in sim_scores]
    id_rec = [int(ids[id]) for id in index_rec]
    return id_rec, index_sim

def recommend(img, top_n = 6):
    idx_rec, idx_sim = get_recommender(img, top_n = top_n)
    print("Recommendation Similarity: ",idx_sim)
    return idx_rec, idx_sim
# recommend(os.getcwd()+'\MLmodel\img1.jpg')