count = 0
labels = []
with open('mscoco_complete_label_map.pbtxt') as f:
    for line in f.readlines():
        if "display_name" in line:
            labels.append(line[17:-2])
labels= [(v, i) for i, v in enumerate(labels)]