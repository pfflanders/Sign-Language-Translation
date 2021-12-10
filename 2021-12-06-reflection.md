---
layout: post
title: Protocol Droids - Final Reflection
---
{::options parse_block_html="true" /}
<div class="gave-help">
**Group Contributions**

Peter Flanders: <br>
Researched previous works' methodologies. Shared utility scripts to aid with collection of data and training of new models. Experimented with collection of diverse image data. Trained dozens of models.<br><br>
Elliot Shin: <br>
Created live feed scripts and implemented them into our Flask app. Trained many models. Experimented with Fine-Tuning existing Image models. <br><br>
Mansa Krishna: <br>
Worked primarily to deploy our Sign Language Translation model(s) into a web service using Flask. 
</div>
{::options parse_block_html="false" /}

## What did we achieve in our project? 
#### Acquiring the Data
We initially planned to use preexisting datasets, but quickly ran into difficulty because we were unable to find diverse, large datasets with consistent signs. We decided to create our own dataset for this project. We used OpenCV, a library aimed at real-time computer vision, to take convert videos of our hands into sequences of images which we sorted into folders with their cooresponding labels. Another issue we had with other data sets were the fact that some of the letters for ASL, such as "Z" and "J", invovled moving gestures instead of stationary signs. We personally chose to remove these signs from our consideration. Feel free to check out the code for recording the data in `record_data.py` in our GitHub repository! You can also view the folder titled reference_data which contains our first collection of data. However, this data ended up not being used in the final training.

Additionally, since none of us were familiar with ASL to begin with, an unexpectedly challenging part of this project was learning to properly sign the ASL alphabet. Furthermore, some of us ran into issues while pushing the data to the GitHub repository since the files were too large. This is why you will not see the full data set on there. We are currently hosting it on a personal Google Drive folder. 

The reason that the data in the folder titled reference data was not used to train the recent model was that after many iterations of underperforming models, we scrapped all of our data and started from scratch with a new RGB dataset. This time we focused more on quality over quantity. In the original dataset the backgrounds of our images were not nearly diverse enough and that did not enable our model to properly learn the gestures present in the images. 

Two key changes in methodology for recording the second dataset vs. the first was (1) to keep the hand at a consistent distance from the camera and (2) to wildly vary the backgrounds of the images. We achieved these new goals by setting a tighter frame (where to keep our hands), and by either setting up our recording process in front of TVs (giving the effect of a green screened background) or by recording data as we walked around (getting real life backgrounds). 

This new dataset proved much harder to learn given the added complexity and so we scaled up the number of parameters in our model from ~2,000,000 parameters(custom CNN and MobileNetV2) to ~20,000,000 parameters for our largest model(ResNet50V2). This obviously increased storage size of the model a lot to 270mb when unzipped. 

#### Creating and Evaluating the Model(s)
Throughout the course of our project, many different variations and permutations of models were used in hopes of identifying which model architecture would prove to be the best. Our initial model was based off of findings online. This model used multiple Conv2D layers mixed with ReLu activation layers accompanied by Dense, Flatten, and Dropout layers. However, it became apparent that while it was decent at classifying our training data, it lacked the performance desired on our validation data. Even worse, performance on a live feed proved to be extremely disappointing and inconsistent. After many different alterations to this initial model, it was deemed that perhaps for the purpose of our project, it would be best to implement transfer learning, leaning on existing models such as MobileNet. 

Thus, we implemented MobileNet as one of our layers in the next iteration of our model. And while the validation accuracy was higher, we still found that performance on a live feed was still too inconsistent to be a viable product. Our team had initially sought out to only use grayscale images with our model in hopes of preventing any learned biases based on our skin tones, but found that the accuracy of the model in a live feed was too low to continue this way. Much to the chagrin of the group, we decided to implement RGB in our next model. 

The final model that the webapp implements uses ResNet and RGB values. We acknowledge the shortcomings and biases of our model, and we hope that we can acquire more data from more diverse sources that our model can be trained on, but for now we had to make do with the appendages the group members had on hand. Further, we collected images using various backgrounds and environments in hopes that our model could learn to only prioritize the hand when classifying letters. Peter actually came up with the ingenious idea of recording data in front of a TV, so that he could maximize the many different backgrounds and other noise that the model would have to filter out. In the end we found that this resnet model had a performance consistently correct enough to demo during our live presentation.  

#### Deploying our Model to a Web App
With regards to deploying our model to a webapp, we decided to attempt to create a live feed translation so that sign language content could be processed in real-time. We did indeed try to write code in JavaScript and import the `.js` file into our `.html` files (stored within our `templates` folder). We experimented with various methods and JavaScript libraries (such as Webcam Easy JS), however even after multiple attempts we were not super successful; perhaps, this is because we were unfamiliar with JavaScript. Given more time, we might have eventually figured out how to accomplish this, but given the time constraints we decided to pivot in another direction. 

Since we were really struggling for time, we decided to take a step back, start small, and try to see if we could upload images to our webapp, display those images, and have our webapp return a prediction. In class we had learned how to render images on a webapp by uploading 8x8 numpy arrays and return a prediction based on a model, however in this case we wanted to see if we could directly upload and process our `.png` files! Indeed, we were able to accomplish this after familiarizing ourselves with the Pillow library, or the Python Imaging Library. 

Since our model was not stored in a `.pkl` file, we couldn't deploy it to the webapp the same way we did in class. We tried importing our model saved in a `.pb` file directly to the webapp using the `tf.saved_model.load` function from the TensorFlow library, however we ran into a couple of issues there as well. Instead, we decided to recompile the model and load in the weights within our Flask `app.py` file. This appeared to work since our webapp successfully rendered both the uploaded `.png` files and the corresponding letter predictions made by our model!

After we managed to deploy our model to our web app, we decided to try again and experiment with various ways to get our live feed translation working. However, this time instead of using JavaScript libraries, we used the OpenCV library (which we were already familiar with) and managed to get a live-feed translation working locally on our computers! Hooray!

In this final part of our project, we ran into several setbacks while trying to deploy our model to the webapp; it often seemed like the minute we fixed one problem, we immediately ran into another problem. It was a very slow process and we really learned that we had to start simple and build our way to the more complex stuff iteratively. After making even a tiny change we would go back and check whether our webapp looked the way we wanted it to. In the end, though this was pretty time consuming and tedious, we thoroughly enjoyed this experience!

## What are we especially proud of? 
~ 2 aspects of our project that we are proud of ~
1. I  believe that all of the data we collected is valuable and can be used in the future for training hand gesture classifiers. At almost a gigabyte of images, managing the data also proved to be a task itself. Since we each recorded data individually, sharing the datasets, merging them together, and hosting them all needed to be addressed. 
2. Obviously, in the end, we are very proud of the final model we trained. While its performance is still inconsistent, we believe that we are on a good track to actually generalize the model's learning to more diverse hands. 


## What would we have done to improve our project? 
Originally, our project's focus was to be able to implement live feed sign language alphabet parsers on the same webapp; however, after realizing how much data was required in order to train our model (over 400,000 images), we were forced to quickly shift away from that goal in order to ensure that we were able to do at least one alphabet. If given more time, we would attempt to train a new model on a new sign language's alphabet. 

Another thing we could have to do improve our project was increase the resolution of our input data. We had originally decided on using 56 x 56 sized images for our neural network in hopes of limiting the amount of training time it would take for our neural networks. While training time was most likely limited, there were many concerns about if the low resolution was enough to discern more finite details. For reference, many other models used input shapes of 64 x 64 and higher. It also felt that our model could vary in success based on the environment the user was in, so in order to create more robust model, perhaps we could train our model on more images at a higher resolution.

Another aspect we would like to improve on is learning the corresponing JavaScript to implement our live feed onto an actual webapp and not our local servers. While we were successful in having our own local machines be able to transmit a live sign language parser, it is entirely dependent on whatever computer is hosting the server. The live feed will always be shown using the camera of the computer hosting the server. 

Finally, the eventual goal was to see if we could teach a neural network to classify gestures in sign language. Due to the complex and confusing nature of data collection, we were turned away from this idea. However, if given more time and perhaps more processing power, we could experiment with using recurrrent Neural Networks with LSTM. 

## How does what we achieved compare to our initial goal? 
To start off with, the goal of our project was to expand the field of sign language translation with a laptop-based tool that provides live-feed translation of basic sign language gestures, and we felt that we accomplished this goal to some extent. We were able to build and deploy a model that was able to (somewhat) successfully translate signed letters of American Sign Language (ASL) in real-time. 

Originally, our project was intended for users who wished to communicate with others via sign language, which was why a further goal of our project was to translate signed phrases and moving gestures as well. However, given that ASL is an incredibly robust language and all three of us had limited knowledge of ASL (plus if you factor in the time constraint), we weren't quite able to achieve this goal. Eventually, the goal of our project evolved - we wanted to see whether webcams could reasonably parse sign language content. 

With over two hundred sign languages being used around the world, another aim of our project was to widen the range of sign language input and attempt to process sign languages other than ASL. However, given the scope of this project and the time constraint, we weren't quite able to achieve this further goal. That being said, given that we have built a model that can parse sign language content, we might be able to re-train it for other sign languages!

## What did we learn from this project experience? 
~ three things we learned ~
1. Better insight into neural networks!! We trained and compiled quite a few models during this entire project and really learned about how those hidden layers worked!
2. Iterative coding is key! We definitely learned to check our work at every stage otherwise we ran the risk of running into bugs and not knowing where to look to fix them (especially because we had really lengthy scripts of code). 
3. Lastly, we learned a little bit of sign language (which all three of us didn't know before).

## How will this project experience help us in our future studies or career?
~ Specific as possible; we can do this by name ~

***Peter***: This project helped me understand a lot more about the surrounding infrastructure required to make a project succeed. Going into the project I was focused on the specificities of the model architecture, but by the end of it I realized how important the data, the deployment, and the language used to communicate about it. Taking the time to create a high quality dataset was vital to the success of the project. Once we had a refined dataset, I spent time learning about the complexities of many existing image classification model architectures and what they do differently. Additionally, another skill I got to practice was using git version control. This is especially important in the production of larger software projects.  <br>

***Elliot***:Personally, this project helped me gain more knowledge about collaborative workflow. I do not think I have worked on an "independent" coding group project like this before. This project also helped me gain better insight into what factors can either make or break a neural network. Things like consistency of data, fine-tuning of transfer learning models, and implementing tools such as google colab really deepened my knowledge of machine learning. I have always been interested in neural networks, and having such a cool group project under my belt gives me the confidence to pursue more projects such as these and hopefully help with gaining some career experience in related fields. Implementing a webapp version of our project was also helpful in helping me with my understanding of what it takes to create an interface potential users can interact with. I am interested in the research aspect of user experience, and feel that this has helped me not only gain experience of implementing such an interface but also gain a sense of what does and does not work when it comes to user-centered design.  <br>

***Mansa***: <br>
Personally for me, I am applying to graduate school (PhD program) in the Atmospheric and Oceanic Sciences/Earth Sciences. I am planning on pursuing research related to predicting climate change using machine learning and modelling our climate system, oceans, and atmosphere using numerical methods. I especially enjoyed the linear algebra and neural networks portion of this class and feel that this course especially helped me learn more about various technologies and algorithms I could implement for the same. 

Additionally, I learned a whole lot about teamwork - this was actually one of the first computing classes I've had where I had to work as a part of a group and honestly I enjoyed the collaborative process a lot (not quite sure how I am going to go back to regular classes from now on). This was an important skill for me to learn since the scientific research process involves a lot of collaboration and peer review (from what I understand). With regards to research itself, I thought our group project was very similar to the scientific research process. A lot of the time we kept running into more problems than successes. I think I cultivated a lot of persistance and tenacity with this project (especially when trying to use Flask to deploy the webapp)! 
