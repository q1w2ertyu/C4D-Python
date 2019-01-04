import c4d
c4d.CallCommand(13957, 13957) # 清空控制台
i=0


def mergeobj():
    c4d.CallCommand(12144, 12144) # 连接对象
    op = doc.GetActiveObject()
    return op

    
def DelOld():
    global i
    a = doc.SearchObject("combine"+str(i-1))
    a[c4d.ID_BASELIST_NAME]="combine"
    while i-2 >=0:
        a = doc.SearchObject("combine"+str(i-2))
        doc.SetSelection(a,c4d.SELECTION_NEW)
        c4d.CallCommand(100004787)
        i-=1

        
def SkinInitial(a,b,op):
    global i
    op[c4d.ID_BASELIST_NAME]="combine"+str(i)
    c4d.CallCommand(1019363, 1019363) # 蒙皮
    meng = doc.GetActiveObject()
    meng.InsertUnder(op)
    meng[c4d.ID_CA_SKIN_OBJECT_INCEXC]=0
    data = meng[c4d.ID_CA_SKIN_OBJECT_INCLUDE]
    data.InsertObject(op,1)
    meng[c4d.ID_CA_SKIN_OBJECT_INCLUDE]=data
    
    op.KillTag(c4d.Tweights,1)
    tagweight=op.GetTag(c4d.Tweights,0)
    first = op.GetFirstTag()
    op.InsertTag(tagweight,first)
    op.InsertTag(first,tagweight)
    tagweight[c4d.ID_CA_WEIGHT_TAG_TOTALWEIGHT] = 0
    c4d.CallButton(tagweight, c4d.ID_CA_WEIGHT_TAG_SET)
    tagweight[c4d.ID_CA_WEIGHT_TAG_TOTALWEIGHT] = 1
    c4d.EventAdd()

    
def mergeweight(a,b,op):
    taga= a.GetTag(c4d.Tweights,0)
    tagb= b.GetTag(c4d.Tweights,0)
    count = taga.GetJointCount()
    tagcom=op.GetTag(c4d.Tweights,0)
    bpointsnumber = b.GetPointCount()
    apointsnumber = a.GetPointCount()
    cpointsnumber = op.GetPointCount()
    lop=0
    while lop < count:
        jointadd = taga.GetJoint(lop)
        judge = tagcom.FindJoint(jointadd)
        if judge>=0:
            lopp=0
            while lopp < apointsnumber: 
                pweight = taga.GetWeight(lop, lopp)
                tagcom.SetWeight(judge,lopp,pweight)
                lopp+=1
            lop+=1
        else: 
            li = tagcom.AddJoint(jointadd)
            lopp=0
            while lopp < apointsnumber: 
                pweight = taga.GetWeight(lop, lopp)
                tagcom.SetWeight(li,lopp, pweight)
                lopp+=1
            lop+=1

            
if __name__=='__main__':
    sel = doc.GetSelection() #选择是以有序列表的形式存放元素。
    times = len(sel)
    a = sel[0]
    b = sel[1]
    doc.SetSelection(a,c4d.SELECTION_NEW)
    doc.SetSelection(b,c4d.SELECTION_ADD)
    op = mergeobj()
    SkinInitial(a,b,op)
    mergeweight(a,b,op)
    i=1
    while i+1<times:
        a = sel[i+1]
        b = op
        b.InsertAfter(a) #一定要注意：模型合并时，模型在层级中的前后顺序就是新模型的顶点的分布顺序。后面模型的权重标签，插入在之前模型权重标签前。
        doc.SetSelection(a,c4d.SELECTION_NEW)
        doc.SetSelection(b,c4d.SELECTION_ADD)
        op = mergeobj()
        SkinInitial(a,b,op)
        mergeweight(a,b,op)
        i+=1
    DelOld()
    a = doc.SearchObject("combine")
    a.SetBit(c4d.BIT_ACTIVE)
    a[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR]=2
    print("done")
