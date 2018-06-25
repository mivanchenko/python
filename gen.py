#!/usr/bin/env python3

items = [
    [
        ['feed1', 'feed2'], 'component12'
    ],
    [
        ['feed3', 'feed4'], 'component34'
    ],
]
feed = 'feed5'

def get_list_item():
    try:
        return [
            component
            for feeds, component in items if feed in feeds
        ][0]
    except IndexError:
        return 'Feed not found'

# You could do this (generator comprehension + next) to avoid iterating
# through the whole list if you only need the first element
def get_gen_item():
    try:
        return next(
            component
            for feeds, component in items if feed in feeds
        )
    except StopIteration:
        return 'Feed not found'

print(get_list_item())
print(get_gen_item())
