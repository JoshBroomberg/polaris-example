# Polaris Demo Repo

## Intro

This repo trains two models to predict the price of a wine bottle based on its age and region.
The first model is a basic scikit regression. The second is a neural network optimized through
sagemaker hyperparameter optimization.

The models are trained, tested, and deployed using Polaris based on the `.polaris/workflow.yaml` file.
This file specifies each step - train, test, deploy - as a declarative stage. Workflows run the stages based
on a trigger like a commit to a branch.

## Tasks

1. Explore the code in the repo
2. Add a new 'grape' feature to the models
3. Adjust the search space for the neural network HPO
4. Change the deployment settings so that batch infernece runs when new data arrives.