# Neural Network for classification of traffics signs.
Dataset Used: GTSRB Dataset (http://benchmark.ini.rub.de/?section=gtsrb&subsection=news).

# Model Summary:
Model: "sequential"   
Test Set Accuracy: 0.9908   
Loss: 0.0833   

| Layer (type)               | Output Shape        |     Param #  |
|----------------------------|---------------------|--------------|
| conv2d (Conv2D)            |None, 28, 28, 32)    |  896         |
|max_pooling2d (MaxPooling2D)|(None, 14, 14, 32)   |    0         |
| flatten (Flatten)          | (None, 6272)        |   0          |
| dense (Dense)              | (None, 128)         |     802944   |
|  dropout (Dropout)         |  (None, 128)        |      0       | 
| dense_1 (Dense)            | (None, 43)          |     5547     |

  Total params: 809,389  
  Trainable params: 809,387  
  Non-trainable params: 0  


# Usage:

## To retrain the model:
`python traffic.py data_directory [model.h5]`

## To make predictions:
`python recognition.py`
