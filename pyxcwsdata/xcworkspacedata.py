import os
import xml.etree.ElementTree as xml

class xcworkspacedata(object):
    
    def __init__(self, wsdata_file_path):
        self.filePath = wsdata_file_path
        try:
            self.contents = xml.parse(self.filePath)
        except:
            print('Unable to load contents.xcworkspacedata file!')
            raise
        
        self.objects = set()
        for child in self.contents.getroot():
            print child.tag