import platform

# ------------ CONSTANTS: ------------ #
COMMON = "Common"
RARE = "Rare"
EPIC = "Epic"
LEGENDARY = "Legendary"
PNG_FOLDER_NAME = "PNGs"
METADATA_FOLDER_NAME = "METADATAs"
CACHE_FILE_EXTENTION = "txt"
# ------------------------------------ #

# ------------ NFT CONFIGURATIONS: ------------ #
NFT_Collection_Size = 5                                                                                    # The maximum number of NFTs you want to generate
NFT_Collection_Name = 'EyeGlasses'                                                                             # The name of the NFT Collection
NFT_Collection_Description = NFT_Collection_Name + ' Collection'                                            # The Description of the NFT Collection
NFT_Collection_BaseUri = 'https://storage.googleapis.com/opensea-prod.appspot.com/' + NFT_Collection_Name   # The image hosting url of all generated pngs 
NFT_Colletion_FileFormat = 'png'                                                                            # Dictate the image extension when Blender renders the images
NFT_Collection_Resolution = [350, 350]                                                                      # The Width, Height of each generated image resolution [0] = width, [1] = height
NFT_Collection_Use_Rarity = False                                                                            # Should I use the predefined rarity palette and choose colors from there? If False choose random float value from [0:1]
NFT_Collection_Materials_Shaders_Names = {                                                                # Define The { MaterialName : ShaderName } you want to have different Variants                        
    "Handle_Mat": "Principled BSDF", 
    "Frame_Mat": "Principled BSDF", 
    "Eyes_Mat": "Glass BSDF", 
}
# NFT_Collection_Materials_Shaders_Names = {                                                                  # Define The { MaterialName : ShaderName } you want to have different Variants                        
#     "Handle": "Glossy BSDF", 
#     "Screw": "Glossy BSDF", 
#     "Blade": "Glossy BSDF", 
# }
NFT_Collection_Names_List = [
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
# NFT_Collection_Traids = ["Handle", "Frame", "Eyes"]

# maxNFTsPerPallet = 3                                                                                      # The maximum number of NFTs for each color pallet
color_palette_rarity = [COMMON, RARE, EPIC, LEGENDARY]
color_palette_rarity_drop_chance = [60, 30, 5, 5]
color_palettes = {
    # https://colors.muz.li/

    # Red
    COMMON: {
        "Analogic": ["ff4d4d", "b33636", "ff944d", "ff4dd3", "b33693"],
        "Tetrade": ["ff4d4d", "4dff4d", "36b336", "ffa64d", "b37436"],
        "Mono": ["ff4d4d", "b33636", "ffd3d3", "ffa6a6", "ffffff"],
    }, 

    # Blue
    RARE: {
        "Analogic": ["4d4dff", "3655b3", "884dff", "4dffff", "36b3b3"],
        "Tetrade": ["4d4dff", "ffb84d", "b38136", "974dff", "6a36b3"],
        "Mono": ["4d4dff", "3655b3", "d3deff", "a6bcff", "ffffff"],
    }, 

    # Purple
    EPIC: {
        "Analogic": ["8a2be2", "4a1e9e", "a92be2", "2d57e2", "1f3d9e"],
        "Tetrade": ["8a2be2", "e2bf2b", "9e861e", "e22bde", "9e1e9c"],
        "Mono": ["8a2be2", "4a1e9e", "ddcbff", "bb98ff", "ffffff"],
    },

    # Gold
    LEGENDARY: {
        "Analogic": ["ffa500", "b38b00", "fffa00", "ff9400", "b36800"],
        "Tetrade": ["ffa500", "4a08ff", "3406b3", "d6ff00", "96b300"],
        "Mono": ["ffa500", "b38b00", "fff1bf", "ffe380", "ffffff"],

    }
}
# ------------------------------------------------ #


# ------------ NFT ROYALTY CONFIGURATION: ------------ #
seller_fee_basis_points = 100                                                                               # Indicates a 1% seller fee. (Royalties)
fee_recipient = "0xA97F337c39cccE66adfeCB2BF99C1DdC54C2D721"                                                # Where seller fees will be paid to.
# ---------------------------------------------------- #

# ------------ SAVE PATH CONFIGURATIONS ------------ #
save_path_mac = ''
save_path_linux = ''
save_path_windows = r'C:\Users\Hristo-PC-RTX\Desktop\NFT_Collection_Generator\outputFiles'
# Place the path in the '', e.g: save_path_mac = '/Users/Path/to/Blend_My_NFTs'
# Example mac: /Users/Path/to/Blend_My_NFTs
# Example windows: C:\Users\Path\to\Blend_My_NFTs
# ------------------------------------------------ #




# ------------------------------------------------ #
# ------------ Utilities - DON'T TOUCH ----------- #
# ------------------------------------------------ #
mac = 'Darwin'                                                                                              # Mac OS same as Linux
windows = 'Windows'                                                                                         # Windows
linux = 'Linux'                                                                                             # Linux same as Mac OS
slash = ''                                                                                                  # Leave empty
save_path = None                                                                                            # Leave empty

# Save_path utilities and os compatibility
if platform.system() == mac:
    save_path = save_path_mac
    slash = '/'
elif platform.system() == linux:
    save_path = save_path_linux
    slash = '/'
elif platform.system() == windows:
    save_path = save_path_windows
    slash = '\\'

collection_SavePath = save_path + slash + NFT_Collection_Name + "_Collection"
collection_PNG_SavePath = collection_SavePath + slash + PNG_FOLDER_NAME
collection_METADATA_SavePath = collection_SavePath + slash + METADATA_FOLDER_NAME
collection_Cache_SavePath = collection_SavePath + slash + "cache." + CACHE_FILE_EXTENTION
# ------------------------------------------------ #