# D7047E-Advanced-DL

Exercise 1

Accuracy
![Accuracy](https://user-images.githubusercontent.com/48216230/161533769-a2d6cf90-a68c-4f07-9ec1-078d41718c61.jpg)

Loss
![Loss](https://user-images.githubusercontent.com/48216230/161533800-e3efac80-3434-4423-9cb4-2d743ba9ca71.jpg)
------------------------------------------------------------------------------------------------------------------


Exercise 2

1.1.1

Newly trained model: 67% accuracy

Fine tuning: 62% accuracy

Feature Extraction: 83% accuracy

Difference between Fine tuning & Feature extraction:

Fine tuning: In the fine-tuning strategy all weights are changed when training on the new task except for the weights of the last layers for the original task.

Feature Extraction: In the feature extraction strategy only the weights of the newly added last layers change during the training phase.

1.1.2

Train a CNN on the mnist dataset: 95% accuracy

Use pre-trained CNN on SVHN dataset: 77% accuracy


Exercise 3

Untrained network t-sne and then pca

![7ef483b4-967d-47cd-8067-ea70115647ba](https://user-images.githubusercontent.com/47854778/164675688-bd317899-c16c-4115-9f60-79e8c516f788.png)

![f2ba9bd9-8b08-4bdc-8bc1-e22b44af6b36](https://user-images.githubusercontent.com/47854778/164675721-4c7763d0-2161-414b-9c62-dc652846e9e8.png)


Trained network t-sne and then pca

![9aa2ee29-3ee6-44d3-b120-4d42e691d998](https://user-images.githubusercontent.com/47854778/164676078-26bfa841-a774-4c85-a02d-72956b278d7d.png)

![bb73cf2d-833a-4828-92a0-19813a8b2790](https://user-images.githubusercontent.com/47854778/164676084-59e1d147-9b42-4a78-9002-ff8735b9b766.png)


Exercise 4

Task-1:  The change in perplexity during training of CharRNN on 2000 epochs
![Perplexity of 2000 epochs](https://user-images.githubusercontent.com/48216230/164911460-5e82081f-7698-4c9b-a60c-3d66e4f6b74c.png)

Task-4:  The change in perplexity during training of WordRNN on 2000 epochs
![Word-Perplexity of 2000 epochs](https://user-images.githubusercontent.com/48216230/164911464-c948f322-841b-4a45-b2fd-bb5d12bcd3e1.png)

Generated output sequences for tasks 2, 3 & 4 can be found in Labs/Lab-4/Results
