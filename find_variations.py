import json
from lxml import etree

# Define the namespace
ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

# Get the path of the XML file from the user
xml_file_path = input("Please enter the path of the XML file: ")

# Prompt for a set of included witnesses
included_witnesses_input = input("Please enter the set of included witnesses (space or comma-separated): ")
included_witnesses = set(included_witnesses_input.replace(',', ' ').split())

# Prompt for a set of excluded witnesses
excluded_witnesses_input = input("Please enter the set of excluded witnesses (space or comma-separated, or leave blank if none): ")
excluded_witnesses = set(excluded_witnesses_input.replace(',', ' ').split()) if excluded_witnesses_input else set()

# Prompt for the maximum number of other witnesses
max_other_witnesses = int(input("Please enter the maximum number of other witnesses that may be present: "))

# Open and parse the XML file
with open(xml_file_path, 'r') as file:
    tree = etree.parse(file)

# Iterate over all 'app' elements
for app in tree.xpath('//tei:app', namespaces=ns):
    rdgs = app.xpath('.//tei:rdg', namespaces=ns)
    for rdg in rdgs:
        wit_set = set(rdg.get('wit', '').split())
        if not wit_set:
            continue
        # Check if any excluded witnesses are present
        if wit_set & excluded_witnesses:
            continue
        included_count = len(wit_set & included_witnesses)
        other_witnesses_count = len(wit_set - included_witnesses)
        if included_count > 0 and other_witnesses_count <= max_other_witnesses:
            witnesses_str = ' '.join(wit_set)
            print(f"{app.get('n')}\t{app.get('from')}\t{app.get('to')}\t{rdg.get('n')}\t{witnesses_str}\t{rdg.text}")