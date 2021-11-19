import bpy
import os
import sys
import importlib
import random
import json
import time

from collections import Counter

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
    all_dropped_rarities = random.choices(config.color_palette_rarity, config.color_palette_rarity_drop_chance, k=config.maxNFTs)
    for i in range(0, config.maxNFTs):
        currentRarity = all_dropped_rarities[i]
        # all_dropped_rarities.remove(currentRarity)
        color_palette = get_color_palette(currentRarity)

        # Get Background Color
        bg_rand_color_from_palette = color_palette[random.randint(0, len(color_palette)-1 ) ]
        # color_palette.remove(bg_rand_color_from_palette)
        rgb_bg_rand_color_from_palette = hextofloats(bg_rand_color_from_palette)

        # Get Blade Color
        blade_rand_color_from_palette = color_palette[random.randint(0, len(color_palette)-1 ) ]
        # color_palette.remove(blade_rand_color_from_palette)
        rgb_blade_rand_color_from_palette = hextofloats(blade_rand_color_from_palette)

        # Get Handle Color
        handle_rand_color_from_palette = color_palette[random.randint(0, len(color_palette)-1 ) ]
        # color_palette.remove(handle_rand_color_from_palette)
        rgb_handle_rand_color_from_palette = hextofloats(handle_rand_color_from_palette)

        # Set World Background Color RGBA
        # randRed_World = round(random.random(), 2)
        # randGreen_World = round(random.random(), 2)
        # randBlue_World = round(random.random(), 2)
        # bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (randRed_World, randGreen_World, randBlue_World, 1)
        bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (rgb_bg_rand_color_from_palette[0], rgb_bg_rand_color_from_palette[1], rgb_bg_rand_color_from_palette[2], 1)

        # Set Blade Mat Color RGBA
        # randRed_Blade = round(random.random(), 2)
        # randGreen_Blade = round(random.random(), 2)
        # randBlue_Blade = round(random.random(), 2)
        # bpy.data.materials["Blade"].node_tree.nodes["Glossy BSDF"].inputs[0].default_value = (randRed_Blade, randGreen_Blade, randBlue_Blade, 1)
        bpy.data.materials["Blade"].node_tree.nodes["Glossy BSDF"].inputs[0].default_value = (rgb_blade_rand_color_from_palette[0], rgb_blade_rand_color_from_palette[1], rgb_blade_rand_color_from_palette[2], 1)

        # Set Handle Mat Color RGBA
        # randRed_Handle = round(random.random(), 2)
        # randGreen_Handle = round(random.random(), 2)
        # randBlue_Handle = round(random.random(), 2)
        # bpy.data.materials["Handle"].node_tree.nodes["Glossy BSDF"].inputs[0].default_value = (randRed_Handle, randGreen_Handle, randBlue_Handle, 1)
        bpy.data.materials["Handle"].node_tree.nodes["Glossy BSDF"].inputs[0].default_value = (rgb_handle_rand_color_from_palette[0], rgb_handle_rand_color_from_palette[1], rgb_handle_rand_color_from_palette[2], 1)

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
        finalName = name  + " #" + str(i+1)
        knife_names_list.remove(name)
        currentDate = int(round(time.time() * 1000)) #for getting the current time now in millisecs 

        # Data to be written
        metadata ={
            "name" : finalName,
            "description" : config.NFTcollectionDescription,
            "image" : config.NFTcollectionBaseUri,
            "dna" : "something",
            "edition" : "some edidition",
            "date" : str(currentDate),
            "attributes" : {
                "environment_color_red" : rgb_bg_rand_color_from_palette,
                
                "blade_color_red" : rgb_blade_rand_color_from_palette,
                
                "handle_color_blue" : rgb_handle_rand_color_from_palette,
            }
        }
        
        # Serializing json 
        json_object = json.dumps(metadata, indent = 4)
        
        #write path json object
        metadataObj_savePath = config.collection_METADATA_SavePath + config.slash + str(i+1) + "#" + str(currentRarity) + ".json"

        # Save file to path
        with open(metadataObj_savePath, "w") as outfile:
            outfile.write(json_object)
        bpy.context.scene.render.filepath = config.collection_PNG_SavePath + config.slash + "{}#{}.".format(i+1, str(currentRarity)) + config.imageFileFormat
        bpy.ops.render.render(write_still=True, use_viewport=True)


def get_color_palette(choosen_rarity):
    color_palette=[]
    if choosen_rarity == config.COMMON:
        # Common
        randIndex = random.randint(0, len(config.color_palettes[config.COMMON]) -1 )
        color_palette = list(config.color_palettes[config.COMMON].values())[randIndex]
        pass
    elif choosen_rarity == config.RARE:
        # Rare
        randIndex = random.randint(0, len(config.color_palettes[config.RARE]) -1 )
        color_palette = list(config.color_palettes[config.RARE].values())[randIndex]
        pass
    elif choosen_rarity == config.EPIC:
        # Epic
        randIndex = random.randint(0, len(config.color_palettes[config.EPIC]) -1 )
        color_palette = list(config.color_palettes[config.EPIC].values())[randIndex]
        pass
    else:
        # Legendary
        randIndex = random.randint(0, len(config.color_palettes[config.LEGENDARY]) -1 )
        color_palette = list(config.color_palettes[config.LEGENDARY].values())[randIndex]
        pass

    return color_palette

def hextofloats(h):
    '''Takes a hex rgb string (e.g. #ffffff) and returns an RGB tuple (float, float, float).'''
    return tuple(int(h[i:i + 2], 16) / 255. for i in (1, 3, 5)) # skip '#'


def main():
    print("#---------- CREATE_COLLECTION_DIR ----------#")
    create_collection_dir()
    print("#---------- END ----------#\n")


    print("#---------- RENDER_AND_SAVE_COLLECTION ----------#")
    render_and_save_collection()
    print("#---------- END ----------#\n")

main()