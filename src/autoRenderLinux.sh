#!/bin/sh


# *---------- CONFIGURE THIS ONLY ----------*
blenderInstallDir="C:\Program Files\Blender Foundation\Blender 2.93"
blenderFileName="NFTProject_Karambit.blend"
blenderInstallDir_Final=`echo $blenderInstallDir | sed -e 's/\\/\\\\/g'`
# *------------------------------------------*

# *---------- SET MAIN PROJECT DIR ----------*
currentFileDir=$PWD
cd $currentFileDir
cd ..
baseProjectDir=$PWD
# *------------------------------------------*


# *---------- START RENDERING ----------*
cd $blenderInstallDir_Final
blender $baseProjectDir\\inputFiles\\$blenderFileName --background --factory-startup --python $currentFileDir\\main.py
# *------------------------------------------*