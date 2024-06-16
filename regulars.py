import re


phone_pattern = re.compile(
    r'(\+?7|8)[\s\-\(]*(\d{3})[\s\-\)]*(\d{3})[\s\-]*(\d{2})[\s\-]*(\d{2})(?:\s*\(?доб\.?\s*(\d{1,4})\)?)?'
)


def reformat_phone_number(phone):
    match = phone_pattern.search(phone)
    if match:
        formatted_phone = f"+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)}"
        if match.group(6):
            formatted_phone += f" доб.{match.group(6)}"
        return formatted_phone
    return phone
