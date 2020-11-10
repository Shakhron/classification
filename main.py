import xml.etree.ElementTree as ET
import numpy as np

def euclide(a, b):
    c = a - b
    c = np.power(np.sum(np.power(c, 2)), 0.5)
    return c

def read_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    classes = {}
    examples = []
    for elem in root:
        source = []
        for i in range(10):
            source.append(list(map(int, elem[i].get("n").split())))
        clss = elem.get("class")
        if clss == "0":
            examples.append(source)
            continue
        if clss in classes:
            classes[clss].append(source)
        else:
            classes[clss] = [source]
    return classes, examples

classes, examples = read_from_xml("input.xml")

def nuclearisation_of_class(classes):
    classes_nucleos = {}
    for cl in classes.keys():
        classes_nucleos[cl] = list(map(lambda x: np.array(x, dtype=np.float32), classes[cl]))
        quantity = len(classes[cl])
        nucleos = np.zeros([10, 10], dtype=np.float32)
        for i in classes[cl]:
            nucleos = nucleos + i
        nucleos = nucleos / quantity
        nucleos = np.around(nucleos)
        classes_nucleos[cl] = nucleos
    return classes_nucleos

def classification(example, nucleo_classes):
    example = np.array(example, dtype=np.float32)
    distants = []
    for nc in nucleo_classes.keys():
        distants.append((euclide(nucleo_classes[nc], example), nc))
    distants.sort()
    return distants[0][1]


fb = open('result.txt', 'w')
for i in range(0,4):
    fb.write('\nОбъект: ')
    for j in range(0,10):
        fb.write('\n')
        for elements in examples[i][j]:
            fb.write(str(elements))
            fb.write(' ')
    fb.write('\nКласс к котрому он принадлежит:\n')
    fb.write(classification(examples[i], nuclearisation_of_class(classes)))
fb.close()
print('Ответ записан в файл result')




