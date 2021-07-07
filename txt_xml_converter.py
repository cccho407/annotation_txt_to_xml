import os
import cv2
from xml.etree.ElementTree import Element, ElementTree, SubElement, dump

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


if __name__=="__main__":
    annotation_path="./Annotations"
    img_path="./Images"
    xml_path="./xml"
    createFolder(xml_path)
    file_list = os.listdir(annotation_path)
    print(len(file_list))

    for i in file_list:
        r = open(annotation_path +'/'+ i,mode='rt')
        r.seek(0)
        num = r.readline()
        img_name = i[:-4]
        xml_name = i[:-8] + ".xml"
        img = cv2.imread(img_path+'/'+img_name)
        h,w,c = img.shape
        #make xml file
        root = Element("annotatioin")
        SubElement(root,"filename").text = img_name
        node_size = SubElement(root,"size")
        SubElement(node_size,"width").text = str(w)
        SubElement(node_size,"height").text = str(h)
        SubElement(node_size,"depth").text = str(c)
        for a in range(int(num)):
            data = r.readline()
            list_data = data.split()
            node_object = SubElement(root,"object")
            SubElement(node_object,"name").text = "person"
            node_bndbox = SubElement(node_object,"bndbox")
            SubElement(node_bndbox,"xmin").text = str(list_data[1])
            SubElement(node_bndbox,"ymin").text = str(list_data[2])
            SubElement(node_bndbox,"xmax").text = str(list_data[3])
            SubElement(node_bndbox,"ymax").text = str(list_data[4])
        indent(root)
        dump(root)
        ElementTree(root).write(xml_path+'/'+xml_name)        
            