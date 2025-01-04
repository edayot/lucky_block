

execute as @a[tag=convention.debug] run function lucky_block:impl/print_version


schedule function lucky_block:impl/tick 1t replace
