# Basic Python Image Recognition

## Theory and Logic

The idea behind the small program is to use object recognition to solve for distance to object. 

It has been shown that an object in your vision takes up a certain amount of space in your field of view.
That same object twice as far away from you, would take up half the space in your field of view. 
That same object twice as close to you, would take up double the space in your field of view.

Using data from an image recognition library, and a baseline image taken at 2 feet away, the program will make a guess on how far an object is away from it. For this program, I used a Coke bottle for a test object.

## Implementation

Using Python and the ImageAI Object Recognition Library(https://imageai.readthedocs.io/en/latest/detection/index.html)
I choose to use the ImageAI library because it already had a model for Coke bottles

1. First, I took a picture of a Coke bottle standing up from about 2 feet away. I ran that image through a modified version of the imageTest.py program to get information on the bounding boxes. 

2. The information of the bounding boxes is the upper left (x1,y1) and lower right (x2, y2) coordinates for the bounding box. Using those coordinates the length (x2 - x1) and width (y2 - y1) of the object can be found. These are the dimensions of the baseline 2 foot away Coke bottle.

3. When a new image is ran through the program, the proportion of that objects length an width to the baseline objects length and width need to be found to calculate the distance compared to the baseline object. 
...For length the proportion is lengthofObject / lengthofBaseline.    
...For width the proportion is widthofObject / widthofBaseline.

4. Take the average of the width and length proportion.
...( width proportion + length proportion ) / 2

5. To find total distance 
... distance of baseline / average proportion

## Bugs

1. The ImageAI result was rotating the image 90 degrees counterclockwise. This swaps the length and width dimensions for the bounding boxes. It had no impact on my experiment because it rotated the baseline and test images the same. However, in a scenario when the baseline image had not been rotated, and the test images were being rotated then the results would be off because the test images would have swapped length and width.

## Future Ideas 

1. Right now this only works looking directly at objects standing in the same orientation as the baseline object. A future work could be finding out how to get this idea to work on objects at different angles and orientations.

2. This test only accounted for one type of object as a baseline, and only used images that only had that one specific item in them. Another improvement would be to get baselines for multiple objects, and then do the math based on what object is found. For example right now the program would be comparing all objects found in an image to the Coke bottle baseline that was hard-coded in. Instead there would be a data structure that would have baselines for many objects at a certain distance that would be used when that specific object is found. 

