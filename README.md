# deep classifier project

------------
# Worklow
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipelines
8. Test run pipeline stage
9. run tox for testing your package
10. update the dvc.yaml
11. run "dvc repro" or running all the stages in pipeline

![img](https://github.com/ywaquar/DeepCNNClassifier/blob/main/docs/images/Data%20Ingestion@2x%20(1).png?raw=true)

# dvc.yaml. paramas.yaml, and config/conig.yaml :

In the root of the project you will ind certain file which is used for the orcrastation that means to connect several pipeline. In the prvious batch you may have seen main.py . Here instead of using main.py we are using dvc.yaml, which will do same kind of things i.e. orcrastation. Its a very interesnting tool. You can use it in various project and its a very lightweight tool, now adays it is very popular, you can put it into your skills. and this will be very unique.

In params.yaml , we will put all the parameters, parameters related to the project, like what is batch size, how many epoches we have to run.

In Config.yaml, where i will keep all the configuration of file. i.e. project struction that means where the artifacts is going to be stiore. for every stage there will be output so all of the file related to artifacts and coniguration will be present inside the config.yaml.

These three iles are root of the project. i.e. outer struction.


there is a package which is inside the src folder. you will find deeClassifier named pacakge.
# Config: 
This will maintain all of our congiration of the project, including parameters also that will be passed some module as well.

# Entity: 
Wehere we will be defining what is the parameters should be passed. 

# Constants: 
We will see what are costants of the prjects. In config.yaml, almost all the parametrs are constant so we will ass only those parameters which remains constant in the rojects.

# Utils: 
Reading and writing certains files. saving binary objects, reading binary object, saving reports ito json file all those will be prsent in the Utils.

# Components + Pipeline :
These components will be passed in this fashion, There will be Data Ingestion, It will get the data somewhere and sored in the artifacts, then this will be used for the training of the data.

# Prepare Base Model: 
It will help us to prepare base model where we will be defind how many layers we will be having.

# Prepare Callbacks: 
We have learnt tensorboards, early stopping, several other callbacks i.e. upto you. So in the training you will be calling all these data.

# Best Model Selector: 
We will use ML flow it allows you to it tracks everythng it will help to shortlist them, it will past run, it will check accuracy . It wil just pick from that model in the past. It will pick that model and put in thhat folder then we can dockerize that model so end users can use it.

