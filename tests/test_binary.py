"""
Unit tests for zeckendorf.binary.
"""
from zeckendorf import binary


def test():
    for (nega,  n,   zeck,         binint,      bitstr,      codeword) in (
        (False, 0,   [],           0b0,         '0',         None),
        (False, 1,   [1],          0b1,         '1',         '11'),
        (False, 5,   [5],          0b1000,      '1000',      '00011'),
        (False, 12,  [8, 3, 1],    0b10101,     '10101',     '101011'),
        (True,  0,   [],           0b0,         '0',         None),
        (True,  1,   [1],          0b1,         '1',         '11'),
        (True,  -1,  [-1],         0b10,        '10',        '011'),
        (True,  -8,  [-8],         0b100000,    '100000',    '0000011'),
        (True,  -17, [-21, 5, -1], 0b10010010,  '10010010',  '010010011'),
        (True,  44,  [34, 13, -3], 0b101001000, '101001000', '0001001011'),
    ):
        # zeck to binary
        assert binary.fromzeck(zeck, nega=nega) == binint
        assert binary.str_fromzeck(zeck, nega=nega) == bitstr
        assert binary.fromint(n, nega=nega) == binint
        assert binary.str_fromint(n, nega=nega) == bitstr

        # binary to zeck
        assert list(binary.tozeck(binint, nega=nega)) == zeck
        assert list(binary.str_tozeck(bitstr, nega=nega)) == zeck
        assert binary.toint(binint, nega=nega) == n
        assert binary.str_toint(bitstr, nega=nega) == n

        if codeword:

            # zeck to codeword
            assert binary.fibcode_fromzeck(zeck, nega=nega) == codeword
            assert binary.fibcode_fromint(n, nega=nega) == codeword

            # codeword to zeck
            assert list(binary.fibcode_tozeck(codeword, nega=nega)) == zeck
            assert binary.fibcode_toint(codeword, nega=nega) == n


if __name__ == '__main__':
    test()
