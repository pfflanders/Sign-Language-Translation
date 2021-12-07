---
layout: post
title: Protocol Droids: Final Reflection
---
{::options parse_block_html="true" /}
<div class="gave-help">
**Group Contributions**

Peter Flanders: <br>

Elliot Shin: <br>

Mansa Krishna: <br>
Worked primarily to deploy our Sign Language Translation model(s) into a web service using Flask. 
</div>
{::options parse_block_html="false" /}

### Did we meet our initial goal? 
To start off with, the goal of our project was to expand the field of sign language translation with a laptop-based tool that provides live-feed translation of basic sign language gestures, and we felt that we accomplished this goal to some extent. We were able to build and deploy a model that was able to (somewhat) successfully translate signed letters of American Sign Language (ASL) in real-time. 

With over two hundred sign languages being used around the world, a further aim of our project was to widen the range of sign language input and attempt to process sign languages other than ASL. However, given the scope of this project and our time constraints, we weren't quite able to achieve this further goal. That being said, given that we have built a model that can parse sign language content, we might be able to re-train it for other sign languages!

### Acquiring the Data
We initially ran into difficulties whilst trying to find a robust and comprehensive data sets to train our models and hence decided to create our own data sets instead. We used the OpenCV library, a library aimed at real-time computer vision, to take snap shots of our own hands making the various signs for various letters. Of course, this in itself had a couple of draw backs since some of the letters for ASL,  such as "Z" and "J" invovled moving gestures instead of fixed signs. Feel free to check out the code for recording the data in the `record_data.py` file in our GitHub repository!

Additionally, none of us were familiar with ASL to begin with, so this was an unexpectedly tedious and challenging part of this project since we had to learn how to sign at least the letters of ASL before recording our data. Furthermore, some of us ran into issues while pushing the data to the GitHub repository since the files were too large (hence, it is possible that you might not see the full data set there). 

### Creating the Models

### Evaluating our Model

### Deploying our Model to a Web App
With regards to deploying our model to a webapp, we decided to attempt to create a live feed translation so that sign language content could be processed in real-time. We did indeed try to write code in JavaScript and import the `.js` file into our `.html` files (stored within our `templates` folder). We experimented with various methods and JavaScript libraries (such as Webcam Easy JS), however even after multiple attempts we were not super successful; perhaps, this is because we were unfamiliar with JavaScript. Given more time, we might have eventually figured out how to accomplish this, but given the time constraints we decided to pivot in another direction. 

Since we were really struggling for time, we decided to take a step back, start small, and try to see if we could upload images to our webapp, display those images, and have our webapp return a prediction. In class we had learned how to render images on a webapp by uploading 8x8 numpy arrays and return a prediction based on a model, however in this case we wanted to see if we could directly upload and process our `.png` files! Indeed, we were able to accomplish this after familiarizing ourselves with the Pillow library, or the Python Imaging Library. 

Since our model was not stored in a `.pkl` file, we couldn't deploy it to the webapp the same way we did in class. We tried importing our model saved in a `.pb` file directly to the webapp using the `tf.saved_model.load` function from the TensorFlow library, however we ran into a couple of issues there as well. Instead, we decided to recompile the model and load in the weights within our Flask `app.py` file. This appeared to work since our webapp successfully rendered both the uploaded `.png` files and the corresponding letter predictions made by our model!

After we managed to deploy our model to our web app, we decided to try again and experiment with various ways to get our live feed translation working. However, this time instead of using JavaScript libraries, we used the OpenCV library (which we were already familiar with) and managed to get a live-feed translation working locally on our computers! Hooray!

In this final part of our project, we ran into several setbacks while trying to deploy our model to the webapp; it often seemed like the minute we fixed one problem, we immediately ran into another problem. It was a very slow process and we really learned that we had to start simple and build our way to the more complex stuff iteratively. After making even a tiny change we would go back and check whether our webapp looked the way we wanted it to. In the end, though this was pretty time consuming and tedious, we thoroughly enjoyed this experience!

### Final Thoughts...
[Discussion of ethics and risks of our project here...]
