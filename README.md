## Robust Quadrupedal Locomotion on Sloped Terrains:A Linear Policy Approach

### Introduction:
This is the main code base accompanying the paper with the above title, under review in CoRL 2020.


### To make an initial policy:
As explained in the paper, we take a guided learning approach wherein the role of a initial policy is quite crucial.To train your own initial policy,run the following command
        
        python create_initial_policy.py --policyName filename

This save the initial policy as *filename.npy* in the initial_policies folder.This is to be loaded later as the initial polcy when you want train your own polciy.However there are a few initial policies present in the same folder which could be directly used to start the ARS training.

**Note:** The initial policies are by default saved in the *initial_policies* folder.

### To train the linear policy with ARS
This is where the ARS trainining starts, with the initial polciy trainied in the previous step.
        
        python ars_multi.py 

The above command starts the training in the default and the best by far hyperparameter and experiment settings.However, the following parameters can be customized in the training as desired b the user.

| Parameter     |About        |  type |
|:-------------:|:-------------:| -----:|
|--render      | flag for rendering | bool |
|--policy      | initial polciy to start the training with|str|
| --logdir | Directory root to log policy files (npy)     |str |
| --lr | learning rate     |float |
| --noise | amount of random noise to be added to the weights|float |
| --msg |any message acompanying the training|str |
| --curi_learn |Number of learning iteration before changing the curriculum      |int |
| --eval_step |Number of policy iterations before a policy update     |int |
| --episode_length|Horizon of a episode|int |

For example,

      python ars_multi.py --lr 0.05 --noise 0.04 --logdir testDir --policy init_policy_TS.npy --msg "Training with some paramters" --episode_length 400

**Note:** 

1. The initial policies are by default loaded from the *initial_policies* folder and the log directory is saved inside the *experiments* folder.
2. The are a few other insignificant parameters which need not be changed for the training, for more info about the parameters run

        python ars_multi.py --help

## To conduct tests on a policy
To run a policy in default conditions, the following command is to be used.

        python test_policy.py

the following test parameters can be changed while testing the policy,

| Parameter     |About        |  type | Allowed values|unit|
|:-------------:|:-------------:|:-----:|:---------:|:-----:|
|--WedgeIncline | the elevation angle of wedge | int |0,5,7,9,11,13|Degrees(°)|
|--WedgeOrientation| the yaw angle of wedge about world z axis | float | -90.0 to 90.0 |Degrees(°)|
|--EpisodeLength |number of gait steps of a episode| int |0 to inf|number of steps|
|--MotorStrength|maximum motor strength that could be applied| float |5.0 to 8.0|NewtonMetre(Nm)|
|--FrictionCoeff|coefficient of friction to be set| float |0.55 to 0.80|unitless|
|--FrontMass|mass to be loaded to the front half of the body| float |0.0 to 0.15|Kilograms(Kg)|
|--BackMass|mass to be loaded to the  rear half of the body| float |0.0 to 0.15|Kilograms(Kg)|
|--RandomTest|flag to activate random sampling| bool |True or False|unitless|

Thus, for a 

1. custom test

        python test_policy.py --WedgeIncline 11 --WedgeOrientation 15 --FrontMass 0.1 --FrictionCoeff 0.6

2. random test

        python test_policy.py --RandomTest True

## To do:

* User choice to give perturbation (may b a parameter in prev point itself)

