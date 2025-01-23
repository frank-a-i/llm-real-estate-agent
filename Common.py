import os
import PIL
from PIL import Image

import dataclasses

ASSETS_FILE_PATH = os.path.join(os.getcwd(), "generated_raw_assets.pickle")
FRESH_ASSETS_FILE_PATH = os.path.join(os.getcwd(), "freshly_generated_raw_assets.pickle")

@dataclasses.dataclass
class RealEstateAttributes:
    district: str # The name of the area
    price: int # The value for the housing object
    bedrooms: int # The amount of bedrooms the housing object offers
    bathrooms: int # The amount of bathrooms the housing object offers
    living_space: float # The area that the housing object offers in square meters
    neighborhood: str # A description what the vicinity looks like
    parking_space: str # A description what the parking options are for the home owner
    heating: str #The type of the main heating source
    internet: str #The bandwith of available internet connection

    def to_dict(self):
        return vars(self)

@dataclasses.dataclass
class ExportAsset:
    attributes: RealEstateAttributes
    image: Image
    image_subtitle: str

    def structuredStr(self, delimiter="\n"):
        attribute_str = f""
        for key, value in dataclasses.asdict(self.attributes).items():
            attribute_str = f"{attribute_str} {key} : {value} {delimiter}"
        return attribute_str
