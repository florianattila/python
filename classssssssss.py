class Fogyatékosság:
    def __init__(self, idiotasag, tanulmanyi_atlag,talalekonysag, nem, kopaszsag= False):
        self.idiotasag = idiotasag
        self.tanulmanyi_atlag = tanulmanyi_atlag
        self.talalekonysag = talalekonysag
        self.nem = nem
        self.kopaszsag = kopaszsag
        

Józsi = Fogyatékosság(10, 5, 10, "ferfi", True)
print(Józsi.kopaszsag)