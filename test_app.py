from app import tambah

def test_tambah_positif():
    assert tambah(2, 3) == 5

def test_tambah_negatif():
    assert tambah(-2, -3) == -5

