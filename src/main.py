import bpy
import os
import sys
import importlib
import random
import json
import time
from datetime import date, datetime


dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)
sys.modules.values()
import config
importlib.reload(config)


def create_collection_dir():
    ''' Pre-Create the needed Folder Structure and Directories for the whole collection '''
    try:
        os.mkdir(config.collection_SavePath)
        os.mkdir(config.collection_SavePath + config.slash + config.PNG_FOLDER_NAME)
        os.mkdir(config.collection_SavePath + config.slash + config.METADATA_FOLDER_NAME)
        with open(config.collection_Cache_SavePath, "w") as cache_file:
            cache_file.write("0")

    except OSError:
        print ("Creation of the directory %s failed" % config.collection_SavePath)
    else:
        print ("Successfully created the directory %s " % config.collection_SavePath)


def render_and_save_collection():
    ''' Auto-Render and save the Output in the specified folder from config.py '''

    # Generate all rarity trails in one go so that we can use it later
    all_dropped_rarities = random.choices(config.color_palette_rarity, config.color_palette_rarity_drop_chance, k=config.NFT_Collection_Size)
    generation_counter = 0
    copy_nft_names_list = config.NFT_Collection_Names_List.copy()

    # Set counter from where we should continue for the generation from cache.txt
    try:
        with open(config.collection_Cache_SavePath) as cache_file:
            lines = cache_file.readlines()
            generation_counter = int(lines[0])
    except:
        print("No Collection Found! Creating New One...") 

    for i in range(0, config.NFT_Collection_Size):
        currentRarity = all_dropped_rarities[i]
        # all_dropped_rarities.remove(currentRarity)
        color_palette = get_color_palette(currentRarity)
        attributes = []

        # Apply to all defined MATERIALS from config.py the choosen HEX color code from choosen palette
        for key, value in config.NFT_Collection_Materials_Shaders_Names.items():
            current_Material_Name = key          # Material Name
            current_Shader_Name = value          # Shader Name
            rand_color = 0                       # HEX Color Value #fffff
            rgb_rand_color = [0, 0, 0]           # Color Values [Red, Green, Blue] 

            if config.NFT_Collection_Use_Rarity == True:
                rand_color = get_random_HEX_color_from_palette(color_palette)       # Get Random HEX Color Code From Choosen Color Palette
                rgb_rand_color = hextofloats(rand_color)                            # Convert HEX Color Code to RGB Color Code
            else:
                for index in range(0,3):
                    rand_color = round(random.random(), 2)
                    rgb_rand_color[index] = rand_color

            current_Attribute_Object = {
                "display_type": "boost_number",
                "trait_type": current_Material_Name,
                "value": rand_color,
                # "value": [red_value, green_value, blue_value]
            }
            attributes.append(current_Attribute_Object)
            bpy.data.materials[current_Material_Name].node_tree.nodes[current_Shader_Name].inputs[0].default_value = (rgb_rand_color[0], rgb_rand_color[1], rgb_rand_color[2], 1)
        
        currentDateTimeStamp = int(datetime.now().timestamp())
        dateObj = {
            "display_type": "date", 
            "trait_type": "birthday", 
            "value": currentDateTimeStamp
        }
        attributes.append(dateObj)
        # print(choosen_color_for_traid)
        # Set World Background Color RGBA
        # bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (rgb_bg_rand_color_from_palette[0], rgb_bg_rand_color_from_palette[1], rgb_bg_rand_color_from_palette[2], 1)

        name = random.choice(copy_nft_names_list)
        finalName = name  + " #" + str(generation_counter+1)
        copy_nft_names_list.remove(name)
        # currentDate = int(round(time.time() * 1000))              # for getting the current time now in millisecs 
        # currentDateTimeStamp = int(datetime.now().timestamp())

        # MetaData to be written
        metadata ={
            "description" : config.NFT_Collection_Description,
            "external_url" : "https://openseacreatures.io/3",
            "image" : config.NFT_Collection_BaseUri + str(generation_counter+1) + "." + config.NFT_Colletion_FileFormat,
            "name" : finalName,
            # "background_color" : bg_rand_color_from_palette,
            "seller_fee_basis_points": config.seller_fee_basis_points, # Indicates a 1% seller fee.
            "fee_recipient": config.fee_recipient, # Where seller fees will be paid to.
            "attributes": attributes
        }
        
        # Serializing json 
        json_object = json.dumps(metadata, indent = 4)
        
        # Write path json object
        metadataObj_savePath = config.collection_METADATA_SavePath + config.slash + str(generation_counter+1) + "#" + str(currentRarity) + ".json"

        # Save file to path
        with open(metadataObj_savePath, "w") as outfile:
            outfile.write(json_object)
            
        bpy.context.scene.render.filepath = config.collection_PNG_SavePath + config.slash + "{}#{}.".format(generation_counter+1, str(currentRarity)) + config.NFT_Colletion_FileFormat
        bpy.context.scene.render.resolution_x = config.NFT_Collection_Resolution[0]
        bpy.context.scene.render.resolution_y = config.NFT_Collection_Resolution[1]
        bpy.ops.render.render(write_still=True, use_viewport=True)
        generation_counter = generation_counter + 1

        # Set cache txt dir
        with open(config.collection_Cache_SavePath, "w") as cache_file:
            cache_file.write(str(generation_counter))


def get_color_palette(choosen_rarity):
    ''' Returns one color palette including the 5 hex colors defind in config.py depending on choosen rarity trail '''
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

def get_random_HEX_color_from_palette(palette):
    ''' Returns one random HEX code color from specified palette as parameter '''
    return palette[random.randint(0, len(palette)-1 ) ]

def hextofloats(hex):
    '''Takes a hex rgb string (e.g. #ffffff) and returns an RGB tuple (float, float, float).'''
    return tuple(int(hex[i:i + 2], 16) / 255. for i in (1, 3, 5)) # omit / skip: '#'


def main():
    ''' The Main Program '''
    print("#---------- CREATE_COLLECTION_DIR ----------#")
    create_collection_dir()
    print("#---------- END ----------#\n")


    print("#---------- RENDER_AND_SAVE_COLLECTION ----------#")
    render_and_save_collection()
    print("#---------- END ----------#\n")

main()