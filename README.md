# Sign-Language-Translation
Machine Learning Project with an interface providing the live translation of (hopefully multiple) sign languages.

### **Abstract**
Sign languages (or signed languages) are languages that utilize visual and manual modality (i.e., gestures) to convey meaning. Rather like other spoken languages of the world, sign languages are not universal or mutually comprehensible despite the various similarities among them. It is important to note that sign languages are not merely visual manifestations of other spoken languages like English, rather they are unique languages with their own set of linguistic rules.

Sign language processing is an emerging field of machine learning that falls within the intersection of natural language processing (NLP) and computer vision. As the name suggests, it involves both the analysis and automatic processing of sign language content. The goal of this project is to expand the field of sign language translation with a laptop-based tool which provides live-feed translation of basic sign language gestures. The overarching methodology involves creating a Computational Neural Network (CNN) that is not only small and fast enough to be run on standard laptops, but also robust enough to accurately translate words and symbols when they are present and not return too many false classifications. Additionally, with over two hundred sign languages being used around the world, a further aim of this project will be to widen the range of sign language input and attempt to process and analyze a significant portion of these languages.

### **Planned Deliverables**
- Partial Success: **a locally run program** would more focused the machine learning aspect of this project and would prioritize the accurate, timely, and possible generalization of translating. We will look into using Transfer Learning to try and capitalize on existing image classification models to create models specific for languages other than ASL.
- More Success: **a webapp** would focus on deploying a trained model in a website environment likely using the TensorflowJS package and others available. If we wanted to focus less on machine learning / are struggling to expand our model beyond ASL, we will focus on enhancing the interface.
- Full Success: **A webbapp which incorporates multiple translation languages** would combine both of the above tasks and flesh them out, making a more complete experience.
- Obviously, if we are finding lots of success along the way and have extra time we can aim to improve accuracies. Additionally one thing that we could explore if we are finding success is the implementation of a set of prior frames to our model to explore the possiblility of recognizing gestures which include motion.  

### **Resources Required**
Obviously to train any classification models, we require datasets to train on. There exist many labeled ASL alphabet datasets. There are other languages which are similar to ASL and which our models would be able to learn. There is a large field focus on data generation which could be explored if we were lacking data and wanted to explore this.

https://www.kaggle.com/datamunge/sign-language-mnist

https://www.kaggle.com/grassknoted/asl-alphabet

https://www.kaggle.com/prathumarikeri/american-sign-language-09az

https://www.kaggle.com/prathumarikeri/indian-sign-language-isl

http://home.ustc.edu.cn/~pjh/openresources/cslr-dataset-2015/index.html

I believe our laptops will be sufficient to train the classifiers necessary for this project since we are focusing on making this model portable.


### **Tools and Skills Required**
Our project focuses on the training and implmentation of a CNN, so we will refine our Tensorflow skills, data manipulation abilities, and will need to learn about deploying models for web use.

### **What You Will Learn**
Our team does not have much experience making our own machine learning models so we'll need to learn the Tensorflow API. The other large challenge will be the development of the interface and making sure we can deploy our model.

### **Risks**
Risks associated with achieving the full deliverable include time, dataset limitations/availability, and adaptation of our model.
- Time: While we are quite confident in building a locally run program to translate sign language with high accuracy, we are unsure if the time permits to be able to do so in a website environment with multiple sign languages. Considering the goal to translate signs and gestures from a live video feed, the time limitation may prevent our team from being able to do so for multiple sign languages.
- Dataset Limitations/Availability: In order to pursue models that can translate multiple sign languages, data pertaining to additional sign languages must exist. While there is a plethora of datasets for ASL, it is more difficult to find datasets for other languages of interest. If there is a language of interest without a dataset, would we have to create our own dataset large enough to train and test a model on? An interesting thing to consider are sign language alphabets that require two hands, and if/how this will affect implementation of our model.
- Adaptation of our Model: Another consideration would be the transfer of a model taught on single images to a model trained on a video feed. If accuracy does drop off when the model is applied to a video feed, how would we adjust/adapt our model to the new environment while maintaining a high accuracy? We are progressing in our project operating under the assumption that we are able to in fact create a model that can operate with a live video feed.  

### **Ethics**
A sign language parser tool aims to help those with impaired hearing or speech, enabling greater ease of communication between groups of people – including not only those who suffer from impaired hearing and speech, but also those who do not know sign language. However, a universal sign language does not exist, instead there are many different dialects of sign language (e.g., American Sign Language (ASL), British Sign Language, Indian Sign Language, etc.), each with their own distinct gestures and signs. This increases the potential for bias as there is a chance we might focus on only the most popular sign languages with readily available data. In an ideal scenario, to mitigate this bias we might need to take into account every single type of sign language. And yet, since there are too many different types of sign languages, we might need to limit our project to only the most popular dialects of sign language. While making this trade-off would still benefit a good number of people, it could indirectly harm those individuals who do not communicate using the most common dialects of sign language.

Though this project has the potential for bias and could inadvertently harm a small minority of individuals, we do think that this project is a good stepping stone in the right direction as it would enable faster and better communication between native sign-language users and non-sign-language users. This will improve communication between diverse groups of people and ultimately lead to innovation, growth, and the spread of new ideas.

### **Tentative Timeline**
Week 3 is now, so our 2 week checkpoints are
- Week 5: Working Model which successfully characterizes single images
- Week 7: Implementation of the model into a live feed. Explore training additional models
- Week 9: Deployment of model(s) into web service.
