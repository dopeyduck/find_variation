import csv
from lxml import etree
import os
from tabulate import tabulate

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

# Prompt for the CSV file name
csv_file_name = input("Please enter the name of the CSV file to save the results: ")
csv_file_path = os.path.join(os.path.dirname(__file__), csv_file_name)

# Open and parse the XML file
with open(xml_file_path, 'r') as file:
    tree = etree.parse(file)

# Find all variation units
variation_units = tree.xpath('//tei:app', namespaces=ns)

# Prepare the results list
results = []

# Process each variation unit
for vu in variation_units:
    vu_id = vu.get('n')
    vu_from = vu.get('from')
    vu_to = vu.get('to')
    
    # Process each reading within the variation unit
    for rdg in vu.xpath('tei:rdg', namespaces=ns):
        rdg_witnesses = set(rdg.get('wit').split())
        rdg_varSeq = rdg.get('varSeq')
        rdg_n = rdg.get('n')
        rdg_type = rdg.get('type')
        
        # Check if the reading includes all included witnesses and excludes all excluded witnesses
        if included_witnesses.issubset(rdg_witnesses) and excluded_witnesses.isdisjoint(rdg_witnesses):
            # Check the number of other witnesses
            other_witnesses = rdg_witnesses - included_witnesses
            if len(other_witnesses) <= max_other_witnesses:
                results.append([vu_id, vu_from, vu_to, rdg_n, rdg_varSeq, rdg_type, ' '.join(rdg_witnesses)])

# Write the results to a CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Variation Unit', 'From', 'To', 'Reading', 'VarSeq', 'Type', 'Witnesses'])
    writer.writerows(results)

# Print the results in a tabular format
print(tabulate(results, headers=['Variation Unit', 'From', 'To', 'Reading', 'VarSeq', 'Type', 'Witnesses']))