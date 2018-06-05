return [
    component
    for feeds, component in COMPONENTS_MAPPING.items() if feed in feeds
][0]

You could do this (generator comprehension + next) to avoid iterating through the whole list if you only need the first element:

try:
    return next(
        component for feeds, component in COMPONENTS_MAPPING.items()
        if feed in feeds
    )
except StopIteration:
    raise FeedNotFound from e

