import numpy
import csv
import cv2

#---------------- convertors -----------------------#

# convert hex -> des
def hex2des(hex):
    dec = int(hex, 16)
    return dec

# convert hex -> bin
def hex2bin(n):
    n = hex2des(n)
    n = dec2bin(n)
    return n

# convert dec -> hex
def dec2hex(dec):
    return hex(dec)

# convert bin -> dec
def bin2dec(bin):
    bin = str(bin)
    return int(bin, 2)

# convert dec -> bin
def dec2bin(n):
    return bin(n).replace("0b", "")

# convert bin -> hex
def bin2hex(n):
    n = bin2dec(n)
    n = dec2hex(n)
    return n




#--------------------- prossesor ---------------------#


def _adddollar(n):
    n = f"${n}"
    return n

"""
mux function
"""
def mux(in0, in1, c):
    if c == 0:
        return in0
    if c == 1:
        return in1
    if c == "x":
        return "x"

"""
and function
"""
def _and(n1, n2):
    return (n1 and n2)

"""
or function
"""
def _or(n1, n2):
    return (n1 or n2)

"""
xor function
"""
def _xor(n1, n2):
    return (n1 ^ n2)

"""
slt function
"""
def _slt(n1, n2):
    return (n1 < n2)



def sing_extend(n, _len=32):
    l = len(n)
    w = str(n)[0]
    g = ""
    for i in range(0, _len - l, 1):
        g = g + w
    g = str(g)
    n = str(n)
    m = g + n
    return m



"""
return bin number starts at from_ and end at to_
"""
def branch_address(addr, target):
    n = hex2des(addr)
    n = n + 4
    m = hex2des(target)
    t = n + (m * 4)
    t = dec2hex(t)
    return t


"""
return bin number starts at from_ and end at to_
"""
def crop_bits(bin, from_, to_):
    bin = str(bin)
    from_ = len(bin) - from_
    to_ = len(bin) - to_
    croped = ""
    for i in range(to_ - 1, from_):
        croped = croped + bin[i]
    return croped




def opcode2instruction(opcode):
    l = []
    with open('opcode.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        for line in data:
            if line[0] == opcode:
                l.append(line)
        return l



def _bincomplatezero(n,lent):
    n = str(n)
    l = lent - len(n)
    for i in range(0, l, 1):
        n = "0" + str(n)
    return n

class Instruction():
    def __init__(self, instr):
        self.str_instr = instr

        jj = self.str_instr.replace(',',' ')

        instr1 = jj.split(" ")
        print(instr1)
        instr_name = instr1[0]
        split_instr = instr.split(", ")
        print(instr1)

        # instr_name = self.split_instr[0]
        # instr_name = instr_name.strip('$')
        # self.instr_name = instr_name



        with open('cc.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            for line in data:
                if line[0].strip('\t').lower() == instr_name.lower():
                    self.formt = line[3].strip('\t')
                    self.opcode = line[1].strip('\t')
                    self.instr_name = line[0].strip('\t')
                    self.func = line[2].strip('\t')
                    f = line[4]
                    f = f.split(" ")
                    # self.rd = instr1[f.index("rt")+1]
        f = f.index("rt")
        print(f)

        if self.formt == "R":

            rs = instr1[f].strip(',')
            rs = rs.strip('$')
            print(rs)
            rt = instr1[1].strip(',')
            self.rs = int(rs)
            self.instr_21_25 = _bincomplatezero(dec2bin(self.rs),6)
            self.instr_16_20 = _bincomplatezero(dec2bin(self.rt),5)

        print(self.instr_21_25)


        #self.instr_26_31 = crop_bits(hex2bin(code), 26, 31)

        # self.instr_16_20 = crop_bits(hex2bin(code), 16, 20)
        # self.instr_11_15 = crop_bits(hex2bin(code), 11, 15)
        # self.instr_0_15 = crop_bits(hex2bin(code), 0, 15)
        # self.instr_0_5 = crop_bits(hex2bin(code), 0, 5)


class Registers:
    def __init__(self,code,frmt,adrs = "0x0400004"):


        self.registers = numpy.array([
            [0, "$zero", 0, dec2hex(0)],
            [0, "$at", 1, dec2hex(1)],
            [0, "$v0", 2, dec2hex(2)],
            [0, "$v1", 3, dec2hex(3)],
            [0,"$a0",4,dec2hex(4)],
            [0,"$a1",5,dec2hex(5)],
            [0,"$a2",6,dec2hex(6)],
            [0,"$a3",7,dec2hex(7)],
            [0,"$t0",8,dec2hex(8)],
            [0,"$t1",9,dec2hex(9)],
            [0,"$t2",10,dec2hex(10)],
            [0,"$t3",11,dec2hex(11)],
            [0,"$t4",12,dec2hex(12)],
            [0,"$t5",13,dec2hex(13)],
            [0,"$t6",14,dec2hex(14)],
            [0,"$t7",15,dec2hex(15)],
            [350,"$s0",16,dec2hex(16)],
            [0,"$s1",17,dec2hex(17)],
            [0,"$s2",18,dec2hex(18)],
            [0,"$s3",19,dec2hex(19)],
            [0,"$s4",20,dec2hex(20)],
            [0,"$s5",21,dec2hex(21)],
            [0,"$s6",22,dec2hex(22)],
            [0,"$s7",23,dec2hex(23)],
            [0,"$t8",24,dec2hex(24)],
            [0,"$t9",25,dec2hex(25)],
            [0,"$k0",26,dec2hex(26)],
            [0,"$k1",27,dec2hex(27)],
            [0,"$gp",28,dec2hex(28)],
            [0,"$sp",29,dec2hex(29)],
            [0,"$fp",30,dec2hex(30)],
            [0,"$zra",31,dec2hex(31)]
        ])


        self.code = code
        self.adrs = adrs
        self.adrs_after_add4 = dec2hex(hex2des(adrs) +4)
        self.instr_26_31 = crop_bits(hex2bin(code), 26, 31)
        self.instr_21_25 = crop_bits(hex2bin(code), 21, 25)
        self.instr_16_20 = crop_bits(hex2bin(code), 16, 20)
        self.instr_11_15 = crop_bits(hex2bin(code), 11, 15)
        self.instr_0_15 = crop_bits(hex2bin(code), 0, 15)
        self.instr_0_5 = crop_bits(hex2bin(code), 0, 5)

        self.rs = crop_bits(hex2bin(code), 21, 25)
        self.rs = _adddollar(bin2dec(self.rs))
        self.rt = crop_bits(hex2bin(code), 16, 20)
        self.rt = _adddollar(bin2dec(self.rt))
        self.rd = crop_bits(hex2bin(code), 11, 15)
        self.rd = _adddollar(bin2dec(self.rd))

        self.sing_extend = sing_extend(self.instr_0_15)

        self.regdst = ""
        self.alusrc = ""
        self.memtoreg = ""
        self.regwrite = ""
        self.memread = ""
        self.memwrite = ""
        self.branch = ""
        self.aluop1 = ""
        self.aluop0 = ""

        if frmt == "r":
            self.regdst = "1"
            self.alusrc = "0"
            self. memtoreg = "0"
            self.regwrite = "1"
            self.memread = "0"
            self.memwrite = "0"
            self.branch = "0"
            self.aluop1 = "1"
            self.aluop0 = "0"

        if frmt == "lw":
            self.regdst = "0"
            self.alusrc = "1"
            self.memtoreg = "1"
            self.regwrite = "1"
            self.memread = "1"
            self.memwrite = "0"
            self.branch = "0"
            self.aluop1 = "0"
            self.aluop0 = "0"

        if frmt == "sw":
            self.regdst = "x"
            self.alusrc = "1"
            self.memtoreg = "x"
            self.regwrite = "0"
            self.memread = "0"
            self.memwrite = "1"
            self.branch = "0"
            self.aluop1 = "0"
            self.aluop0 = "0"

        if frmt == "beq":
            self.regdst = "x"
            self.alusrc = "0"
            self.memtoreg = "x"
            self.regwrite = "0"
            self.memread = "0"
            self.memwrite = "0"
            self.branch = "1"
            self.aluop1 = "0"
            self.aluop0 = "1"

        self.aluop = f"{self.aluop0}{self.aluop1}"

        if self.aluop == "00":
            self.alu_control = "0000 and"
        if self.aluop == "01":
            self.alu_control = "0001 or"
        if self.aluop == "10":
            self.alu_control = "0010 add"
        if self.aluop == "11":
            self.alu_control = "0111 slt"

        self.o = opcode2instruction(str(self.instr_0_5))

    def read_register(self,reg):
        # reg = self.instr_21_25
        reg = bin2hex(reg)
        reg = hex2des(reg)
        print(type(reg))
        for regi in self.registers:
            if int(regi[2]) == reg:
                d = regi[0]
        d = dec2hex(int(d))
        return d


def code(code, _format=None):
    instr_26_31 = crop_bits(hex2bin(code), 26, 31)
    instr_21_25 = crop_bits(hex2bin(code), 21, 25)
    instr_16_20 = crop_bits(hex2bin(code), 16, 20)
    instr_11_15 = crop_bits(hex2bin(code), 11, 15)
    instr_0_15 = crop_bits(hex2bin(code), 0, 15)
    instr_0_5 = crop_bits(hex2bin(code), 0, 5)

    rs = crop_bits(hex2bin(code), 21, 25)
    rs = _adddollar(bin2dec(rs))
    rt = crop_bits(hex2bin(code), 16, 20)
    rt = _adddollar(bin2dec(rt))
    rd = crop_bits(hex2bin(code), 11, 15)
    rd = _adddollar(bin2dec(rd))

    se = sing_extend(instr_0_15)


    regdst = ""
    alusrc = ""
    memtoreg = ""
    regwrite = ""
    memread = ""
    memwrite = ""
    branch = ""
    aluop1 = ""
    aluop0 = ""

    if _format == "r":
        regdst = "1"
        alusrc = "0"
        memtoreg = "0"
        regwrite = "1"
        memread = "0"
        memwrite = "0"
        branch = "0"
        aluop1 = "1"
        aluop0 = "0"

    if _format == "lw":
        regdst = "0"
        alusrc = "1"
        memtoreg = "1"
        regwrite = "1"
        memread = "1"
        memwrite = "0"
        branch = "0"
        aluop1 = "0"
        aluop0 = "0"

    if _format == "sw":
        regdst = "x"
        alusrc = "1"
        memtoreg = "x"
        regwrite = "0"
        memread = "0"
        memwrite = "1"
        branch = "0"
        aluop1 = "0"
        aluop0 = "0"

    if _format == "beq":
        regdst = "x"
        alusrc = "0"
        memtoreg = "x"
        regwrite = "0"
        memread = "0"
        memwrite = "0"
        branch = "1"
        aluop1 = "0"
        aluop0 = "1"

    aluop = f"{aluop0}{aluop1}"

    if aluop == "00":
        alu_control = "0000 and"
    if aluop == "01":
        alu_control = "0001 or"
    if aluop == "10":
        alu_control = "0010 add"
    if aluop == "11":
        alu_control = "0111 slt"

    o = opcode2instruction(str(instr_0_5))
    print("-------------Instruction---------------")
    for line in o:
        print(line[1].strip('\t'), rd+",",rt+",",rs)
        break
    print(code)
    print(f"[{crop_bits(hex2bin(code), 26, 31)}|{crop_bits(hex2bin(code), 21, 25)}|{crop_bits(hex2bin(code), 16, 20)}|{crop_bits(hex2bin(code), 11, 15)}|{crop_bits(hex2bin(code), 6, 10)}|{crop_bits(hex2bin(code), 0, 5)}]")
    print("---------------------------------------")
    # print("\n")

    print(f"instruction[31-26] = {instr_26_31} ---- {bin2hex(instr_26_31)}")
    print(f"instruction[25-21] = {instr_21_25} ---- {bin2hex(instr_21_25)}")
    print(f"instruction[20-16] = {instr_16_20} ---- {bin2hex(instr_16_20)}")
    print(f"instruction[15-11] = {instr_11_15} ---- {bin2hex(instr_11_15)}")
    print(f"instruction[15-0] = {instr_0_15} ---- {bin2hex(instr_0_15)}")
    print(f"instruction[5-0] = {instr_0_5} ---- {bin2hex(instr_0_5)}")



    print("--------------------------")

    print(f"opcode = {instr_0_5}")
    print("register file:")
    print(f"rs = read addr 1  = {rs} ")
    print(f"rt = read addr 2  = {rt}")
    print(f"rd = {rd}")

    print("--------------------------")

    print("sing extend:")
    print(f"input = {instr_0_15} ---- {bin2hex(instr_0_15)}")
    print(f"output = {se} ---- {bin2hex(se)}")

    print("--------------------------")

    print("control:")
    print(f"regdst = {regdst}")
    print(f"alusrc = {alusrc}")
    print(f"memtoreg = {memtoreg}")
    print(f"regwrite = {regwrite}")
    print(f"memread = {memread}")
    print(f"memwrite = {memwrite}")
    print(f"branch = {branch}")
    print(f"aluop1 = {aluop1}")
    print(f"aluop0 = {aluop0}")
    print(f"aluop = {aluop0}{aluop1}")

    print("--------------------------")

    print(f"alu control = {alu_control}")

def _printalu(n):
    n= f"0x{n}"
    return n

def _puttext(img, text, pos,mode):
    if mode == "hex":
        text =(bin2hex(int(text)))
    if mode == "bin":
        text = text
    if mode == None:
        text = text
    img = cv2.putText(img, text, pos, cv2.FONT_HERSHEY_SIMPLEX, 0.35, [0, 0, 255], 1, cv2.LINE_AA)
    return img



def diag(hh):
    diagram = cv2.imread("docs/diagram.jpg")
    mode = "hex"

    diagram = cv2.rectangle(diagram,(25,25),(280,360),[200,200,200],2)


    #memread
    diagram = _puttext(diagram, hh.memread, (700, 214),mode)
    #branch
    diagram = _puttext(diagram, hh.branch, (678, 197),mode)

    # aluop
    diagram = _puttext(diagram, hh.aluop, (681, 247),mode)

    # memwrite
    diagram = _puttext(diagram, hh.memwrite, (696, 263),mode)

    # alusrc
    diagram = _puttext(diagram, hh.alusrc, (682, 279),mode)

    # reg write
    diagram = _puttext(diagram, hh.regwrite, (690, 295),mode)

    #memtoreg
    diagram = _puttext(diagram, hh.memtoreg, (705, 231),mode)

    #regdst
    diagram = _puttext(diagram, hh.regdst, (562, 140),mode)

    #instr 31-26
    diagram = _puttext(diagram, hh.instr_26_31, (503, 212),mode)

    #instr 21-25
    diagram = _puttext(diagram, hh.instr_21_25, (503, 308),mode)

    #instr 16-20
    diagram = _puttext(diagram, hh.instr_16_20, (503, 350),mode)

    #instr 11-15
    diagram = _puttext(diagram, hh.instr_11_15, (503, 408),mode)

    # instr 0-15
    if mode == "bin":
        diagram = _puttext(diagram, hh.instr_0_15, (466, 492),mode)
    if mode == "hex":
        diagram = _puttext(diagram, hh.instr_0_15, (503, 492), mode)

    # instr 0-31
    if mode == "bin":
        diagram = cv2.line(diagram, (388,388), (290,464), [0,0,255], 1)
        diagram = _puttext(diagram, hex2bin(hh.code), (245,478), mode)
    if mode == "hex":
        diagram = _puttext(diagram, hex2bin(hh.code), (378, 370), mode)

    #instr 0-5
    diagram = _puttext(diagram, hh.instr_0_5, (630, 565),mode)

    #rearegister1
    diagram = _puttext(diagram, hh.rs, (644, 329),None)

    # rearegister
    diagram = _puttext(diagram, hh.rt, (644, 366), None)

    # adrass
    diagram = _puttext(diagram, hh.adrs, (360, 210), None)

    # adrass+4
    diagram = _puttext(diagram, hh.adrs_after_add4, (540, 95), None)

    # alu control
    diagram = _puttext(diagram, f"{hh.aluop0}{hh.aluop1}", (820, 537), mode)

    # read data1
    diagram = cv2.line(diagram, (710, 340), (785, 290), [0, 0, 255], 1)
    diagram = _puttext(diagram, hh.read_register(hh.instr_21_25), (795, 290), None)

    # read data2
    diagram = cv2.line(diagram, (710, 392), (785, 315), [0, 0, 255], 1)
    diagram = _puttext(diagram, hh.read_register(hh.instr_16_20), (795, 315), None)





    print(diagram.shape)

    diagram= diagram[0:630, 285:1100]
    cv2.imshow("gg", diagram)
    cv2.waitKey(0)





class memory():
    def __init__(self, bit_addras, index, block, offset, way):
        self.bit_adrs = bit_addras
        self.index = index
        self.block = block
        self.offset = offset
        self.way = way
        self.tag = self.bit_adrs - (index + block + offset)

        n = index
        m = block

        self.words_in_block = 2 ** n
        self.bytes_in_block = 2 ** (m + 2)
        self.total_bits_in_memory = (((2 ** m) * bit_addras) + (bit_addras - (n + m + 2) + 1)) * 2 ** n

    def location(self, hex):
        b = hex2bin(hex)
        offset1 = crop_bits(b, 0, self.offset - 1)
        block1 = crop_bits(b, self.offset, self.block + 1)
        t = self.block + self.offset
        g = self.block + self.offset + self.index - 1
        index1 = crop_bits(b, t, g)
        t = self.block + self.offset + self.index
        g = self.bit_adrs - 1
        tag1 = crop_bits(b, t, g)
        print(f"{tag1}  {index1}  {block1}  {offset1}")
        print("")
        print(f"offset = {offset1}  |  {bin2hex(offset1)}")
        print(f"block = {block1}  |  {bin2hex(block1)}")
        print(f"index = {index1}  |  {bin2hex(index1)}")
        print(f"tag= {tag1}  |  {bin2hex(tag1)}")

