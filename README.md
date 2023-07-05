# Pinocchio_examples
Some python examples using robot manipulators, particuarly the Jaco Gen2 of kinova.

## For getting more information about Pinocchio
https://github.com/stack-of-tasks/pinocchio

## For using Pinocchio on the Real manipulator (C++ and skillset architecture) 
https://gitlab.com/J.Betancourt20/jaco_skills/-/tree/Pinocchio

## Easy Installation to start runing the programs

### Pinnochio 
```
$ conda install pinocchio -c conda-forge
```
###  meshcat
```
$ conda install -c conda-forge meshcat-python 
```
### gepetto-viewer
```
$ conda install gepetto-viewer gepetto-viewer-corba -c conda-forge
```
### Plotly
```
$conda install -c plotly plotly=5.13.1 
```
### Troubleshooting
When runing the files you'll have an error when lunching meshcat. It seems that the package typing has some issues. In order to run the files
```
$ pip uninstall typing
```
If you want to use the interactive ``%matplotlib widget`` probably you will get the following error ``Uncaught exception in ZMQStream callback``. I solved it with
```
$ pip install --upgrade ipyflow jupyter_client jupyter_server jupyter_core tornado
```
