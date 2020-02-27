# Determining Legal Advice Posts' Britishness
by Ethan Henley\
This project was completed as a part of General Assembly's Data Science Intensive.

## Contents

- [Problem Statement](#Problem-Statement)
- [Executive Summary](#Executive-Summary)
- [Model Selection](#Model-Selection)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)
- [Materials Used](#Materials-Used)

## Problem Statement

To establish potential stakeholders, this model was designed for an **imaginary** client startup: LawChat, an app that intends to connect clients with legal experts on retainer to answer small-potatoes legal questions, preparing for a simultaneous soft launch in both the United States and the United Kingdom. 

LawChat cannot collect user location data. However, they wish to connect users to legal experts in the correct country. To facilitate this, we have decided to __generate a model to predict whether a legal advice request is coming from America or the United Kingdom based on the title and text of the message.__ 

We use posts from the subreddits r/legaladvice as a proxy for LawChat advice requests from the United States (though it allows posts from non-Americans) and r/LegalAdviceUK for the United Kingdom.

## Executive Summary

We used a Python script to access the PushShift API and gather data from the subreddits r/legaladvice and r/LegalAdviceUK, and saved that data to a .csv. This data includes post titles and bodies, which we used in our model. We gathered 3000 posts from each Subreddit.

We inspected and cleaned this data; accounting for deleted, removed, or otherwise blank posts; processed the text with stemming and word vectorization; and then ran multiple models.

Ultimately, we decided that, based on models' accuracy with testing data, our best model was a Multinomial Naive Bayes model. We were also interested in the concept of the Support Vector Machine model, though it was outperformed by the Multinomial Naive Bayes.

## Model Selection

|Model|Vectorizer|Train Accuracy|Test Accuracy|
|-|-|-|-|
|Baseline|n/a|.5|.5|
|Logistic Regression|TFIDF|.802|.767|
|Multinomial Naive Bayes|Count|.907|.853|
|Gaussian Naive Bayes|TFIDF|.919|.809|
|Support Vector Machine|TFIDF|.992|.827|
|AdaBoost|Count|.932|.801|
|kNN|TFIDF|.766|.706|
|Bagged Decision Trees|Count|.984|.757|

Based on test accuracy scores alone, it is easy to pick our best model: the Multinomial Naive Bayes. Knowledge that Naive Bayes models are generally suited well for natural language processing also influences this decision, even though we know that the naive assumption of variable independence absolutely does not hold for word counts.

The Support Vector Machine is interesting, and takes second place in test accuracy even as it is substantially overfit. Its usefulness on natural language data is worth remembering.

## Conclusions and Recommendations

The best of the models we tested is the Multinomial Naive Bayes model, with 85% accuracy on non-training data. We expect this will extend to similar, non-Reddit data collected by LawChat, allowing the service to distinguish between UK and US users. 

This model could be upgraded after the hypothetical app's launch by retraining it on legitimate app data, which will hopefully remove some of the weaknesses that come from relying on Reddit data. 

However, 85% accuracy is far from perfect, so we would recommend that each legal expert respondent confirm that the messages forwarded to them appear to be from the correct country and be given an easy method to mark a message as for another country based on their judgement, which we expect they will need to do 15% of the time. Still, this is cheaper and preferable to having humans manually sort through every message.

Additionally, we would recommend that once location data can be easily and legally collected, which is much simpler and more accurate. Text-analysis-predicted locations could be used for the few cases where that is not feasible.

## Materials Used

- [Pushshift API](https://pushshift.io/)
- [r/legaladvice](https://reddit.com/r/legaladvice)
- [r/LegalAdviceUK](https://reddit.com/r/LegalAdviceUK)
