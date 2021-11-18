import platform

# ------------ NFT CONFIGURATIONS: ------------ #
maxNFTs = 3  # The maximum number of NFTs you want to generate
NFTcollectionName = 'Karambit'  # The name of the NFT Collection
NFTcollectionDescription = 'Test Collection for Karambits'  # The Description of the NFT Collection
NFTcollectionBaseUri = 'ipfs://NewUriToReplace'  # The image hosting url of all generated pngs 

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


imageFileFormat = 'PNG'  # Dictate the image extension when Blender renders the images
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