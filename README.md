# Artificial Intelligence in Data Science - Final Project

> Antoine Montier<br>
> NE**FMQN90**<br>
> Final Project

## Introduction

Welcome to the **Final Project** for the *Artificial Intelligence in Data Science* course. This project is unique as it allows students to choose their subject. After a full semester of exploring Artificial Intelligence using Python, with extensive experience in image processing, I ventured through various projects—from **car plate number recognition** to **road sign recognition** and **classification**, including the traditional MNIST dataset classification. For this project, I've chosen to focus on **N**atural **L**anguage **P**rocessing, or **NLP**.

## NLP

**N**atural **L**anguage **P**rocessing involves several steps:

1. Data Collection
2. Text Preprocessing
3. Tokenization
4. Normalization
5. Lemmatization & Stemming
6. Removing Stop Words
7. Handling Special Characters and Punctuation
8. Word Embeddings
9. Model Training
10. Model Evaluation (confusion matrix, `val_loss` value, etc.)

## Dataset Source

I began by exploring available datasets on Kaggle for this classification task, considering several options:

- [BoolQ](https://www.kaggle.com/datasets/thedevastator/boolq-dataset-consistent-data-fields)
- [Stack Overflow Sample](https://www.kaggle.com/datasets/stackoverflow/stacksample)
- [Stack Overflow Python Questions](https://www.kaggle.com/datasets/stackoverflow/pythonquestions/data)
- [Question & Answer Dataset](https://www.kaggle.com/datasets/rtatman/questionanswer-dataset)
- [AI Text vs Student Text](https://www.kaggle.com/datasets/prajwaldongre/llm-detect-ai-generated-vs-student-generated-text)

However, [this dataset](https://www.kaggle.com/datasets/thedevastator/hate-speech-and-offensive-language-detection) particularly caught my attention. It includes a file named [train.csv](./archive/train.csv), containing columns such as:

- `count`: Total number of annotations for each tweet (Integer).
- `hate_speech_count`: Number of annotations classifying a tweet as hate speech (Integer).
- `offensive_language_count`: Number of annotations classifying a tweet as offensive language (Integer).
- `neither_count`: Number of annotations classifying a tweet as neither hate speech nor offensive language (Integer).
- `tweet`: The actual tweet in full text (String).

The goal is to classify tweets as hateful/offensive or not.

## Classification Process

The challenging part was trying various **approaches**:

- Deep Learning
- CNN
- LSTM
- Embedding
- SVM
- Logistic Regression

## From Scratch Notebook

Click [here](./nlp_from_scratch.ipynb) to explore how I achieved high accuracy:

![Confusion Matrix](./output.png)

## Under the Iceberg

Here is the rest, which makes up **90%** of my work:

- [chat.ipynb](./chat.ipynb): This notebook is where I started my experiments, figuring out some traditional TensorFlow & Keras models. I tried using `Embedding` and `LSTM` layers after preprocessing the data. However, I encountered a significant challenge with **data imbalance** (approximately 80% of the tweets were not hateful). In this notebook, I also explored **word tags** (identifying whether a word is a noun, an adjective, etc.). I pondered on what kind of input structure to use for the model, such as:
  - An array like: [$stem_0$, $tag_0$, $stem_1$, $tag_1$, ..., $stem_n$, $tag_n$]
  - Or an array like: [$stem_0$, $stem_1$, ..., $stem_n$, $tag_0$, $tag_1$, ..., $tag_n$]
  - Or two separate arrays: one for stem codes and one for tag codes.
  
  Although [chat.ipynb](./chat.ipynb) didn’t yield the expected results, it laid the foundation for subsequent notebooks.

- [predict.ipynb](./predict.ipynb): Here, I loaded a model to make predictions, but it turned out to be more **random** than accurate.

- [test.ipynb](./test.ipynb): Chat-GPT provided a skeleton architecture for my project in this notebook. Some of its ideas were interesting, but there were many issues (incorrect preprocessing, word padding, and a peculiar model architecture). In this model, I learned about an **effective approach to address data imbalance**: using `compute_class_weight` from `sklearn.utils`. This approach worked better than the one in [chat.ipynb](./chat.ipynb) but was still somewhat random in its predictions.

- [text-CNN.ipynb](./text-CNN.ipynb): Influenced by [this video](https://www.youtube.com/watch?v=MsL79ZIqWpg), I experimented with **NLP using CNN**. I incorporated some functions from previous notebooks and used callbacks during training to save the model's progress. However, the results weren’t as good as I had hoped. The model's accuracy was lacking. I suspected its architecture might have caused it to focus on incorrect data or specific words/word sequences. As I was inexperienced with using CNN for NLP, I decided not to continue modifying this model and shifted my focus to other classification methods.

- [bert.ipynb](./bert.ipynb): In this notebook, I attempted to use BERT (**B**idirectional **E**ncoder **R**epresentations from **T**ransformers), developed by Google. My research indicated that BERT is incredibly powerful, currently employed in search engines. However, it seemed **too powerful for my task**, so I decided not to pursue it further.

- [nlp_grid_search.ipynb](./nlp_grid_search.ipynb): I explored using random forests in this notebook but struggled with model accuracy. I consulted Chat-GPT for advice on improving the model and was introduced to the concepts of **grid search** and **cross-validation**, areas I was not familiar with. Despite implementing these techniques, the results were disappointing. It appeared the model didn’t learn effectively, as evidenced by the following confusion matrix:

  ![Confusion Matrix](./output-2.png)

- In [nlp_from_scratch_2cat.ipynb](./nlp_from_scratch_2cat.ipynb) and [nlp_from_scratch_3cat.ipynb](./nlp_from_scratch_3cat.ipynb), I experimented with **SVM** and **logistic regression**. The SVM model required approximately 2 hours for training and did not yield accurate results. In [nlp_word_influence.ipynb](./nlp_word_influence.ipynb), I explored the influence of specific words in the SVM model and discovered that words like *thewalkingdead* were being misinterpreted, leading to incorrect classifications. Adjusting the model proved time-consuming, so I shifted my focus to logistic regression.

- The logistic regression model, trained in just 8 seconds, showed promise. With some precision adjustments (like setting a threshold of $0.2$), I achieved a test accuracy of 93%, which I considered sufficient. This success demonstrated that sometimes simpler models can be more effective for certain tasks.


## User Script

A user script is available for running and viewing [here](./nlp_from_scratch.py).