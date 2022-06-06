import c4d

def main():
    cycleObjects(doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0))

def cycleObjects(objects):
    for obj in objects:
        cleanTracks(obj)    
        if (obj.GetChildren()!= None):
            cycleObjects(obj.GetChildren())

# Returns True if there is a difference in key values - meaning the track shouldn't be deleted
def checkKeyDifference(curve):
    key_value = 0
    flag = False

    # Iterates over keys in track and changes flag to True if the value != to the value of the first key
    for key_idx in range(curve.GetKeyCount()):
        if key_idx == 0:
            key_value = curve.GetKey(key_idx).GetValue()
        if curve.GetKey(key_idx).GetValue() != key_value
            flag = True    

    return flag

# Iterates over tracks in Curve and deletes those that have less than 3 keyframes that have the same value
def cleanTracks(object):
    for track in object.GetCTracks():
        if (track.GetCurve().GetKeyCount() <= 2 and (not checkKeyDifference(track.GetCurve()))):
            track.Remove()
                   
if __name__=='__main__':
    main()