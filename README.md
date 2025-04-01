# POSE 2025 Workshop!
*April 14-15, 2025 @ The University of Washington*


This repository contains code for the 2025 Pathways to Open-Source Hardware for Laboratory Automation Workshop at the University of Washington! Read on to learn about the workshop and the contents of this repository.

## About the Workshop
On April 14-15 2025, we are gathering a group of scientists and engineers interested in using open-source technologies for automating scientific experiments at the University of Washington. You can find more information about the workshop and participants [here](https://depts.washington.edu/machines/scienceautomation/).

## Workshop Hackathon
During the workshop, we will break into teams and have 4 open-ended work sessions to set up automation workflows using [Science Jubilee](https://science-jubilee.readthedocs.io/en/latest/), a custom toolchanging machine. 

### Materials
We'll have 6 machines equipped with the following tools:

- a camera, for imaging the bed plate
- a 10cc syringe, for liquid handling or gel extrusion 3D printing
- a spectral sensor, for data collection
- an OT-2 pipette, for precision liquid handling
- additionally, 1 machine has 2 FFF 3D printing heads equipped

We'll provide laptops with all relevant software already installed. If you'd prefer to try to install on your own laptop, see the [installation instructions](#installation) below.

### What Should I Make?
Whatever you want! You don't necessarily have to use Jubilee, if you and your team have other interests. Here are some ideas:

- Implementing a color matching algorithm
- Tuning (plastic or gel) 3D printing parameters using a video feed
- Integrating a new tool for Jubilee, if you're CAD-inclined
- Working on optimization algorithms that might be suited to Jubilee, if you're software-inclined

Whatever you work on, be sure to take some notes along the way so you can share with others what you've worked on! 

### Schedule
The full workshop schedule (including discussion topics, lunch breaks, etc) can be found [here](https://depts.washington.edu/machines/scienceautomation/). The following times are when we'll have open-ended work sessions:

#### Monday, April 14
##### 10:30a-12p: Notebook Intro
- Form teams
- Get familiar with Jubilee/controlling using Python using example notebooks
- Start brainstorming projects

##### 2:30-4:20p: Hackathon Work Time
- Finalize a project idea
- Work time!

#### Tuesday, April 15
##### 10:30a-12p: Hackathon Work Time
- Hackathon project work time continued!

##### 2:30-4:20p: Project Wrap-up
- Time to continue and wrap up projects

### Connecting to Jubilee
Much of this workshop involves doing various things with Jubilee, so the first step is to connect with the machine and open Jupyter Lab to talk to it. Here's how:

1. Turn on the machine.
2. Connect with the Ethernet cable.
3. Open Jupyter Lab: you can do this via the Terminal by typing `jupyter lab` or through VS Code.

### Repository Overview
This repository has introductory notebooks for each tool, along with some other relevant documentation.  They probably won't do exactly what you'd like, but will give you a starting point to work from! There's no need to run through every notebook; feel free to only use the ones relevant to your interests/your project idea. Here's a brief overview of the notebooks:

<<<<<<< HEAD
<<<<<<< HEAD
#### [Start Here](./start-here/)
=======
#### [General](./start-here/)
>>>>>>> 44b2f8c (update readme)
=======
#### [Start Here](./start-here/)
>>>>>>> a7e70c3 (Update README.md)
Start here! This folder contains a general introduction to using the machine (connecting, moving around, etc).

#### [Labware](./labware/)
Notebooks about using a laboratory automation deck to house labware. Check our these notebooks if you plan on doing liquid handling/navigating labware!

#### [Pipette](./pipette/)
Notebooks for liquid handling with the OT-2 Pipette. Run through the [labware](#labware) notebooks for more details on setting up labware.

#### [Syringe](./syringe/)
Notebooks for both liquid handling with the syringe tool, as well as printing gels. If you you want to do liquid handling with the syringe tool, run through the [labware](#labware) notebooks for more details on setting up labware.

#### [Spectral Sensor](./spectral-sensor/)
Notebooks for data collection with the spectral sensor.

#### [Camera](./camera/)
Notebooks for taking pictures and video using the camera tool.

#### [Calibration](./calibration/)
Some helper notebooks for various calibration tasks, in case your project calls for them.

#### [Extending Science Jubilee](./extending-science-jubilee/)
Resources on how to add a new tool to science jubilee.


## Installation
We will have laptops with the relevent software installed so you don't have to deal with any installation issues. But if you'd like to use your personal computer:

- Install `science-jubilee` using the instructions [here](https://science-jubilee.readthedocs.io/en/latest/getting_started/installation.html#installation)