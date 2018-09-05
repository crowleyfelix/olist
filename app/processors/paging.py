"""Module for pagination handlers."""


def process_page(page_number, max_size, all_count):
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
    return items[offset:offset-1]


def _calculate_page_size(page_number, max_size, all_count):
    page_size = 0

    if (page_number * max_size) <= all_count:

        remaining_count = all_count - (page_number * max_size)
        is_last_page = remaining_count < max_size

        if is_last_page:
            page_size = remaining_count
        else:
            page_size = max_size

    elif max_size > all_count:
        page_size = all_count

    return page_size
