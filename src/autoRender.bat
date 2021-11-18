@echo off 
set blenderInstallDir=C:\Program Files\Blender Foundation\Blender 2.93
cd %blenderInstallDir%
echo  %blenderInstallDir%
blender %HOMEPATH%\Desktop\NFT_Collection_Generator\inputFiles\NFTProject_Karambit.blend --background --python C:\Users\Hristo-PC-RTX\Desktop\NFT_Collection_Generator\src\main.py
set /p DUMMY=Hit ENTER to continue...