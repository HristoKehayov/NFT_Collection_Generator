# @echo off

# @REM *---------- CONFIGURE THIS ONLY ----------*
# set blenderInstallDir=C:\Program Files\Blender Foundation\Blender 2.93
# set blenderFileName=NFTProject_Karambit.blend
# @REM *------------------------------------------*


# @REM *---------- SET MAIN PROJECT DIR ----------*
# set currentDir=%cd%
# cd %currentDir%
# cd ..
# set "mainRepoDir=%cd%"
# @REM *------------------------------------------*


# @REM *---------- START RENDERING ----------*
# cd %blenderInstallDir%
# blender %mainRepoDir%\inputFiles\%blenderFileName% --background --python %currentDir%\main.py
# Pause
# @REM *------------------------------------------*