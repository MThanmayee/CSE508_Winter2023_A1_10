def AND_merge(list1, list2):
    comparisons = 0
    ANDSet = set()
    ptr1 ,ptr2 = 0,0
    len1 = len(list1)
    len2 = len(list2)
    list1.sort()
    list2.sort()
    while ptr1 < len1 and ptr2 < len2:
        if list1[ptr1] == list2[ptr2]:
            ANDSet.add(list1[ptr1])
            ptr1 += 1
            ptr2 += 1
            comparisons += 1
        else:
            comparisons += 2
            if list1[ptr1] < list2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1
    ANDSet = list(ANDSet)
    return ANDSet,comparisons

def ANDNOT_merge(list1, list2):
    comparisons = 0
    ANDNOTSet = set()
    ptr1 ,ptr2 = 0,0
    len1 = len(list1)
    len2 = len(list2)
    list1.sort()
    list2.sort()
    while ptr1 < len1 and ptr2 < len2:
        if list1[ptr1] < list2[ptr2]:
            comparisons += 1
            ANDNOTSet.add(list1[ptr1])
            ptr1 += 1
        elif list1[ptr1] > list2[ptr2]:
            comparisons += 1
            ptr2 += 1
        else:
            comparisons += 1
            ptr1 += 1
            ptr2 += 1

    ANDNOTSet = list(ANDNOTSet)
    return ANDNOTSet,comparisons

def OR_merge(list1, list2):
    comparisons = 0
    ORSet = set()
    list1.sort()
    list2.sort()
    ptr1 ,ptr2 = 0,0
    len1 = len(list1)
    len2 = len(list2)
    while ptr1 < len1 and ptr2 < len2:
        if list1[ptr1] == list2[ptr2]:
            comparisons += 1
            ORSet.add(list1[ptr1])
            ptr1 += 1
            ptr2 += 1
        else:
            comparisons += 2
            if list1[ptr1] < list2[ptr2]:
                ORSet.add(list1[ptr1])
                ptr1 += 1
            else:
                ORSet.add(list2[ptr2])
                ptr2 += 1

    while ptr1 < len1:
        ORSet.add(list1[ptr1])
        ptr1 += 1
    while ptr2 < len2:
        ORSet.add(list2[ptr2])
        ptr2 += 1
    ORSet = list(ORSet)
    return ORSet,comparisons

def ORNOT_merge(list1, list2):
    comparisons = 0
    ORNOTSet = set()
    list1.sort()
    list2.sort()
    ptr1 ,ptr2 = 0,0
    len1 = len(list1)
    len2 = len(list2)
    while ptr1 < len1 and ptr2 < len2:

        if list1[ptr1] == list2[ptr2]:
            comparisons += 1
            if ptr2 == 0:
                for i in range(0, list2[ptr2] + 1):
                    ORNOTSet.add(i)
            else:
                for i in range(list2[ptr2 - 1] + 1, list2[ptr2] + 1):
                    ORNOTSet.add(i)
            ORNOTSet.add(list1[ptr1])
            ptr1 += 1
            ptr2 += 1
        else:
            comparisons += 2
            if list1[ptr1] > list2[ptr2]:
                if ptr2 == 0:
                    for i in range(1, list2[ptr2]):
                        ORNOTSet.add(i)
                else:
                    for i in range(list2[ptr2 - 1] + 1, list2[ptr2]):
                        ORNOTSet.add(i)
                ptr2 += 1
            else:
                ptr1 += 1
    while ptr2 < len2:
        for i in range(list2[ptr2 - 1] + 1, list2[ptr2]):
            ORNOTSet.add(i)
        ptr2 += 1
    for i in range(list2[ptr2 - 1] + 1, 1400):
        ORNOTSet.add(i)
    
    ORNOTSet = list(ORNOTSet)
    return ORNOTSet,comparisons










