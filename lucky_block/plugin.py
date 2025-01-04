from beet import Context
from simple_item_plugin.types import NAMESPACE, Lang
from simple_item_plugin.item import Item, BlockProperties
from simple_item_plugin.crafting import ShapedRecipe, VanillaItem



def beet_default(ctx: Context):
    lucky_block = Item(
        id="lucky_block",
        base_item="minecraft:beehive",
        item_name=(
            f"{NAMESPACE}.item.lucky_block",
            {Lang.en_us: "Lucky block", Lang.fr_fr: "Bloc de la chance"},
        ),
        block_properties=BlockProperties(
            base_block="minecraft:beehive",
            all_same_faces=True,
        )
    ).export(ctx)
