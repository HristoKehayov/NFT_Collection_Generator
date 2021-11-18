import bpy
import os
import sys
import importlib
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)
sys.modules.values()
import config
importlib.reload(config)

def create_collection_dir():
    try:
        os.mkdir(config.collection_SavePath)
        os.mkdir(config.collection_SavePath + config.slash + "PNGs")
        os.mkdir(config.collection_SavePath + config.slash + "METATAGs")
    except OSError:
        print ("Creation of the directory %s failed" % config.collection_SavePath)
    else:
        print ("Successfully created the directory %s " % config.collection_SavePath)


def render_and_save_collection():
    for i in range(1, config.maxNFTs +1):
        # Set World Background Color RGBA
        randRed_World = random.random()
        randGreen_World = random.random()
        randBlue_World = random.random()
        bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (randRed_World, randGreen_World, randBlue_World, 1)

        # Set Blade Mat Color RGBA
        randRed_Blade = random.random()
        randGreen_Blade = random.random()
        randBlue_Blade = random.random()
        bpy.data.materials["Blade"].node_tree.nodes["Glossy BSDF"].inputs[0].default_value = (randRed_Blade, randGreen_Blade, randBlue_Blade, 1)

        # Set Handle Mat Color RGBA
        randRed_Handle = random.random()
        randGreen_Handle = random.random()
        randBlue_Handle = random.random()
        bpy.data.materials["Handle"].node_tree.nodes["Glossy BSDF"].inputs[0].default_value = (randRed_Handle, randGreen_Handle, randBlue_Handle, 1)

        
        # save PNGs
        # save as meta (soon...)
        bpy.context.scene.render.filepath = config.collection_PNG_SavePath + config.slash + "{}.".format(i) + config.imageFileFormat
        bpy.ops.render.render(write_still=True, use_viewport=True)

def main():
    print("#---------- CREATE_COLLECTION_DIR ----------#")
    create_collection_dir()
    print("#---------- END ----------#\n")


    print("#---------- RENDER_AND_SAVE_COLLECTION ----------#")
    render_and_save_collection()
    print("#---------- END ----------#\n")

main()