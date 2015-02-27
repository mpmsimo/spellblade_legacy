    def get_passive(self):
        print("passive: {0}".format(self.passive))
        return(self.passive)

    def set_passive(self, passive):
        new_passive = passive
        print(("setpassive\n"
                "Old: passive {0}\n"
                "New: new_passive {1}").format(self.passive, new_passive))
        return new_passive

    def get_active(self):
        print("active: {0}".format(self.active))
        return(self.active)

    def set_active(self, active):
        new_active = active
        print(("setactive\n"
                "Old: active {0}\n"
                "New: new_active {1}").format(self.active, new_active))
        return new_active