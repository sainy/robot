from joint import Joint
from register import Register

Store = Register()

class LeftHand:
    l_lit_fg_top = Joint("left little finger top",init_pos={"x":-15.0,"y":-4.0,"z":68.0})
    l_rin_fg_top = Joint("left ring finger top",init_pos={"x":-15.0,"y":-2.0,"z":66.0})
    l_mid_fg_top = Joint("left middle finger top",init_pos={"x":-15.0,"y":0.0,"z":65.0})
    l_for_fg_top = Joint("left fore finger top",init_pos={"x":-15.0,"y":2.0,"z":67.0})
    l_thrumb_top = Joint("left thrumb top",init_pos={"x":-15.0,"y":5.0,"z":73.0})
    l_lit_fg_ctrl = Joint("left little finger controller",init_pos={"x":-15.0,"y":-4.0,"z":74.0},dw_joint =[l_lit_fg_top])
    l_rin_fg_ctrl = Joint("left ring finger controller",init_pos={"x":-15.0,"y":-2.0,"z":74.0},dw_joint=[l_rin_fg_top])
    l_mid_fg_ctrl = Joint("left middle finger controller",init_pos={"x":-15.0,"y":0.0,"z":74.0},dw_joint=[l_mid_fg_top])
    l_for_fg_ctrl = Joint("left fore finger controller",init_pos={"x":-15.0,"y":2.0,"z":74.0},dw_joint=[l_for_fg_top])
    l_thrumb_ctrl = Joint("left thrumb controller",init_pos={"x":-15.0,"y":5.0,"z":76.0},dw_joint=[l_thrumb_top])
    l_palm = Joint("left plam",init_pos={"x":-15.0,"y":0.0,"z":80.0},dw_joint = [l_lit_fg_ctrl,l_rin_fg_ctrl,l_mid_fg_ctrl,l_for_fg_ctrl,l_thrumb_ctrl])
    l_elbow = Joint("left elbow",init_pos={"x":-15.0,"y":0.0,"z":105.0},dw_joint = [l_palm])
    l_hand = Joint("left hand",init_pos={"x":-15.0,"y":0.0,"z":133.0},dw_joint = [l_elbow])
    
    def __init__(self):
        lh = {"name":"leftHand"}
        lh["controller"] = [self.l_hand,self.l_elbow,self.l_palm,self.l_thrumb_ctrl,self.l_for_fg_ctrl,self.l_mid_fg_ctrl,self.l_rin_fg_ctrl,self.l_lit_fg_ctrl,self.l_thrumb_top,self.l_for_fg_top,self.l_mid_fg_top,self.l_rin_fg_top,self.l_lit_fg_top]
        Store.register(lh)

    def printInfo(self):
        self.l_hand.printInfo()
        self.l_elbow.printInfo()
        self.l_palm.printInfo()

class RightHand:
    r_lit_fg_top = Joint("rigth little finger top",init_pos={"x":15.0,"y":-4.0,"z":68.0})
    r_rin_fg_top = Joint("right ring finger top",init_pos={"x":15.0,"y":-2.0,"z":66.0})
    r_mid_fg_top = Joint("right middle finger top",init_pos={"x":15.0,"y":0.0,"z":65.0})
    r_for_fg_top = Joint("right fore finger top",init_pos={"x":15.0,"y":2.0,"z":67.0})
    r_thrumb_top = Joint("right thrumb top",init_pos={"x":15.0,"y":5.0,"z":73.0})
    r_lit_fg_ctrl = Joint("right little finger controller",init_pos={"x":15.0,"y":-4.0,"z":74.0},dw_joint =[r_lit_fg_top])
    r_rin_fg_ctrl = Joint("rigth ring finger controller",init_pos={"x":15.0,"y":-2.0,"z":74.0},dw_joint=[r_rin_fg_top])
    r_mid_fg_ctrl = Joint("right middle finger controller",init_pos={"x":15.0,"y":0.0,"z":74.0},dw_joint=[r_mid_fg_top])
    r_for_fg_ctrl = Joint("right fore finger controller",init_pos={"x":15.0,"y":2.0,"z":74.0},dw_joint=[r_for_fg_top])
    r_thrumb_ctrl = Joint("right thrumb controller",init_pos={"x":15.0,"y":5.0,"z":76.0},dw_joint=[r_thrumb_top])
    r_palm = Joint("right plam",init_pos={"x":15.0,"y":0.0,"z":80.0},dw_joint = [r_lit_fg_ctrl,r_rin_fg_ctrl,r_mid_fg_ctrl,r_for_fg_ctrl,r_thrumb_ctrl])
    r_elbow = Joint("right elbow",init_pos={"x":15.0,"y":0.0,"z":105.0},dw_joint = [r_palm])
    r_hand = Joint("right hand",init_pos={"x":15.0,"y":0.0,"z":133.0},dw_joint = [r_elbow])

    def __init__(self):
        rh = {"name":"leftHand"}
        rh["controller"] = [self.r_hand,self.r_elbow,self.r_palm,self.r_thrumb_ctrl,self.r_for_fg_ctrl,self.r_mid_fg_ctrl,self.r_rin_fg_ctrl,self.r_lit_fg_ctrl,self.r_thrumb_top,self.r_for_fg_top,self.r_mid_fg_top,self.r_rin_fg_top,self.r_lit_fg_top]
        Store.register(rh)

    def printInfo(self):
        self.r_hand.printInfo()
        self.r_elbow.printInfo()
        self.r_palm.printInfo()

class LeftLeg:
    l_toe = Joint("left toe",init_pos={"x":-9,"y":10,"z":0})
    l_sole = Joint("left sole",init_pos={"x":-6,"y":5,"z":0},dw_joint=[l_toe])
    l_ankle = Joint("left ankle",init_pos={"x":-3,"y":-1,"z":0},dw_joint=[l_sole])
    l_knee = Joint("left knee",init_pos={"x":-4,"y":0,"z":40},dw_joint=[l_ankle])
    l_thigh = Joint("left thigh",init_pos={"x":-3,"y":0,"z":95},dw_joint=[l_knee])

    def __init__(self):
        ll = {"name":"LeftLeg"}
        ll["controller"] = [self.l_toe,self.l_sole,self.l_ankle,self.l_knee,self.l_thigh]
        Store.register(ll)

    def printInfo(self):
        self.l_toe.printInfo()
        self.l_sole.printInfo()
        self.l_ankle.printInfo()
        self.l_knee.printInfo()
        self.l_thigh.printInfo()

class RightLeg:
    r_toe = Joint("right toe",init_pos={"x":9,"y":10,"z":0})
    r_sole = Joint("right sole",init_pos={"x":6,"y":5,"z":0},dw_joint=[r_toe])
    r_ankle = Joint("right ankle",init_pos={"x":3,"y":-1,"z":0},dw_joint=[r_sole])
    r_knee = Joint("right knee",init_pos={"x":4,"y":0,"z":40},dw_joint=[r_ankle])
    r_thigh = Joint("right thigh",init_pos={"x":3,"y":0,"z":95},dw_joint=[r_knee])

    def __init__(self):
        rl = {"name":"RightLeg"}
        rl["controller"] = [self.r_toe,self.r_sole,self.r_ankle,self.r_knee,self.r_thigh]
        Store.register(rl)

    def printInfo(self):
        self.r_toe.printInfo()
        self.r_sole.printInfo()
        self.r_ankle.printInfo()
        self.r_knee.printInfo()
        self.r_thigh.printInfo()

class Body:
    """this class is used to initial the whole body.

    each key point in the body is definited at this place."""
    Left_hand = LeftHand()
    Right_hand = RightHand()
    Left_leg = LeftLeg()
    Right_leg = RightLeg()
    head = Joint("The head top",init_pos={"x":0,"y":0,"z":175})
    neck = Joint("body's neck",init_pos={"x":0,"y":0,"z":150},dw_joint=[Left_hand.l_hand,Right_hand.r_hand,head])
    back = Joint("the back of body",init_pos={"x":0,"y":0,"z":125},dw_joint=[neck])
    waist = Joint("the waist of body",init_pos={"x":0,"y":0,"z":110},dw_joint=[back,Left_leg.l_thigh,Right_leg.r_thigh])

    def __init__(self):
        body = {"name":"The whole body"}
        body["controller"] = [self.head,self.neck,self.back,self.waist]
        Store.register(body)

    def printInfo(self):
        self.head.printInfo()
        self.neck.printInfo()
        self.back.printInfo()
        self.waist.printInfo()

if __name__=="__main__":
    #lefthand = LeftHand()
    #lefthand.printInfo()
    body = Body()
    #body.printInfo()
    #print Store.key_points
