def muotoile_heksaluvuksi(luku, bitit):
    heksa = hex(luku)
    bitit = bitit//4
    m_heksa = heksa.replace("0x", "")
    m_heksa = m_heksa.zfill(bitit)
    return m_heksa
try:
    luku = int(input("Anna kokonaisluku:"))
    bitit = int(input("Anna heksaluvun pituus (bittien lukumäärä):"))
except ValueError:
    print("Kokonaisluku kiitos")
else:
    heksaluku = muotoile_heksaluvuksi(luku, bitit)
    print(heksaluku)