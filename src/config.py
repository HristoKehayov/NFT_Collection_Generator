import platform

# ------------ CONSTANTS: ------------ #
COMMON = "Common"
RARE = "Rare"
EPIC = "Epic"
LEGENDARY = "Legendary"
# ------------------------------------ #

# ------------ NFT CONFIGURATIONS: ------------ #
maxNFTs = 3  # The maximum number of NFTs you want to generate
NFTcollectionName = 'Karambit'  # The name of the NFT Collection
NFTcollectionDescription = 'Test Collection for Karambits'  # The Description of the NFT Collection
NFTcollectionBaseUri = 'ipfs://NewUriToReplace'  # The image hosting url of all generated pngs 
imageFileFormat = 'PNG'  # Dictate the image extension when Blender renders the images

# solanaMetadata = {
#   symbol: "YC",
#   seller_fee_basis_points: 1000, # Define how much % you want from secondary market sales 1000 = 10%
#   external_url: "https://www.youtube.com/c/hashlipsnft",
#   creators: [
#     {
#       address: "7fXNuer5sbZtaTEPhtJ5g5gNtuyRoKkvxdjEjEnPN4mC",
#       share: 100,
#     },
#   ],
# }

maxNFTsPerPallet = 3 # The maximum number of NFTs for each color pallet
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


# ------------ SAVE PATH CONFIGURATIONS ------------ #
save_path_mac = ''
save_path_windows = r'C:\Users\Hristo-PC-RTX\Desktop\NFT_Collection_Generator\outputFiles'
# Place the path in the '', e.g: save_path_mac = '/Users/Path/to/Blend_My_NFTs'
# Example mac: /Users/Path/to/Blend_My_NFTs
# Example windows: C:\Users\Path\to\Blend_My_NFTs
# ------------------------------------------------ #


# ------------ Utilities - DON'T TOUCH ------------ #
mac = 'Darwin'  # Mac OS
windows = 'Windows'  # Windows
slash = ''  # Leave empty
save_path = None  # Leave empty

# Save_path utilities and os compatibility
if platform.system() == mac:
    save_path = save_path_mac
    slash = '/'
elif platform.system() == windows:
    save_path = save_path_windows
    slash = '\\'

collection_SavePath = save_path + slash + NFTcollectionName + "_Collection"
collection_PNG_SavePath = collection_SavePath + slash + "PNGs"
collection_METADATA_SavePath = collection_SavePath + slash + "METADATAs"
# ------------------------------------------------ #