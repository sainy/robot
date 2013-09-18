from command import mvCmd,rtCmd,Command
from math import sin,cos,pi,acos

class Joint:
    """this is the key point definition.
    
    """
    def __init__(self,name,init_pos,dw_joint=[]):
        self.name = name
        self.position = {"pos_x":0.0,"pos_y":0.0,"pos_z":0.0,"alpha":0.0,"beta":0.0,"gamma":0.0}
        self.command = None
        self.down_joint = dw_joint
        self.length = 0.0
        self.initial(init_pos)

    def initial(self,init_pos):
        if init_pos.has_key("x"):
            self.position["pos_x"] = init_pos["x"]
        if init_pos.has_key("y"):
            self.position["pos_y"] = init_pos["y"]
        if init_pos.has_key("z"):
            self.position["pos_z"] = init_pos["z"]
        if init_pos.has_key("alpha"):
            self.position["alpha"] = init_pos["alpha"]
        if init_pos.has_key("beta"):
            self.position["beta"] = init_pos["beta"]
        if init_pos.has_key("gamma"):
            self.position["gamma"] = init_pos["gamma"]
        if self.down_joint:
            for joint in self.down_joint:
                length = 0
                length += (self.position["pos_x"]-joint.position["pos_x"])**2
                length += (self.position["pos_y"]-joint.position["pos_y"])**2
                length += (self.position["pos_z"]-joint.position["pos_z"])**2
                length = length**0.5
                self.length += length
            self.length /= len(self.down_joint)
        self.calAngle()
    
    def calAngle(self):
        if self.down_joint:
            pos_x = 0.0
            pos_y = 0.0
            pos_z = 0.0
            length = len(self.down_joint)
            for joint in self.down_joint:
                pos_x += joint.position["pos_x"]
                pos_y += joint.position["pos_y"]
                pos_z += joint.position["pos_z"]
            pos_x /= length
            pos_y /= length
            pos_z /= length
            n_x = pos_x - self.position["pos_x"]
            n_y = pos_y - self.position["pos_y"]
            n_z = pos_z - self.position["pos_z"]
            ln = (n_x**2+n_y**2+n_z**2)**0.5
            ln_xy = (n_x**2+n_y**2)**0.5
            self.position["gamma"] = acos((-n_z)/ln)/pi * 180.0
            if ln_xy>0:
                self.position["alpha"] = acos(n_x/ln_xy)/pi * 180.0
                self.position["beta"] = acos(n_y/ln_xy)/pi * 180.0

    def setCmd(self,cmd):
        self.command = cmd

    def move(self,cmd):
        self.position["pos_x"] += cmd.move["mv_x"]
        self.position["pos_y"] += cmd.move["mv_y"]
        self.position["pos_z"] += cmd.move["mv_z"]
        if self.down_joint:
            for joint in self.down_joint:
                joint.move(cmd)

    def rotate(self,cmd):
        diff_gamma = self.position["gamma"]+cmd.rotate["gamma"]
        diff_alpha = self.position["alpha"]+cmd.rotate["alpha"]
        diff_beta = self.position["beta"]+cmd.rotate["beta"]
        if self.down_joint:
            ln = self.length
            Dz = ln*cos(self.position["gamma"]/180.0*pi)-ln*cos(diff_gamma/180.0*pi)
            Dx = ln*sin(diff_gamma/180.0*pi)*cos(diff_alpha/180.0*pi)-ln*sin(self.position["gamma"]/180.0*pi)*cos(self.position["alpha"]/180.0*pi)
            Dy = ln*sin(diff_gamma/180.0*pi)*cos(diff_beta/180.0*pi)-ln*sin(self.position["gamma"]/180.0*pi)*cos(self.position["beta"]/180.0*pi)
            mvcmd = mvCmd()
            mvcmd.setCommand({"mv_x":Dx,"mv_y":Dy,"mv_z":Dz})
            for joint in self.down_joint:
                joint.move(mvcmd)
                joint.rotate(cmd)
        self.position["alpha"] = diff_alpha
        self.position["beta"] = diff_beta
        self.position["gamma"] = diff_gamma

    def doAction(self):
        if isinstance(self.command,mvCmd):
            self.move(self.command)
        elif isinstance(self.command,rtCmd):
            self.rotate(self.command)
        elif isinstance(self.command,Command):
            self.move(self.command.mv)
            self.rotate(self.command.rt)

    def run(self):
        self.doAction()

    def printInfo(self):
        if self.down_joint:
            print("JointName:%s,  Next:%s,  ControlLength:%.2f" %(self.name,self.down_joint[0].name,self.length))
        else:
            print("JointName:%s,  Next:None, COntrolLength:0.0 "%self.name)
        print("Position:(%.2f,%.2f,%.2f,%.2f,%.2f,%.2f)\n"%(self.position["pos_x"],self.position["pos_y"],self.position["pos_z"],self.position["alpha"],self.position["beta"],self.position["gamma"]))
        if self.down_joint:
            for joint in self.down_joint:
                joint.printInfo()

if __name__=="__main__":
    #palm = Joint("palm",init_pos = {"x":0.0,"y":0.0,"z":70.0,"alpha":0.0,"beta":0.0,"gamma":0.0})
    palm = Joint("palm",init_pos = {"z":70.0})
    elbow = Joint("elbow",init_pos = {"x":0.0,"y":0.0,"z":90.0,"alpha":0.0,"beta":0.0,"gamma":0.0},dw_joint=[palm])
    hand = Joint("hand",init_pos ={"x":-20.0,"y":0.0,"z":110.0,"alpha":0.0,"beta":0.0,"gamma":45.0},dw_joint = [elbow])
    #cmd = Command()
    #cmd.mv.setCommand({"mv_x":-12.2,"mv_y":0.3,"mv_z":0.4})
    #cmd.rt.setCommand({"alpha":0.0,"beta":0.0,"gamma":45.0})
    #hand.setCmd(cmd)
    #hand.run()
    #hand.printInfo()









