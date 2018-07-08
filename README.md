#Mychatbot
Chat bot for ABC company in place of technical support agents using Keras-tensorflow

#keras-chatbot-tensorflow
Simple keras chat bot using seq2seq model with Flask serving web

The chat bot is built based on seq2seq models, and can infer based on either character-level or word-level.

The seq2seq model is implemented using LSTM encoder-decoder on Keras.

Notes
GloVe word encoding of the chatbot gives the best performance.

Usage
Environment setup:

1.Install Anaconda 4.5.4 
2.Open Anaconda command prompt 
3.Create new environment and activate it by running following commands:

```bash

conda create -n tensorflow pip python=3.5
 
```
```bash

conda activate tensorflow
 
```
 
4.Install Git in Anaconda by using following command:

```bash

conda install -c anaconda git 
 
```

Run the following command to clone the source code from github

```bash

git clone https://github.com/Anoopparjanya/Mychatbot Mychatbot

```


Run the following command to install the keras, flask and other dependency modules:

```bash

pip install --user -r requirements.txt
```

If tensorflow is not installed by the above command,run the following command:

```bash

pip install --ignore-installed --upgrade tensorflow 

``` 


Since keras by default uses theano backend,to work on tensorflow backend run the following command:

```bash

set KERAS_BACKEND=tensorflow

```

Also install all nlkt data packages by using the following command:

```bash

python -m nltk.downloader all 

```

The chat bot models are train using a data set and are available in the"chatbot_train/models" directory. During runtime, the flask app will load these trained models to perform the chat-reply

Training (Optional)

As the trained models are already included in the "chatbot_train/models" folder in the project, the bot training is not required. However, if you like to tune the parameters of the seq2seq and retrain the models, you can use the following command to run the training:

```bash

cd chatbot_train

python Anoop_word_seq2seq_glove_train.py

```


The above commands will train seq2seq model using data on the character-level and store the trained model in "chatbot_train/models/Anoop/char-**"

To verify the trained model,change the directory to chatbot_web and run the following command:

To navigate to previous folder,run the following command in Anaconda command Prompt:

```bash

cd..

```



```bash

cd chatbot_web

python Anoop_word_seq2seq_glove_predict.py

```

Running Web Api Server
Goto chatbot_web directory and run the following command:

```bash

python flaskr.py

```

Now navigate your browser to http://localhost:5000 and you can try out predictor built with the following trained seq2seq model:

Word-level seq2seq models (GloVe Encoding)
A simple chat bot is displayed in http://localhost:5000 when you can enter questions and click on send,the bot will reply you automatially with minimum error.
