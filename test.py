
import pandas as pd
import numpy as np

def loadFont():
    glove_path='/home/zhangwenqiao/Project/VideoQA/data/msvd_qa/word_embedding.npy'
    vocab_path='/home/zhangwenqiao/Project/VideoQA/data/msvd_qa/test_word.txt'
    glove = pd.read_csv(
        glove_path, sep=' ', quoting=csv.QUOTE_NONE, header=None)
    glove.set_index(0, inplace=True)
    # load vocabulary.
    vocab = pd.read_csv(vocab_path, header=None)[0]

    embedding = np.zeros([len(vocab), len(glove.columns)], np.float64)
    not_found = []
    for i in range(len(vocab)):
        word = vocab[i]
        if word in glove.index:
            embedding[i] = glove.loc[word]
        else:
            not_found.append(i)
    print('Not found:\n', vocab.iloc[not_found])

    embedding_avg = np.mean(embedding, 0)
    embedding[not_found] = embedding_avg

    np.save(embedding_path, embedding.astype(np.float32))

if __name__ == '__main__':
    loadFont()

