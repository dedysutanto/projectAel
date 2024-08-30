class Gelas:
    def __init__(self, warna_input: str, ukuran_input: int):
        self.warna = warna_input
        self.ukuran = ukuran_input

    def __str__(self):
        return "Warna:" + self.warna + " dengan ukuran " + str(self.ukuran)

class Piring:
    def __init__(self, warna_input: str, bahan_input: str, apakah_bulat: bool):
        self.warna = warna_input
        self.bahan = bahan_input
        self.is_bulat = apakah_bulat

    def __str__(self):
        if self.is_bulat:
            bentuk = "bulat"
        else:
            bentuk = "tidak bulat"

        return "Piring " + self.bahan + " warnanya " + self.warna + " bentuknya " + bentuk


gelas1 = Gelas("Merah", 10)
piring1 = Piring("Putih", "kaca", True)

#print(gelas1)
print(piring1)
