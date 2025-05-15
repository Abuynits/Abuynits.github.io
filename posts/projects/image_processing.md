---
title: "Image Proccessing"
summary: "Compilation of random CV + image processing projects"
coverImage: "/assets/projects/processing/processing_overview.png"
order: 6
---


**OCR for Playing Cards**

This is a collection of small CV / Image Processing Projects I've completed


## Pokemón Classifier

<img src="/assets/projects/processing/processing_pkm.png" width="500" height="500">

**Dataset sample highlighting the low number of samples**

ML@Purdue hosted a Pokemón Classfier competition where we were tasked with creating a classifier to predict a Pokemón's type.

I originally used transfer learning from a ResNet-150, but this was deemed illegal by the competition judges... so I turned to a VGG-16 architecture. The provided dataset was very small and severly imabalanced with a large number of classes (i think 18?) and I had to apply data augmentations carefully to prevent loosing too much features.

I ended up winning 1st place!!


## Rock Paper Scissor Game

<img src="/assets/projects/processing/processing_rps.png" width="500" height="500">

**Rock paper scissor detector @ 95% accuracy**

This was a quick weekend project I completed as part of onboarding to the TensorFlow model garden group at Purdue.

This was a standard CNN consisting of three conv -> max pool -> dropout -> max_pool blocks followed by flattening and a few linear layers.

We were challenged to reach >95% accuracy with the smallest parameter count. My model got 3rd place with 25k parameters.

## K-Nearest Neighbor / Image Filters

<img src="/assets/projects/processing/processing_knn.png" width="500" height="500">

**KNN using 7 Clusters**

In APCS, I got a chance to work on an image processing project.

There I implemented KNN in addition to image filters such as image rotation, color masks, and edge detection. 

## OCR for Playing Cards

<img src="/assets/projects/processing/processing_cards.png" width="500" height="500">

**Detecting cards with OpenCV + MNIST. It didnt work well...**

I was just getting started with torch, and instead of making a basic CV project with MNIST, I extended MNIST to detect OCR in cards. 

The base MNIST model worked, but I faced many issues with correctly croping to the top left corner of a playing card and scaling the number, introducing a lot of noise in the model.