@echo off

@REM *---------- CONFIGURE THIS ONLY ----------*
set blenderInstallDir=C:\Program Files\Blender Foundation\Blender 2.93
set blenderFileName=glasses_project_alexis_NO_Modifiers.blend
@REM *------------------------------------------*


@REM *---------- SET MAIN PROJECT DIR ----------*
set currentFileDir=%cd%
cd %currentFileDir%
cd ..
set "baseProjectDir=%cd%"
@REM *------------------------------------------*


@REM *---------- START RENDERING ----------*
cd %blenderInstallDir%
blender %baseProjectDir%\inputFiles\%blenderFileName% --background --python %currentFileDir%\main.py
@REM Pause
@REM --factory-startup
@REM *------------------------------------------*