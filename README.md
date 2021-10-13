# Sign-Language-Translation
Github Repo focused on the translation of sign language using machine learning

### **Abstract**
The goal of our project is to expand the field of sign language translation with a laptop based tool which provides live-feed translation of basic sign language gestures. We wish to accomplish this by creating a CNN small & fast enough to be run on \*standard laptops, but robust enough to accurately translate words and symbols when they are present and not return too many false classifications.

### **Planned Deliverables**
- Partial Success: **a locally run program** would more focused the machine learning aspect of this project and would prioritize the accurate, timely, and possible generalization of translating. If we wanted to explore Transfer-Learning to try and capitalize on existing models to include more than just ASL, we would need time to focus on this.
- More Success: **a webapp** would focus on deploying a trained model in a website environment likely using the TensorflowJS packages available. If we wanted to focus less on machine learning / are struggling to expand our model beyond ASL, this could be a good path to take.
- Full Success: **A webbapp which incorporates multiple translation models** would combine both of the above tasks and flesh them out, making a more complete experience.
- Obviously, if we are finding lots of success along the way and have extra time we can aim to improve accuracies to make an even more impressive project!

### **Resources Required**
Obviously to train any classification models, we require datasets to train on. There exist many labeled alphanumeric ASL datasets. I do not know yet about other languages. There is a large field focus on data generation which could be explored if we were lacking data for a specific language. *This is not going in the actual proposal this will be deleted after we speak*.

https://www.kaggle.com/datamunge/sign-language-mnist

https://www.kaggle.com/grassknoted/asl-alphabet

https://www.kaggle.com/prathumarikeri/american-sign-language-09az

https://www.kaggle.com/prathumarikeri/indian-sign-language-isl

http://home.ustc.edu.cn/~pjh/openresources/cslr-dataset-2015/index.html

I believe our laptops will be sufficient to train the classifiers necessary for this project since we are focusing on making this model portable. 


What resources do you need in order to complete your project? Data? Computing power? An account with a specific service?

Please pay special attention to the question of data. If your project idea involves data, include at least one link to a data set you can use. It's also acceptable to link to a website from which you intend to scrape the data you will use (although note that high-quality scraping is a lot of work).

If you can't find data for your original idea, that's ok! Think of something related to your group's interests for which you can find data.

Most projects should involve data in some way, but certain projects may not require data. Ask me if you're not sure.

### **Tools and Skills Required**

What skills will you need? Machine learning, database management, complex visualization, something else? Do a bit of research into which Python packages accomplish the tasks you are going to need. Feel free to look ahead at what we're going to do in the remainder of the course -- you're likely to find some of the packages you'll need there!

### **What You Will Learn**
What will you learn by completing this project? Feel free to mention particular techniques, software packages, version control, project management principles, any other learning goals you might have.

### **Risks**
What are two things that could potentially stop you from achieving the full deliverable above? Maybe it turns out that the signal you thought would be present in the data just doesn't exist? Or maybe your idea requires more computational power than is available to you? What particular risks might be applicable for your project?

### **Ethics**
A sign language parser tool aims to help those with impaired hearing or speech, enabling greater ease of communication between groups of people – including not only those who suffer from impaired hearing and speech, but also those who do not know sign language. However, a universal sign language does not exist, instead there are many different dialects of sign language (e.g., American Sign Language (ASL), British Sign Language, Indian Sign Language, etc.), each with their own distinct gestures and signs. This increases the potential for bias as there is a chance we might focus on only the most popular sign languages with readily available data. In an ideal scenario, to mitigate this bias we might need to take into account every single type of sign language. And yet, since there are too many different types of sign languages, we might need to limit our project to only the most popular dialects of sign language. While making this trade-off would still benefit a good number of people, it could indirectly harm those individuals who do not communicate using the most common dialects of sign language. 

Though this project has the potential for bias and could inadvertently harm a small minority of individuals, we do think that this project is a good stepping stone in the right direction as it would enable faster and better communication between native sign-language users and non-sign-language users. This will improve communication between diverse groups of people and ultimately lead to innovation, growth, and the spread of new ideas. 

### **Tentative Timeline**
Week 3 is now, so our 2 week checkpoints are
- Week 5: 
- Week 7: 
- Week 9: 
There will be checkpoints for the project at approximately two-week intervals. With this in mind, please describe what you expect to achieve after two, four, and six weeks. At each stage, you should have "something that works." For example, maybe in two weeks you'll ready to demonstrate the data acquisition pipeline, in four weeks you'll be able to demonstrate some data analysis, and in six weeks you'll have your full machine learning pipeline set up. Please keep in mind that you'll be asked to present at each of these checkpoints. Showing "something that works" will usually be necessary for full credit. The "something that works" idea is related to the common concept of "minimum viable products" in software development, and is visually illustrated here:
