# video-qa-FAAAN

This is an implementation of [Frame Augmented Alternating Attention Network for Video Question Answering] with Tensorflow. 

### Codes

Before Training

- preprocess_msrvttqa.py : extract feature vectors for train(image features, question and answer features) for msrvttqa dataset. Also build word2ix and ix2word for questions and answers.
- preprocess_msvdqa.py : extract feature vectors for train(image features, question and answer features) for msvdqa dataset.

Models and Train & Test codes(Tensorflow is used)

- config.py : configuration file 
- faster_rcnn: extract the spatial regions for question to region attention.
- model
  - faa.py : a faa model which do not have attention mapping
  - run_faa.py : a code for training and testing.





