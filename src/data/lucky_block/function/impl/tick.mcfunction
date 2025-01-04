execute 
    as @e[type=item_display,tag=lucky_block.block.beehive,predicate=!lucky_block:impl/destroy_beehive] 
    at @s
    run function ./blocks/destroy_beehive


schedule function lucky_block:impl/tick 1t replace