from pprint import pprint
import csv
from collections import defaultdict
from regulars import reformat_phone_number


# Объединения значений в словаре
def merge_values(existing_value, new_value):
    if not existing_value:
        return new_value
    if not new_value:
        return existing_value
    if isinstance(existing_value, dict):
        if new_value not in existing_value.values():
            existing_value[len(existing_value) + 1] = new_value
    else:
        if existing_value != new_value:
            existing_value = {1: existing_value, 2: new_value}
    return existing_value


# Открытие и чтение CSV файла
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

grouped_contacts = defaultdict(lambda: {
    'lastname': '', 'firstname': '', 'surname': '', 'organization': '', 'position': '', 'phone': '', 'email': ''
})

# Обработка каждого контакта
for contact in contacts_list[1:]:
    raw = []
    for i in range(3):
        raw.append(contact[i])
    string_ = ' '.join(raw).split()
    lastname, firstname = string_[0], string_[1]
    surname = string_[2] if len(string_) > 2 else ''
    new_phone = reformat_phone_number(contact[5])
    key = (lastname, firstname)
    grouped_contacts[key]['lastname'] = lastname
    grouped_contacts[key]['firstname'] = firstname
    grouped_contacts[key]['surname'] = merge_values(grouped_contacts[key]['surname'], surname)
    grouped_contacts[key]['organization'] = merge_values(grouped_contacts[key]['organization'], contact[3])
    grouped_contacts[key]['position'] = merge_values(grouped_contacts[key]['position'], contact[4])
    grouped_contacts[key]['phone'] = merge_values(grouped_contacts[key]['phone'], new_phone)
    grouped_contacts[key]['email'] = merge_values(grouped_contacts[key]['email'], contact[6])

# Преобразование словаря в список
final_contacts_list = [contacts_list[0]]
for key, value in grouped_contacts.items():
    final_contacts_list.append([
        value['lastname'],
        value['firstname'],
        value['surname'],
        value['organization'],
        value['position'],
        value['phone'],
        value['email']
    ])

with open("phonebook.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(final_contacts_list)
