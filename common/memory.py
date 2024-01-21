class Memory:
    def __init__(self):
        self.vol = 30000
        self.memory = [0]*self.vol;
        self.ptr = 0

    def __repr__(self):
        return str(self.memory)
    
