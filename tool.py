from mt19937predictor import MT19937Predictor
from encryption import XOR

predictor = MT19937Predictor()

with open("flag.jpg.partial", "rb") as file_partial, open("flag.jpg.enc", "rb") as file_encrypt, open("flag.jpg",
                                                                                                "wb") as file:
    while True:
        # Get XOR nums
        partial = file_partial.read(4)

        if len(partial) < 4:
            break
        encrypt = file_encrypt.read(4)
        number = int(XOR(encrypt, partial).encode("hex"), 16)
        predictor.setrandbits(number, 32)
        file.write(partial)

    while True:
        # XOR the cypher and the predictor
        encrypt = file_encrypt.read(4)
        if encrypt == "":
            break
        predictor_number = predictor.getrandbits(32)
        s = hex(predictor_number)[2:].replace('L', '').zfill(8).decode("hex")
        file.write(XOR(s, encrypt))

print("done")