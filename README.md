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

## From scratch notebook

Click [here](./nlp_from_scratch.ipynb) to explore and figure out how I solved it with a high accuracy:

![confusion matrix](./output.png)

## Under the Iceberg

Right above you will find **10%** of my total work. Here are the **90%**:

- [chat.ipynb](./chat.ipynb) is the first notebook where I made my experiments ad figured out some tensorflow & keras traditionnal model aren't as always the best solution. You'll find that I tried to use `Embedding` (zoom on the [Embedding layer](./emb.md)) & `LSTM` layers after pre-processing data. It ended up being too complicated. After facing a big problem which is **data imbamance** (about 80% of the tweets are peaceful). To face this problem I tried to make a **custom loss function** that penalize false-hate but I didn't worked. In this notebook, I also explored here the **word tags** (if a word is a noun, an adjective..). I faced some issue when training my data: here are the ideas I got when asking myself what input should I put in the model
  - An array of this type:
    - [$stem_0$, $tag_0$, $stem_1$, $tag_1$, $stem_2$, $tag_2$ ... $stem_n$, $tag_n$]
  - Or an array of this type: 
    - [$stem_0$, $stem_1$, $stem_2$ ... $stem_n$, $tag_0$, $tag_1$, $tag_2$ ... $tag_n$]
  - Or two input arrays:
    - stem code
    - tag code

> The [chat.ipŷnb](./chat.ipynb) notebook didn't worked but is the **basement for the next notebooks**.

- In [predict.ipynb](./predict.ipynb), I loaded a model to make predictions but it wasn't accurate, It was more **random** than everything

- Chat-GPT made me a skeleton architecture for my project [here](./test.ipynb). I found some of his ideas interesting but there were a lot of problems (incorect pre-processing, word padding, weird model architecture..). In this model I learned about an **effective way to bypass data imbalance**: using the `compute_class_weight` from `sklearn.utils`. It worked better than [chat.ipŷnb](./chat.ipynb) notebook but still kind of random

- After viewing [this](https://www.youtube.com/watch?v=MsL79ZIqWpg) video, I tried to implement some **NLP using CNN** [here](./text-CNN.ipynb). I copied some functions of the previous notebooks. During the training I used two callbacks to save the model trained so far. The outcome wasn't as good as I predicted, the model wasn't accurate. I think its wrong architecture made him classify data focusing on wrong data or maybe only on some words / word sequences. As I never used CNN for NLP I gave up model modifications and focused on other classifications methods.

- In [this notebook](./bert.ipynb) I tried to use BERT (**B**idirectional **E**ncoder **R**epresentations from **T**ransformers) developped by *Google*. When doing researches about NLP I founded that BERT is very powerful. Today BERT is used in **search engines**. I tested it and then I though it may be **too powerful for my task**.

- [Here](./nlp_grid_search.ipynb) I explored random forests. The model wasn't accurate, I asked *Chat-GPT* how to make it accurate and it gave me some code and explanaitions about **grid search** and **cross validation** which are two subjects I don't know at all. The result was very bad. I think the model didn't learned at all:

![confusion matrix](./output-2.png)

- In those notebooks: [here](./nlp_from_scratch_2cat.ipynb) and [here](./nlp_from_scratch_3cat.ipynb), I tried to use **SVM** and **logistic regression** to solve my task. SVM took about 2 hours to train and wasn't accurate at all. In [this notebook](./nlp_word_influence.ipynb): example of SVM use plus at the end there's a picture that shows the important words. Here I saw that *thewalkingdead* was the 3rd most positive word... I tried to adjust but 2 hours of computing between each try made me give up and focus on logistic regression. <br> Logistic regression trained during 8 seconds and with some optimisations on the precisions (eg: I made a threshold = $0.2$), I reached with this model a test accuracy of $93 %$ which is enough in my opinion.

## User script

I made a user script that you can run and view [here](./nlp_from_scratch.py).