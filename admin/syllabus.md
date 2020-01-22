# CSCI 378: Deep Learning
## Spring 2020 Syllabus

### Basic Information

**Professor:** Mark Hopkins, hopkinsm@reed.edu

**Class Schedule:** MWF 9-950am in Eliot 207

**Office Hours:** W 4-6pm, Th 1030-1130 (first come, first served), as well as
MF 4-5pm (by appointment - sign up using [this link](https://calendar.google.com/calendar/selfsched?sstoken=UU5mSjE1SFNSUk5xfGRlZmF1bHR8NzQ2MDU3MzJkYjQyOTkxOGE3OWViMzU0MDYxMTQxOWM)).

**Website:** http://markandrewhopkins.com/csci-378-deep-learning


### Overview

This course teaches you the fundamentals you need, in order to be an informed,
well-rounded practitioner of deep learning.  It will proceed through three
phases:

1. **The Pool:** In which we learn/review the fundamental background for deep learning, including gradient descent, simple regression models, important probability distributions, regularization, and matrix manipulation (with the Python torch package).
2. **The Shallows:** In which we learn about the most mainstream concepts in deep learning, including multilayer feedforward networks, convolutional neural networks, and recurrent neural networks.
3. **The Abyss:** In which we go into the cutting edge, including advanced neural architectures, open research questions, and important NLP and computer vision applications.


### Coursework

**Homework:** There will be short but very regular (i.e. most class sessions)
homework assignments. They are important to do, so that you can learn the
material well. Even if you can't get to the solution, please try to hand in
a good faith effort. We will spend the first section of each class tackling
the homework assignment from the last class. You will be required to hand in
homework solutions, with the freedom to skip four homeworks over the course
of the semester without penalty. I would, however, encourage you not to
exercise this freedom unless necessary.

**Projects:** There will be an ongoing sequence of projects during the course,
curated specifically for this course offering.

**Exams:** There will be three exams during the course: two midterms and a
final. Each exam is weighted equally and covers one phase of the course.
However, the material in the course builds on the previous material, so while
the final will be focused on the final third of the course, you will probably
need a solid understanding of the first two thirds in order to do well.


### Learning Objectives

Learning objectives for this course include (but are not limited to) the 
following:

1. Given access to reference documentation for PyTorch, a student will be
able to transform an input tensor into a specified goal tensor, while
preserving automatic differentiation.
2. Given a Bayesian network diagram, a student will be able to determine whether
given variables X and Y are d-separated by a particular set Z of variables.
3. Given a functional causal model, a student will be able to compute an
arbitrary partial derivative using repeated applications of the Chain Rule
of Partial Derivatives.
4. A student should be able to derive maximum likelihood estimates for
ordinary linear regression and robust linear regression.
5. A student should be able to derive MAP estimates for ridge regression
and lasso regresssion.
6. A student should be able to derive the gradient of the MLE loss function
for logistic regression.
7. A student should be able to devise a dataset that cannot be modeled using
logistic regression, and prove that it cannot be modeled. The student should
be able to show that the dataset can be modeled using a two-layer feedforward
neural network.
8. A student should be able to use backpropagation to compute the gradient
of a loss function with respect to a particular parameter in a simple
multilayer feedforward neural network.
9. Given an example classification/regression problem, a student should be
able to design a sensible output layer for a neural network classifier.
10. A student should be able to define (from memory) the ReLU and softmax
functions.
11. Given the kernel size, number of kernels, and stride, a student should
be able to give the dimensions of the parameter tensors of a convolutional
neural network.
12. A student should be able to apply a maxpool operation on an example tensor.
13. A student should be able to complete a partially drawn causal diagram
for a convolutional neural network.
14. A student should be able to draw a logistic sigmoid function.
15. Given a particular padding and stride, a student should be able to
manually convolve a (small) image with a kernel.
16. A student should be able to draw a causal model diagram for an unraveled
recurrent neural network, including giving the dimensions of the parameter
tensors. The student should be able to compute partial derivatives using
this diagram and backpropagation.




### Collaboration

Collaborating on homework and projects is permitted, but each student must
write up homework independently, and must do the actual programming on the
projects independently (no cutting and pasting somebody else’s code!) Also,
you should acknowledge the names of anyone who you collaborated with.


### Reading Assignments

Reading assignments will be posted on the website a minimum of two days in
advance of each lecture. I will assume that the reading is done prior to
lecture. 


### Disability Accommodation

If you have a disability for which you are or may be requesting an accommodation, you
are encouraged to contact both your professor and the Office of Disability Support
Services, disability-services@reed.edu or 503-517-7921 as early as possible in the
semester. Please be aware that requests may take several weeks to implement once
approved, and that accommodations are not retroactive.
