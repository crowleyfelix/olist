"""Module for pagination handlers."""


def process(page_number, max_size, all_count):
    """Process page."""
    page_info = {
        "current": page_number,
        "size":    _calculate_page_size(page_number, max_size, all_count),
        "max_size": max_size
    }

    if page_number > 1:
        page_info["previous"] = page_number - 1

    if (page_number * max_size) < all_count:
        page_info["next"] = page_number + 1

    return page_info


def filter(items, page, limit):
    """Filter page."""
    offset = (page-1) * limit
    return items[offset:offset+limit]


def _calculate_page_size(page_number, max_size, all_count):

    start_offset = (page_number-1) * max_size
    next_offset = page_number * max_size
    is_last_page = next_offset >= all_count

    if start_offset >= all_count:
        page_size = 0
    elif is_last_page:
        page_size = all_count - start_offset
    else:
        page_size = max_size

    return page_size
