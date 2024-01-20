# Artificial Intelligence in Data Science - Final Project

> Antoine Montier<br>
> NE**FMQN90**<br>
> Final Project

## Introduction

Welcome to the **Final Project** of the *Artificial Intelligence in Data Science* course. This is the only project where the student chooses the subject. After a full semester studying Artificial Intelligence using python. I had a lot of experience in image processing. I did many projects: From the digits of a **car plate number** **recognition** to the **road sign** **recognition** and **classification** via the traditionnal mnist dataset classification. I choosed for this project to focus on **N**atural **L**anguage **P**rocessing: **NLP** for short.

## NLP

**N**atural **L**anguage **P**rocessing is a process involving different steps:

1. Data Collection
2. Text Preprocessing
3. Tokenization
4. Normalization
5. Lemmatization & Stemming
6. Removing Stop Words
7. Handling Special Characters and Punctuation.
8. Word Embeddings
9. Model Training
10. Model Evaluation (confusion matrix, `val_loss` value..)

## Dataset source

I first looked at datasets available on Kaggle for this classification task. Here are a few ones:

- [BoolQ](https://www.kaggle.com/datasets/thedevastator/boolq-dataset-consistent-data-fields)
- [Stack Overflow Sample](https://www.kaggle.com/datasets/stackoverflow/stacksample)
- [Stack Overflow Python questions](https://www.kaggle.com/datasets/stackoverflow/pythonquestions/data)
- [Question & Answer](https://www.kaggle.com/datasets/rtatman/questionanswer-dataset)
- [AI text vs student text](https://www.kaggle.com/datasets/prajwaldongre/llm-detect-ai-generated-vs-student-generated-text)

But [this one](https://www.kaggle.com/datasets/thedevastator/hate-speech-and-offensive-language-detection) had my attention.
It contains a file: [train.csv](./archive/train.csv). Not difficult. This csv file has the following columns:

- `count`: The total number of annotations for each tweet. (Integer)
- `hate_speech_count`: The number of annotations classifying a tweet as hate speech. (Integer)
- `offensive_language_count`: The number of annotations classifying a tweet as offensive language. (Integer)
- `neither_count`: The number of annotations classifying a tweet as neither hate speech nor offensive language. (Integer)
- `tweet`: The actual tweet in full text (String)

My goal is to classify tweets as hateful/offensive or not.

## Classification Process

Here is the tricky part. I tried many **different approach**.

- Deep learning
- CNN
- LSTM
- Embedding
- SVM
- Logistic regression

Here's the [approach](./nlp_from_scratch.ipynb) that worked out the best