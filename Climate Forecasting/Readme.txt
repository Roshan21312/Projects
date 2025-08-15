In this project I have implemented LSTM MODEL on multivariate features to predict nxt temperature based on 13 features provided.

Overview of LSTM model :
It is a version of RNN which is capable of holding long term memory by utilizing an architecture of Forget Gate,Input Gate,Output Gate.

1) Forget Gate: Determines how much of Long-term memory (Cell state C(t-1)) to keep. It takes new data-point (X(t)) and previous hidden state (h(t-1)) and applies sigmoid function to their linear combination and gets a value between 0-1 which acts as weight for old cell state and gives us f(t)*C(t-1).

2) Input Gate: Determine how much of new information to store in cell. It computes a weight(using sigmoid) and applies it to candidate cell state(created using tanh function on linear combination of new information (X(t)) and previous hidden state).Then we combine this weighted short-term memory(candidate cell state) and weighted long-term memory(Updated cell state from Forget Gate). Which gives us C(t) = i(t)*c(t) + f(t)*C(t-1).

3) Output Gate:Determines the next hidden state/Output. Similar to DNN, here we apply an activation function(Sigmoid) to combination of new information(x(t)) and hidden state(h(t-1)) which acts as a weight. we apply tanh to our updated cell state (C(t)).this weighted multiple of updated cell state gives us our new hidden state/output.
