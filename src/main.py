import bpy
import os
import sys
import importlib
import random
import json
from datetime import date

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)
sys.modules.values()
import config
importlib.reload(config)

def create_collection_dir():
    try:
        os.mkdir(config.collection_SavePath)
        os.mkdir(config.collection_SavePath + config.slash + "PNGs")
        os.mkdir(config.collection_SavePath + config.slash + "METADATAs")
    except OSError:
        print ("Creation of the directory %s failed" % config.collection_SavePath)
    else:
        print ("Successfully created the directory %s " % config.collection_SavePath)


def render_and_save_collection():
    for i in range(1, config.maxNFTs +1):
        # Set World Background Color RGBA
        randRed_World = round(random.random(), 2)
        randGreen_World = round(random.random(), 2)
        randBlue_World = round(random.random(), 2)
        bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (randRed_World, randGreen_World, randBlue_World, 1)

        # Set Blade Mat Color RGBA
        randRed_Blade = round(random.random(), 2)
        randGreen_Blade = round(random.random(), 2)
        randBlue_Blade = round(random.random(), 2)
        bpy.data.materials["Blade"].node_tree.nodes["Glossy BSDF"].inputs[0].default_value = (randRed_Blade, randGreen_Blade, randBlue_Blade, 1)

        # Set Handle Mat Color RGBA
        randRed_Handle = round(random.random(), 2)
        randGreen_Handle = round(random.random(), 2)
        randBlue_Handle = round(random.random(), 2)
        bpy.data.materials["Handle"].node_tree.nodes["Glossy BSDF"].inputs[0].default_value = (randRed_Handle, randGreen_Handle, randBlue_Handle, 1)


        knife_names_list = [
            "Hell's Scream",
            "Dragontooth",
            "Scalpel",
            "Feral Dagger",
            "Vengeance Scalpel",
            "Eternal Steel Sculptor",
            "Stormguard Ebon Skewer",
            "Midnight, Voice of the Fallen",
            "Rigormortis, Champion of Infinite Trials",
            "Crucifix, Etcher of the Ancients",
            "Death's Kiss",
            "Heartseeker",
            "Oathkeeper",
            "Storm Sabre",
            "Soul-Forged Deflector",
            "Undead Gold Carver",
            "Fiery Obsidian Doomblade",
            "Lynch, Cry of Stealth",
            "Laceration, Deflector of the East",
            "Requiem, Favor of Nightmares"
        ]

        name = random.choice(knife_names_list)
        finalName = name  + " #" + str(i)
        knife_names_list.remove(name)
        currentData = date.today()

        # Data to be written
        metadata ={
            "name" : finalName,
            "description" : config.NFTcollectionDescription,
            "image" : config.NFTcollectionBaseUri,
            "dna" : "something",
            "edition" : "some edidition",
            "data" : str(currentData),
            "attributes" : {
                "environment_color_red" : randRed_World,
                "environment_color_green" : randGreen_World,
                "environment_color_blue" : randBlue_World,
                
                "blade_color_red" : randRed_Blade,
                "blade_color_green" : randGreen_Blade,
                "blade_color_blue" : randBlue_Blade,
                
                "handle_color_blue" : randBlue_Handle,
                "handle_color_blue" : randBlue_Handle,
                "handle_color_blue" : randBlue_Handle
            }
        }
        
        # Serializing json 
        json_object = json.dumps(metadata, indent = 4)
        
        #write path json object
        metadataObj_savePath = config.collection_METADATA_SavePath + config.slash + str(i) + ".json"

        # Save file to path
        with open(metadataObj_savePath, "w") as outfile:
            outfile.write(json_object)




        
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