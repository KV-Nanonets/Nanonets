import xml.sax

# Define a custom SAX ContentHandler class to handle events
class TravelPackageHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.packages = []
        self.current_package = {}
        self.current_element = ""
        self.current_payment = {}

    def startElement(self, name, attrs):
        self.current_element = name
        if name == "package":
            self.current_package = {"id": attrs.getValue("id")}

    def characters(self, content):
        if self.current_element in ["description", "destination", "price", "duration", "EMIoption", "refund"]:
            self.current_package[self.current_element] = content.strip()
        if self.current_element == "payment":
            self.current_payment = {}

    def endElement(self, name):
        if name == "package":
            self.current_package["payment"] = self.current_payment
            self.packages.append(self.current_package)
        if name == "payment":
            self.current_package["payment"] = self.current_payment

    def startElementNS(self, name, qname, attrs):
        pass

    def endElementNS(self, name, qname):
        pass
    
# Create a SAX parser object
parser = xml.sax.make_parser()
handler = TravelPackageHandler()
parser.setContentHandler(handler)
parser.parse("travel_pckgs.xml")

for package in handler.packages:
  print(f'Package: {package["id"]}')