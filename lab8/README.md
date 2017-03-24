# Lab8

* inputs = Input(shape=(maxlen,))
* x = inputs
* x = Embedding(max_features, 128, dropout=0.2)(x)
* x = Flatten()(x)
* x = Dense(1)(x)
* predictions = Activation("sigmoid")(x)
  
* x = Dense(64)(x)
* x = PReLU()(x)
* x = dropout(0.2)(x)
* The result for first step is 0.8278
