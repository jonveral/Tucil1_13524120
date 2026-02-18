class PapanQueens:
    def __init__(self, data_papan):
        self.papan = data_papan
        self.n = len(data_papan)
        self.total_iterasi = 0

    def cek_aman(self, baris_solusi):
        kolom_terpakai = [False] * self.n
        warna_terpakai = set()
        
        for r in range(self.n):
            c = baris_solusi[r]
            if kolom_terpakai[c]: return False
            kolom_terpakai[c] = True
            
            warna = self.papan[r][c]
            if warna in warna_terpakai: return False
            warna_terpakai.add(warna)
            
            for r_lama in range(r):
                c_lama = baris_solusi[r_lama]
                if abs(r_lama - r) <= 1 and abs(c_lama - c) <= 1:
                    return False
        return True

    def cari_exhaustive(self, baris, solusi_skrg, callback_visual):
        if baris == self.n:
            self.total_iterasi += 1
            if self.total_iterasi % 2000 == 0:
                callback_visual(solusi_skrg)
            return self.cek_aman(solusi_skrg)

        for col in range(self.n):
            solusi_skrg[baris] = col
            if self.cari_exhaustive(baris + 1, solusi_skrg, callback_visual):
                return True
        return False