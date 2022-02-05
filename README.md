#NLP Rotten Tomatoes Reviews

## Background

The dataset was taken from [Kaggle](https://www.kaggle.com/mrbaloglu/rotten-tomatoes-reviews-dataset) and is comprised of ~10K reviews. Reviews are balanced between two classes, "Rotten" and "Fresh."

## EDA

**Common Words** 
![plot](https://git.generalassemb.ly/tshapiro/project_hackathon/blob/master/plots/top_words.png)

**Common Phrases**
![plot](https://git.generalassemb.ly/tshapiro/project_hackathon/blob/master/plots/top_bis.png)

## Model Results

SVM model yielded the best results, with an accuracy of 78.5%.

| Model                        | Train Accuracy | Accuracy | TP  | FP  | TN  | FN  | Precision | Sensitivity | Specificity | Recall |
|------------------------------|----------------|----------|-----|-----|-----|-----|-----------|-------------|-------------|--------|
| SVM with TFV                 | 93.6%          | 78.5%    | 645 | 189 | 611 | 155 | 79.8%     | 80.6%       | 76.4%       | 76.4%  |
| Logistic Regression with TFV | 94.1%          | 78.2%    | 630 | 179 | 621 | 170 | 78.5%     | 78.8%       | 77.6%       | 77.6%  |
| MultiNomial NB with TFV      | 92.7%          | 77.4%    | 637 | 198 | 602 | 163 | 78.7%     | 79.6%       | 75.3%       | 75.3%  |
| Logistic Regression with CV  | 93.5%          | 77.3%    | 623 | 187 | 613 | 177 | 77.6%     | 77.9%       | 76.6%       | 76.6%  |
| KNN with TFV                 | 82.6%          | 70.8%    | 557 | 224 | 576 | 243 | 70.3%     | 69.6%       | 72.0%       | 72.0%  |
| Random Forest with CV        | 100.0%         | 70.2%    | 574 | 251 | 549 | 226 | 70.8%     | 71.8%       | 68.6%       | 68.6%  |
| Random Forest with TFV       | 98.3%          | 69.6%    | 567 | 253 | 547 | 233 | 70.1%     | 70.9%       | 68.4%       | 68.4%  |

## Conclusions & Recommendations

- **Improving the model** – more hyperparameter tuning with GridSearch to find best model parameters for SVM
- **Testing other models** – would a Neural Network classifier or XGBoost yield higher accuracy scores?
- **Increasing sample size** – collect more reviews to train the model, changing train/test split from 80/20 to 85/15 improved performance slightly.
- **Defining “Rotten”** – model is for binary-classification, but Rotten Tomatoes reviews are typically scaled (1-4 or %). Problem better suited for multi-class?
- **Sarcasm** – text classification analysis doesn’t seem to perform well on sarcasm or text with mixed sentiments (good and bad remarks)

