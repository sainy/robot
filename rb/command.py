class mvCmd:
    """this command refects the key point's move action.
    
    the move action can be modeled in x,y,z direction"""
    def __init__(self):
        self.move = {"mv_x":0.0,"mv_y":0.0,"mv_z":0.0}

    def setCommand(self,mv_params):
        if mv_params.has_key("mv_x"):
            self.move["mv_x"] = mv_params["mv_x"]
        if mv_params.has_key("mv_y"):
            self.move["mv_y"] = mv_params["mv_y"]
        if mv_params.has_key("mv_z"):
            self.move["mv_z"] = mv_params["mv_z"]

class rtCmd:
    """this command refects the key point's rotate action.
    
    the rotate action can be modeled by calculating the angel in x,y,z direction.
    rotation does not change this point's pos, but it changes the pos of its controllers"""
    def __init__(self):
        self.rotate = {"alpha":0.0,"beta":0.0,"gamma":0.0,"pos":0.0}

    def setCommand(self,rt_params):
        if rt_params.has_key("alpha"):
            self.rotate["alpha"] = rt_params["alpha"]
        if rt_params.has_key("beta"):
            self.rotate["beta"] = rt_params["beta"]
        if rt_params.has_key("gamma"):
            self.rotate["gamma"] = rt_params["gamma"]
        if rt_params.has_key("pos"):
            self.rotate["pos"] = rt_params["pos"]

class Command:
    """this is the command that refects the actions that key point can do.
    
    it contained a mvCmd and a rtCmd instance."""
    def __init__(self):
        self.mv = mvCmd()
        self.rt = rtCmd()

    def printInfo(self):
        print self.mv.move
        print self.rt.rotate

if __name__=="__main__":
    cmd = Command()
    cmd.rt.setCommand({"alpha":45.0,"beta":0.0,"gamma":15.0})
    cmd.printInfo()




