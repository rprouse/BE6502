# Func: make a 32K rom.bin filled with 0xea (NOP)
rom = bytearray([0xea] * 32768)

# 0x7ffc - 0x7fff is the reset vector
rom[0x7ffc] = 0x00
rom[0x7ffd] = 0x80
rom[0x7ffe] = 0x00
rom[0x7fff] = 0x00

with open('rom.bin', 'wb') as f:
    f.write(rom)