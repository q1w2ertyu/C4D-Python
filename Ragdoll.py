# -*- coding:utf-8 -*- 
import c4d
c4d.CallCommand(13957, 13957) # 清空控制台
c4d.CallCommand(5104) # 地面
c4d.CallCommand(12096, 12096) # 合并...
floor = doc.SearchObject("地面")
floor.SetBit(c4d.BIT_ACTIVE)
floor[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = -9
c4d.CallCommand(180000043, 180000043) # #$7 碰撞体
fric = floor.GetFirstTag() 
fric[c4d.RIGID_BODY_FRICTION]= 2
c4d.EventAdd()

bonelist =["spine lower","spine upper","head neck upper","root hips",
"leg right knee","leg right ankle","leg right thigh",
"leg left knee","leg left ankle","leg left thigh",
"arm left shoulder 2","arm left elbow","arm left wrist",
"arm right shoulder 2","arm right elbow","arm right wrist"]


def insertbyname(son,parent):
    obj = doc.SearchObject(son)
    m = obj.GetMg()
    obj1 = doc.SearchObject(parent)
    obj.InsertUnder(obj1)
    obj.SetMg(m)

def insert(obj,obj1):
    m = obj.GetMg()
    obj.InsertUnder(obj1)
    obj.SetMg(m)
    
def main():
    ctrlist=[]
    
    for thing in bonelist:
        c4d.CallCommand(5140, 5140) # 建造空白对象，且其位置在骨骼处 
        obj = doc.SearchObject("空白")
        obj[c4d.ID_BASELIST_NAME]= thing+" aux"
        obj1 = doc.SearchObject(thing)
        m = obj1.GetMg()
        obj.SetMg(m)
        objneedinsert =doc.SearchObject(thing+" col") #将模拟碰撞体插入空白对象
        insert(objneedinsert,obj)
        insert(obj1,objneedinsert) #将骨骼插入模拟碰撞体
        c4d.EventAdd()
    
    insertbyname("arm right elbow aux","arm right shoulder 2 aux")
    insertbyname("arm right wrist aux","arm right elbow aux")
    insertbyname("leg right ankle aux","leg right knee aux")
    insertbyname("leg right knee aux","leg right thigh aux")
    insertbyname("arm left elbow aux","arm left shoulder 2 aux")
    insertbyname("arm left wrist aux","arm left elbow aux")
    insertbyname("leg left ankle aux","leg left knee aux")
    insertbyname("leg left knee aux","leg left thigh aux")
    insertbyname("leg right thigh aux","root hips aux")
    insertbyname("leg left thigh aux","root hips aux")
    insertbyname("spine lower aux","root hips aux")
    insertbyname("spine upper aux","spine lower aux")
    insertbyname("head neck upper aux","spine upper aux")
    insertbyname("arm left shoulder 2 aux","spine upper aux")
    insertbyname("arm right shoulder 2 aux","spine upper aux")
    
    
    
    for thing in bonelist:
        obj = doc.SearchObject(thing)
        c4d.CallCommand(180000011) # 建造连结器，重命名
        ctr = doc.SearchObject("连结器")
        name = "ctr "+thing
        print("{} has been made!".format(thing)) 
        
        m = ctr.GetMg()#将CTR连接器放到辅助对象，作为子节点
        ctr.InsertUnder(doc.SearchObject(thing+" aux"))
        ctr.SetMg(m)
        
        ctr[c4d.ID_BASELIST_NAME] = name #将连接器名字放入列表
        ctr[c4d.FORCE_SIZE] = 5
        ctr[c4d.FORCE_ALWAYS_VISIBLE] = False
        ctr[c4d.ID_BASEOBJECT_GLOBAL_POSITION] = obj[c4d.ID_BASEOBJECT_GLOBAL_POSITION]
        c4d.CallCommand(100004758, 30000)
        ctrlist.append(name)
        
    for thing in ctrlist:
        object = doc.SearchObject(thing)
        
        if object[c4d.ID_BASELIST_NAME]=="ctr spine lower":
            object[c4d.FORCE_TYPE]= 3
            
            obja=doc.SearchObject("spine lower col")
            objb=doc.SearchObject("root hips col")
            
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
            
            object[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = -1.496
    
            object[c4d.CONSTRAINT_CONE_LIMIT_RADIUS] = 0.349
            object[c4d.CONSTRAINT_ROT1_LIMIT] = True
            object[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = -0.262
            object[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 0.262

        if object[c4d.ID_BASELIST_NAME]=="ctr spine upper":
            object[c4d.FORCE_TYPE]= 3
            
            obja=doc.SearchObject("spine upper col")
            objb=doc.SearchObject("spine lower col")
            
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
            
            object[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = -1.555
    
            object[c4d.CONSTRAINT_CONE_LIMIT_RADIUS] = 0.349
            object[c4d.CONSTRAINT_ROT1_LIMIT] = True
            object[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = -0.524
            object[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 0.524            
        
            
        if object[c4d.ID_BASELIST_NAME]=="ctr head neck upper":
            object[c4d.FORCE_TYPE]= 3
            
            obja=doc.SearchObject("head neck upper col")
            objb=doc.SearchObject("spine upper col")
            
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
            
            object[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = -1.571
    
            object[c4d.CONSTRAINT_CONE_LIMIT_RADIUS] = 0.262
            object[c4d.CONSTRAINT_ROT1_LIMIT] = True
            object[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = -0.524
            object[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 0.524    
            
        if object[c4d.ID_BASELIST_NAME]=="ctr leg left thigh":
        
            object[c4d.FORCE_TYPE]= 3
            obja=doc.SearchObject("leg left thigh col")
            objb=doc.SearchObject("root hips col")
            
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
                    
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] = 1.571
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = 0.349
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = 1.571
    
            object[c4d.CONSTRAINT_ROT1_LIMIT] = True

            object()[c4d.CONSTRAINT_CONE_LIMIT_RADIUS] = 0.524
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = 2.356
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 3.752
            
            
        if object[c4d.ID_BASELIST_NAME]=="ctr leg right thigh":
            object[c4d.FORCE_TYPE]= 3
            
            obja=doc.SearchObject("leg right thigh col")
            objb=doc.SearchObject("root hips col")
            
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
            
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] = -1.571
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = 0.349
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = -1.571
    
            object[c4d.CONSTRAINT_ROT1_LIMIT] = True

            object()[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 4.276
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = -3.316
            object()[c4d.CONSTRAINT_CONE_LIMIT_RADIUS] = 0.524
            
        if object[c4d.ID_BASELIST_NAME]=="ctr arm right wrist":
         
            object[c4d.FORCE_TYPE]= 3
         
            obja=doc.SearchObject("arm right wrist col")
            objb=doc.SearchObject("arm right elbow col")
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
          
            object[c4d.CONSTRAINT_ROT1_LIMIT] = True
            object()[c4d.CONSTRAINT_CONE_LIMIT_RADIUS] = 0.524
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = -1.396
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = 0.698
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] = -0.524
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = 3.7
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 5.027
            
        if object[c4d.ID_BASELIST_NAME]=="ctr arm left wrist":
            object[c4d.FORCE_TYPE]= 3
            obja=doc.SearchObject("arm left wrist col")
            objb=doc.SearchObject("arm left elbow col")
            
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
    
            object[c4d.CONSTRAINT_ROT1_LIMIT] = True

            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = 1.396
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = 0.698
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] = -0.524
            object()[c4d.CONSTRAINT_CONE_LIMIT_RADIUS] = 0.524
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = 0.349
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 1.222
        if object[c4d.ID_BASELIST_NAME]=="ctr arm right shoulder 2":
            object[c4d.FORCE_TYPE]= 3
            
            obja=doc.SearchObject("arm right shoulder 2 col")
            objb=doc.SearchObject("spine upper col")
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
            
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] = 0
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = -0.262
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = -1.571
    
            object[c4d.CONSTRAINT_ROT1_LIMIT] = True

            object()[c4d.CONSTRAINT_CONE_LIMIT_RADIUS] = 1.047
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 2.443
            
        if object[c4d.ID_BASELIST_NAME]=="ctr arm left shoulder 2":
            object[c4d.FORCE_TYPE]= 3
            
            obja=doc.SearchObject("arm left shoulder 2 col")
            objb=doc.SearchObject("spine upper col")
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
            
            object[c4d.CONSTRAINT_ROT1_LIMIT] = True
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = 1.571
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = -0.262
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] = 0
            object()[c4d.CONSTRAINT_CONE_LIMIT_RADIUS] = 1.047
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = 3.386
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = -0.698
    

            
        if object[c4d.ID_BASELIST_NAME]=="ctr arm right elbow":
            obja=doc.SearchObject("arm right elbow col")
            objb=doc.SearchObject("arm right shoulder 2 col")
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
            object[c4d.FORCE_TYPE]= 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT] = True
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = -1.571
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = -0.785
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] = 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 2.269
            
        if object[c4d.ID_BASELIST_NAME]=="ctr arm left elbow":
            obja=doc.SearchObject("arm left elbow col")
            objb=doc.SearchObject("arm left shoulder 2 col")
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
            object[c4d.FORCE_TYPE]= 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT] = True
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = 1.571
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = -0.785
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] = 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = -2.269
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 6.37
            
            
            
        if object[c4d.ID_BASELIST_NAME]=="ctr leg right knee":
            obja=doc.SearchObject("leg right knee col")
            objb=doc.SearchObject("leg right thigh col")
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
            object[c4d.FORCE_TYPE]= 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT] = True
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = -1.571
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = -0.314
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] = 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = -2.618
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 0
            
        if object[c4d.ID_BASELIST_NAME]=="ctr leg left knee":
            obja=doc.SearchObject("leg left knee col")
            objb=doc.SearchObject("leg left thigh col")
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
            object[c4d.FORCE_TYPE]= 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT] = True
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = 1.571
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = -0.314
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] = 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 2.618
            
        if object[c4d.ID_BASELIST_NAME]=="ctr leg right ankle":
            obja=doc.SearchObject("leg right ankle col")
            objb=doc.SearchObject("leg right knee col")
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
            object[c4d.FORCE_TYPE]= 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT] = True
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = -1.553
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = -0.332
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] = -0.017
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = -0.646
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 1.449
            
        if object[c4d.ID_BASELIST_NAME]=="ctr leg left ankle":
            obja=doc.SearchObject("leg left ankle col")
            objb=doc.SearchObject("leg left knee col")
            object()[c4d.FORCE_OBJECT_A]=obja
            object()[c4d.FORCE_OBJECT_B]=objb
            object[c4d.FORCE_TYPE]= 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT] = True
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = 1.571
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = -0.349
            object()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] = 0
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MIN] = -1.309
            object()[c4d.CONSTRAINT_ROT1_LIMIT_MAX] = 0.785
            


        
if __name__=='__main__':
    main()
   
