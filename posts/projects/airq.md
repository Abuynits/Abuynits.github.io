---
title: "AirQ"
summary: "LSTM / seq2seq model for air quality prediction"
coverImage: "/assets/projects/airq/airq_overview.png"
order: 5 
---

**Output from a seq2seq model for predicting 10 time steps**

[Devpost link](https://devpost.com/software/airq)

## Background

This was a Hackathon project for BoilerMake X.

I wanted to do a hackathon and I really didn't want to do web dev... so I decided to find a fun dataset and mess around with it for 48 hours. I had a blast and won **first place** for [Dagshub](https://dagshub.com/)!


## What it does
This is a LSTM and seq2seq model (transformer-like model) that predicts specified air quality metrics using input and output features (data columns). One can select the input feature(s), desired output feature(s), loookback range, and prediction range to see which input features have the most weight in determining the output features. One can also experiment with adjusting the models, their architecture, and other hyper parameters without worry about the the implementation. It is built using Pytorch, with DVC and MLflow to allow for easy testing and augmentation through the constant.py file.

## How it works

### Preparing the data
We started by finding a data set on air quality, which we found in UC Irvine’s data archive. We then preprocessed this data. To do this we first interpolated missing/malformed data points, and then normalized the data between 0 and 1 to make it ready for training. After preparing the data, we split it into training and validation sets and batched it. We then created custom datasets and loaded them into dataloaders to be used by our model.

### Designing the model:
For our model design, we initially started with an LSTM, but after training it, we noticed that even with any combination of hidden layers or lstm cells, the model would struggle with predicting two or more time steps ahead which is why we switched to using a seq2seq model, commonly used in NLP techniques. Such models are based on an encoder-decoder architecture:

Data is fed to the encoder, and we store the hidden state for the last timestep in the encoder
we take the last input, and the last hidden state, and feed it into the decoder which produce the required hidden states
We pass this through a linear layer to decrease the output dimensions from the hidden size to the desired amount of outputs and a new input state to the model.
This process continues until we generate the required amount of time steps
### Training the model:
#### Learning Rate:

We selected a learning rate of 0.001 and a ExponentialLR scheduler from pytorch with Gamma = 0.99 to exponentially decay the learning rate by gamma as we move through the epochs.

(see more in main.ipynb)

#### Epochs:

We train for 1000 epochs, saving a model whenever we reach a new best validation loss.

#### Optimizer:

We use a MSEloss to calculate the loss between our quantitative outputs.

### Version Control

We use DagsHub with DVC for our data, git for our code, and MLflow to analyze the training results.

Learn more [here](https://devpost.com/software/airq)