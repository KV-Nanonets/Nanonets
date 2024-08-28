import xml.etree.ElementTree as ET
import csv

def xml_to_csv(xml_file, csv_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Open a CSV file for writing
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Write the header
        header = ['id', 'description', 'destination', 'price', 'duration', 'EMIoption', 'refund']
        writer.writerow(header)

        # Write the rows
        for package in root.findall('package'):
            row = [
                package.get('id'),
                package.find('description').text,
                package.find('destination').text,
                package.find('price').text,
                package.find('duration').text,
                package.find('payment/EMIoption').text,
                package.find('payment/refund').text
            ]
            writer.writerow(row)

# Example usage
xml_file = 'travel_pckgs.xml'
csv_file = 'travel_packages.csv'
xml_to_csv(xml_file, csv_file)