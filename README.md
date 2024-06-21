# Image-Classifier

This project is designed to classify whether an image of a shirt belongs to Sport or Náutico, which are football teams from Recife, the capital of Pernambuco, a state in Brazil. The classification is performed using the EfficientNet model for image classification. The project also incorporates web scraping techniques to gather images from the internet for training and testing the model.


## First Step
Clone the repository on your machine and run the command: 

```
pip install -r requirements.txt
```
## Second Step
```
project-root/
├── imagens/
│   ├── scraping/
│   │   ├── train/
│   │   │   ├── sport/
│   │   │   │   ├── sport1.jpg
│   │   │   │   ├── sport2.jpg
│   │   │   │   └── ...
│   │   │   ├── nautico/
│   │   │   │   ├── nautico1.jpg
│   │   │   │   ├── nautico2.jpg
│   │   │   │   └── ...
│   │   ├── val/
│   │   │   ├── sport/
│   │   │   │   ├── sport1.jpg
│   │   │   │   ├── sport2.jpg
│   │   │   │   └── ...
│   │   │   ├── nautico/
│   │   │   │   ├── nautico1.jpg
│   │   │   │   ├── nautico2.jpg
│   │   │   │   └── ...
│   ├── test/
│   │   ├── sport/
│   │   │   ├── sport1.jpg
│   │   │   ├── sport2.jpg
│   │   │   └── ...
│   │   ├── nautico/
│   │   │   ├── nautico1.jpg
│   │   │   ├── nautico2.jpg
│   │   │   └── ...
```
## Third Step

Train the model by running the file below:
ModelTrain.ipynb
The ModelTrain.ipynb will train the model using the images in imagens/scraping/train for training and imagens/scraping/val for validation. The trained model will be saved as modelo_camisas_sport_nautico.pth.

## Fourth Step

To evaluate the trained model with new images, place the new images in the imagens/test directory structured as follows:
```
imagens/test/
├── sport/
│   ├── sport1.jpg
│   ├── sport2.jpg
│   └── ...
├── nautico/
│   ├── nautico1.jpg
│   ├── nautico2.jpg
│   └── ...
```

Then, run the following file to evaluate the model:
LoadandTestModel.ipynb
The evaluate.py script will load the trained model from modelo_camisas_sport_nautico.pth and evaluate the new images in imagens/test. It will print the evaluation metrics and show a confusion matrix.

## Troubleshooting

1. Ensure your image directories are correctly structured.
2. Check that you have the required permissions to read/write files in the specified directories.
3. If CUDA is not available, the script will automatically switch to CPU, which might be slower.

