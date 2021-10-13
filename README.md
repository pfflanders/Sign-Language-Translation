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
All projects we undertake involve decisions about whose interests matter; which problems are important; and which tradeoffs are considered acceptable. Take some time to reflect on the potential impacts of your product on its users and the broader world. If you can see potential biases or harms from your work, describe some of the ways in which you will work to mitigate them. Remember that even relatively simple ideas can have unexpected and impactful biases. Here's a nice introductory video for thinking about these questions, and here's one that goes into somewhat more detail. Here are some relevant examples: - A recipe recommendation app can privilege the cuisines of some locales over others. Will your user search recipes by ingredients? Peanut butter and tomato might seem an odd combination in the context of European cuisine, but is common in many traditional dishes of the African diaspora. A similar set of questions applies to recommendation systems related to style or beauty. - A sentiment analyzer must be trained on specific languages. What languages will be included? Will diverse dialects be included, or only the "standard" version of the target language? Who would be excluded by such a choice, and how will you communicate about your limitations?

A related question is: should this app exist? In a few sentences, discuss the following questions:

What groups of people have the potential to benefit from the existence of our product?
What groups of people have the potential to be harmed from the existence of our product?
Will the world become an overall better place because of the existence of our product? Describe at least 2 assumptions behind your answer. For example, if your project aims to make it easier to predict crime, your assumptions might include:
Criminal activity is predictable based on other features of a person or location.
The world is a better place when police are able to perform their roles more efficiently.

### **Tentative Timeline**
Week 3 is now, so our 2 week checkpoints are
- Week 5: 
- Week 7: 
- Week 9: 
There will be checkpoints for the project at approximately two-week intervals. With this in mind, please describe what you expect to achieve after two, four, and six weeks. At each stage, you should have "something that works." For example, maybe in two weeks you'll ready to demonstrate the data acquisition pipeline, in four weeks you'll be able to demonstrate some data analysis, and in six weeks you'll have your full machine learning pipeline set up. Please keep in mind that you'll be asked to present at each of these checkpoints. Showing "something that works" will usually be necessary for full credit. The "something that works" idea is related to the common concept of "minimum viable products" in software development, and is visually illustrated here:
