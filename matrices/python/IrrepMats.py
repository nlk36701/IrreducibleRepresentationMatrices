import numpy as np

c3 = np.cos(np.pi/3)
s3 = np.sin(np.pi/3)



irrm_C1 = {
        "A": np.array([[[1]]])
        }

irrm_Cs = {
        "A'":  np.array([[[1]], [[1]]]), 
        "A''": np.array([[[1]], [[-1]]])
        }

irrm_Ci = {
        "Ag": np.array([[[1]], [[1]]]), 
        "Au": np.array([[[1]], [[-1]]])
        }

irrm_C2 = {
        "A": np.array([[[1]], [[1]]]), 
        "B": np.array([[[1]], [[-1]]])
        }
irrm_C3 = {
      "A" : np.array([[[1]],[[1]],  [[1]]]),
    "E_1" : np.array([[[1]],[[e3]], [[ce3]]]),
    "E_2" : np.array([[[1]],[[ce3]],[[e3]]])
}
irrm_C4 = {
    "A"  :  np.array([[[1]],[[1]],[[1]],[[1]]]),
    "B"  :  np.array([[[1]],[[-1]],[[1]],[[-1]]]),
    "E_1" : np.array([[[1]],[[im]],[[-1]],[[-im]]]),
    "E_2" : np.array([[[1]],[[-im]],[[-1]],[[im]]])
}

irrm_C5 = {
    "A"    : np.array([[[1]],[[1]],[[1]],[[1]],[[1]]]),
    "E1_1" : np.array([[[1]],[[e5]],[[e25]],[[ce25]],[[ce5]]]),
    "E1_2" : np.array([[[1]],[[ce5]],[[ce25]],[[e25]],[[e5]]]),
    "E2_1" : np.array([[[1]],[[e25]],[[ce5]],[[e5]],[[ce25]]]),
    "E2_2" : np.array([[[1]],[[ce25]],[[e5]],[[ce5]],[[e25]]])
}

irrm_C6 = {
    "A"    : np.array([[[1]],[[1]],[[1]],[[1]],[[1]],[[1]]]),
    "B"    : np.array([[[1]],[[-1]],[[1]],[[-1]],[[1]],[[-1]]]),
    "E1_1" : np.array([[[1]],[[e6]],[[-ce6]],[[-1]],[[-e6]],[[ce6]]]),
    "E1_2" : np.array([[[1]],[[ce6]],[[-e6]],[[-1]],[[-ce6]],[[e6]]]),
    "E2_1" : np.array([[[1]],[[-ce6]],[[-e6]],[[1]],[[-ce6]],[[-e6]]]),
    "E2_2" : np.array([[[1]],[[-e6]],[[-ce6]],[[1]],[[-e6]],[[-ce6]]])
}

irrm_C7 = {
    "A"    :  np.array([[[1]],[[1]],[[1]],[1],[[1]],[[1]],[1]]),
    "E1_1" :  np.array([[[1]],[[e7]],[[e72]],[[e73]],[[ce73]],[[ce72]],[[ce7]]]),
    "E1_2" :  np.array([[[1]],[[ce7]],[[ce72]],[[ce73]],[[e73]],[[e72]],[[e7]]]),
    "E2_1" :  np.array([[[1]],[[e72]],[[ce73]],[[ce7]],[[e7]],[[e73]],[[ce72]]]),
    "E2_2" :  np.array([[[1]],[[ce72]],[[e73]],[[e7]],[[ce7]],[[ce73]],[[e72]]]),
    "E3_1" :  np.array([[[1]],[[e73]],[[ce7]],[[e72]],[[ce72]],[[e7]],[[ce73]]]),
    "E3_2" :  np.array([[[1]],[[ce73]],[[e7]],[[ce72]],[[e72]],[[ce7]],[[e73]]])
}

irrm_C8 = {
    "A"    : np.array([[[1]],[[1]],   [[1]],[[1]],[[1]],[[1]],[[1]],[[1]]]),
    "B"    : np.array([[[1]],[[-1]],   [[1]],[[-1]],[[1]],[[-1]],[[1]],[[-1]]]),
    "E1_1" : np.array([[[1]],  [[e8]], [[im]],[[-ce8]],[[-1]], [[-e8]],[[-im]], [[ce8]]]),
    "E1_2" : np.array([[[1]], [[ce8]],[[-im]], [[-e8]],[[-1]],[[-ce8]], [[im]],  [[e8]]]),
    "E2_1" : np.array([[[1]],  [[im]], [[-1]], [[-im]], [[1]],  [[im]], [[-1]], [[-im]]]),
    "E2_2" : np.array([[[1]], [[-im]], [[-1]],  [[im]], [[1]], [[-im]], [[-1]],  [[im]]]),
    "E3_1" : np.array([[[1]], [[-e8]], [[im]], [[ce8]],[[-1]],  [[e8]],[[-im]],[[-ce8]]]),
    "E3_2" : np.array([[[1]],[[-ce8]],[[-im]],  [[e8]],[[-1]], [[ce8]], [[im]], [[-e8]]])
}

irrm_S4 = {
    "A"   : np.array([[[1]],[[1]],[[1]],[[1]]]),
    "B"   : np.array([[[1]],[[1]],[[-1]],[[-1]]]),
    "E_1" : np.array([[[1]],[[-1]],[[im]],[[-im]]]),
    "E_2" : np.array([[[1]],[[-1]],[[-im]],[[im]]])
}

irrm_S6 = {
    "Ag"   : np.array([[[1]],[[1]], [[1]],[[1]],[[1]],[[1]]]),
    "Eg1"  : np.array([[[1]],[[1]], [[e3]],[[ce3]],[[ce3]],[[e3]]]),
    "Eg2"  : np.array([[[1]],[[1]], [[ce3]],[[e3]],[[e3]],[[ce3]]]),
    "Au"   : np.array([[[1]],[[-1]],[[1]],[[1]],[[-1]],[[-1]]]),
    "Eu1"  : np.array([[[1]],[[-1]],[[e3]],[[ce3]],[[-ce3]],[[-e3]]]),
    "Eu2"  : np.array([[[1]],[[-1]],[[ce3]],[[e3]],[[-e3]],[[-ce3]]])
}

irrm_S8 = {
    "A"    : np.array([[[1]],[[1]], [[1]], [[1]],[[1]],[[1]],[[1]],[[1]]]),
    "B"    : np.array([[[1]],[[1]], [[1]], [[1]],[[-1]],[[-1]],[[-1]],[[-1]]]),
    "E1_1" : np.array([[[1]], [[im]],[[-1]],[[-im]],  [[e8]],[[-ce8]], [[-e8]], [[ce8]]]),
    "E1_2" : np.array([[[1]],[[-im]],[[-1]], [[im]], [[ce8]], [[-e8]],[[-ce8]],  [[e8]]]),
    "E2_1" : np.array([[[1]], [[-1]], [[1]], [[-1]],  [[im]], [[-im]],  [[im]], [[-im]]]),
    "E2_2" : np.array([[[1]], [[-1]], [[1]], [[-1]], [[-im]],  [[im]], [[-im]],  [[im]]]),
    "E3_1" : np.array([[[1]],[[-im]],[[-1]], [[im]],[[-ce8]],  [[e8]], [[ce8]], [[-e8]]]),
    "E3_2" : np.array([[[1]], [[im]],[[-1]],[[-im]], [[-e8]], [[ce8]],  [[e8]],[[-ce8]]])
    }

irrm_C2h = {
    "Ag": [[[1]],[[1]],[[1]],[[1]]],
    "Bg": [[[1]],[[-1]],[[1]],[[-1]]],
    "Au": [[[1]],[[-1]],[[-1]],[[1]]],
    "Bu": [[[1]],[[1]],[[-1]],[[-1]]]
}
irrm_C3h = {
    "A'"   : np.array([[[1]],[[1]],[[1]],[[1]],[[1]],[[1]]]),
    "E'1"  : np.array([[[1]],[[1]],[[e3]],[[ce3]],[[e3]],[[ce3]]]),
    "E'2"  : np.array([[[1]],[[1]],[[ce3]],[[e3]],[[ce3]],[[e3]]]),
    "A''"  : np.array([[[1]],[[-1]],[[1]],[[1]],[[-1]],[[-1]]]),
    "E''1" : np.array([[[1]],[[-1]],[[e3]],[[ce3]],[[-e3]],[[-ce3]]]),
    "E''2" : np.array([[[1]],[[-1]],[[ce3]],[[e3]],[[-ce3]],[[-e3]]])
}

irrm_C4h = {
    "Ag"  : np.array([[[1]], [[1]], [[1]],  [[1]], [[1]],  [[1]],  [[1]],  [[1]]]),
    "Bg"  : np.array([[[1]], [[1]], [[1]], [[-1]], [[1]], [[-1]], [[-1]], [[-1]]]),
    "Eg1" : np.array([[[1]],[[-1]], [[1]], [[im]],[[-1]],[[-im]],[[-im]], [[im]]]),
    "Eg2" : np.array([[[1]],[[-1]], [[1]],[[-im]],[[-1]], [[im]], [[im]],[[-im]]]),
    "Au"  : np.array([[[1]],[[-1]],[[-1]],  [[1]], [[1]],  [[1]], [[-1]], [[-1]]]),
    "Bu"  : np.array([[[1]],[[-1]],[[-1]], [[-1]], [[1]], [[-1]],  [[1]],  [[1]]]),
    "Eu1" : np.array([[[1]], [[1]],[[-1]], [[im]],[[-1]],[[-im]], [[im]],[[-im]]]),
    "Eu2" : np.array([[[1]], [[1]],[[-1]],[[-im]],[[-1]], [[im]],[[-im]], [[im]]])
}

irrm_C5h = {
    "A'"    : np.array([[[1]], [[1]],    [[1]],    [[1]],    [[1]],    [[1]],    [[1]],    [[1]],    [[1]],    [[1]]]),
    "E1'1"  : np.array([[[1]], [[1]],   [[e5]],  [[e25]], [[ce25]],  [[ce5]],   [[e5]],  [[e25]], [[ce25]],  [[ce5]]]),
    "E1'2"  : np.array([[[1]], [[1]],  [[ce5]], [[ce25]],  [[e25]],   [[e5]],  [[ce5]], [[ce25]],  [[e25]],   [[e5]]]),
    "E2'1"  : np.array([[[1]], [[1]],  [[e25]],  [[ce5]],   [[e5]], [[ce25]],  [[e25]],  [[ce5]],   [[e5]], [[ce25]]]),
    "E2'2"  : np.array([[[1]], [[1]], [[ce25]],   [[e5]],  [[ce5]],  [[e25]], [[ce25]],   [[e5]],  [[ce5]],  [[e25]]]),
    "A''"   : np.array([[[1]],[[-1]],    [[1]],    [[1]],    [[1]],    [[1]],   [[-1]],   [[-1]],   [[-1]],   [[-1]]]),
    "E1''1" : np.array([[[1]],[[-1]],   [[e5]],  [[e25]], [[ce25]],  [[ce5]],  [[-e5]], [[-e25]],[[-ce25]], [[-ce5]]]),
    "E1''2" : np.array([[[1]],[[-1]],  [[ce5]], [[ce25]],  [[e25]],   [[e5]], [[-ce5]],[[-ce25]], [[-e25]],  [[-e5]]]),
    "E2''1" : np.array([[[1]],[[-1]],  [[e25]],  [[ce5]],   [[e5]], [[ce25]], [[-e25]], [[-ce5]],  [[-e5]],[[-ce25]]]),
    "E2''2" : np.array([[[1]],[[-1]], [[ce25]],   [[e5]],  [[ce5]],  [[e25]],[[-ce25]],  [[-e5]], [[-ce5]], [[-e25]]])
}

irrm_C6h = {
    "Ag"   : np.array([[[1]], [[1]], [[1]],   [[1]],   [[1]], [[1]],   [[1]],   [[1]],   [[1]],   [[1]],   [[1]],   [[1]]]),
    "Bg"   : np.array([[[1]],[[-1]], [[1]],  [[-1]],   [[1]],[[-1]],   [[1]],  [[-1]],   [[1]],  [[-1]],  [[-1]],   [[1]]]),
    "E1g1" : np.array([[[1]],[[-1]], [[1]],  [[e6]],[[-ce6]],[[-1]], [[-e6]], [[ce6]], [[-e6]], [[ce6]],  [[e6]],[[-ce6]]]),
    "E1g2" : np.array([[[1]],[[-1]], [[1]], [[ce6]], [[-e6]],[[-1]],[[-ce6]],  [[e6]],[[-ce6]],  [[e6]], [[ce6]], [[-e6]]]),
    "E2g1" : np.array([[[1]], [[1]], [[1]],[[-ce6]], [[-e6]], [[1]],[[-ce6]], [[-e6]],[[-ce6]], [[-e6]],[[-ce6]], [[-e6]]]),
    "E2g2" : np.array([[[1]], [[1]], [[1]], [[-e6]],[[-ce6]], [[1]], [[-e6]],[[-ce6]], [[-e6]],[[-ce6]], [[-e6]],[[-ce6]]]),
    "Au"   : np.array([[[1]],[[-1]],[[-1]],   [[1]],   [[1]], [[1]],   [[1]],   [[1]],  [[-1]],  [[-1]],  [[-1]],  [[-1]]]),
    "Bu"   : np.array([[[1]], [[1]],[[-1]],  [[-1]],   [[1]],[[-1]],   [[1]],  [[-1]],  [[-1]],   [[1]],   [[1]],  [[-1]]]),
    "E1u1" : np.array([[[1]], [[1]],[[-1]],  [[e6]],[[-ce6]],[[-1]], [[-e6]], [[ce6]],  [[e6]],[[-ce6]], [[-e6]], [[ce6]]]),
    "E1u2" : np.array([[[1]], [[1]],[[-1]], [[ce6]], [[-e6]],[[-1]],[[-ce6]],  [[e6]], [[ce6]], [[-e6]],[[-ce6]],  [[e6]]]),
    "E2u1" : np.array([[[1]],[[-1]],[[-1]],[[-ce6]], [[-e6]], [[1]],[[-ce6]], [[-e6]], [[ce6]],  [[e6]], [[ce6]],  [[e6]]]),
    "E2u2" : np.array([[[1]],[[-1]],[[-1]], [[-e6]],[[-ce6]], [[1]], [[-e6]],[[-ce6]],  [[e6]], [[ce6]],  [[e6]], [[ce6]]])
}


irrm_C2v = {
        "A1": np.array([[[1.]], [[1.]], [[1.]],  [[1.]]]), 
        "A2": np.array([[[1.]], [[1.]], [[-1.]], [[-1.]]]),
        "B1": np.array([[[1.]], [[-1.]], [[-1.]], [[1.]]]), 
        "B2": np.array([[[1.]], [[-1.]], [[1.]], [[-1.]]])
}

irrm_C3v = {
        "A1" : np.array([[[1]],[[1]],[[1]],[[1]], [[1 ]],[[1 ]]]),
        "A2" : np.array([[[1]],[[1]],[[1]],[[-1]],[[-1]],[[-1]]]),
        "E"  : np.array([[[1, 0],[0, 1]], [[-c3, -s3],[ s3, -c3]], [[-c3, s3],[ -s3, -c3]], [[1, 0],[0, -1]], [[-c3, -s3],[ -s3, c3]], [[-c3, s3],[ s3, c3]]])
    }

irrm_C4v = {
    "A1" : np.array([[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]]]),
    "A2" : np.array([[[1]],[[1]],[[1]],[[1]],[[-1]],[[-1]],[[-1]],[[-1]]]),
    "B1" : np.array([[[1]],[[-1]],[[1]],[[-1]],[[1]],[[1]],[[-1]],[[-1]]]),
    "B2" : np.array([[[1]],[[-1]],[[1]],[[-1]],[[-1]],[[-1]],[[1]],[[1]]]),
    "E"  : np.array([[[1, 0],[0, 1]],[[0, -1],[1, 0]],[[-1, 0],[0, -1]],[[0, 1],[ -1, 0]],[[1, 0], [0, -1]],[[-1, 0], [0, 1]],[[0, 1], [1, 0]],[[0, -1], [-1, 0]]])
}

irrm_C5v = {
    "A1" : np.array([[[1]],[[1]],[[1]],[[1]],[[1]],[[1]], [[1]], [[1]], [[1]],[[1]]]),
    "A2" : np.array([[[1]],[[1]],[[1]],[[1]],[[1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]]]),
    "E1" : np.array([[[1,  0], [0, 1]],[[c25, -s25], [s25, c25]],[[-c5, -s5],[s5, -c5]],[[-c5, s5],[-s5, -c5]],[[c25, s25],[-s25, c25]],
             [[1, 0],[0, -1]],[[-c5, s5],[s5, c5]],[[c25, -s25], [-s25, -c25]],[[c25, s25],[s25, -c25]],[[-c5,-s5],[-s5, c5]]]),
    "E2" : np.array([[[1, 0],[0, 1]],[[-c5, -s5],[s5, -c5]],[[c25, s25],[-s25, c25]],[[c25, -s25],[s25, c25]],[[-c5, s5], [-s5, -c5]],
             [[1, 0],[0, -1]],[[c25, -s25], [-s25, -c25]],[[-c5, -s5], [-s5, c5]],[[-c5, s5], [s5, c5]],[[c25, s25],[s25, -c25]]])
}

irrm_C6v = {
    "A1" : np.array([[[1]],[[1]], [[1]],[[1]], [[1]],[[1]], [[1]],[[1]],[[1]],[[1]],[[1]],[[1]]]),
    "A2" : np.array([[[1]],[[1]], [[1]],[[1]], [[1]],[[1]], [[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]]]),
    "B1" : np.array([[[1]],[[-1]],[[1]],[[-1]],[[1]],[[-1]],[[1]],[[1]],[[1]],[[-1]],[[-1]],[[-1]]]),
    "B2" : np.array([[[1]],[[-1]],[[1]],[[-1]],[[1]],[[-1]],[[-1]],[[-1]],[[-1]],[[1]],[[1]],[[1]]]),
    "E1" : np.array([[[1, 0],[0, 1]],[[c3, -s3],[s3, c3]],[[-c3, -s3],[s3, -c3]],[[-1, 0],[0, -1]],[[-c3, s3],[-s3, -c3]],[[c3, s3],[-s3, c3]],
             [[1, 0],[0, -1]],[[-c3, s3],[s3, c3]],[[-c3, -s3],[-s3, c3]],[[c3, s3],[s3, -c3]],[[-1, 0],[0, 1]],[[c3, -s3],[-s3, -c3]]]),
    "E2" : np.array([[[1, 0],[0, 1]],[[-c3, s3],[-s3, -c3]],[[-c3, -s3],[s3, -c3]],[[1, 0],[0, 1]],[[-c3, s3],[-s3, -c3]],[[-c3, -s3],[s3, -c3]],
             [[1, 0],[0, -1]],[[-c3, s3],[s3, c3]],[[-c3, -s3],[-s3, c3]],[[-c3, -s3],[-s3, c3]],[[1, 0],[0, -1]],[[-c3, s3],[s3, c3]]])
}


irrm_D2 = {
    "A"  : np.array([[[1]],[[1]],[[1]],[[1]]]),
    "B1" : np.array([[[1]],[[1]],[[-1]],[[-1]]]),
    "B2" : np.array([[[1]],[[-1]],[[-1]],[[1]]]),
    "B3" : np.array([[[1]],[[-1]],[[1]],[[-1]]])} # To preserve Cotton ordering, our symels are zxy and Cotton's are zyx (Essentially swap B2 and B3}
irrm_D3 = {
    "A1" : np.array([[[1]],[[1]],[[1]],[[1]],[[1]],[[1]]]),
    "A2" : np.array([[[1]],[[1]],[[1]],[[-1]],[[-1]],[[-1]]]),
    "E"  : np.array([[[1, 0],[0, 1]],[[-c3, -s3],[s3, -c3]],[[-c3, s3],[-s3, -c3]],[[1, 0],[0, -1]],[[-c3, -s3],[-s3, c3]],[[-c3, s3],[s3, c3]]])
}

irrm_D4 = {
    "A1" : [[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]]],
    "A2" : [[[1]],[[1]],[[1]],[[1]],[[-1]],[[-1]],[[-1]],[[-1]]],
    "B1" : [[[1]],[[-1]],[[1]],[[-1]],[[1]],[[1]],[[-1]],[[-1]]],
    "B2" : [[[1]],[[-1]],[[1]],[[-1]],[[-1]],[[-1]],[[1]],[[1]]],
    "E"  : [[[1, 0],[0, 1]],[[0, -1],[1, 0]],[[-1, 0],[0, -1]],[[0, 1],[-1, 0]],[[1, 0],[0, -1]],[[-1, 0],[0, 1]],[[0, 1],[1, 0]],[[0, -1],[-1, 0]]]
}
irrm_D5 = {
    "A1" : [[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]]],
    "A2" : [[[1]],[[1]],[[1]],[[1]],[[1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]]],
    "E1" : [[[1, 0],[0, 1]],[[c25, -s25],[ s25, c25]],[[-c5, -s5],[ s5, -c5]],[[-c5, s5],[ -s5, -c5]],[[c25, s25],[ -s25, c25]],
             [[1, 0],[0, -1]],[[-c5, s5],[ s5, c5]],[[c25, -s25],[ -s25, -c25]],[[c25, s25],[ s25, -c25]],[[-c5, -s5],[ -s5, c5]]],
    "E2" : [[[1, 0],[0, 1]],[[-c5, -s5],[ s5, -c5]],[[c25, s25],[ -s25, c25]],[[c25, -s25],[ s25, c25]],[[-c5, s5],[ -s5, -c5]],
             [[1, 0],[0, -1]],[[c25, -s25],[ -s25, -c25]],[[-c5, -s5],[ -s5, c5]],[[-c5, s5],[ s5, c5]],[[c25, s25],[ s25, -c25]]]}
irrm_D6 = {
    "A1" : [[[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]]],
    "A2" : [[[1]], [[1]], [[1]], [[1]], [[1]], [[1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]]],
    "B1" : [[[1]],[[-1]], [[1]],[[-1]], [[1]],[[-1]], [[1]], [[1]], [[1]],[[-1]],[[-1]],[[-1]]],
    "B2" : [[[1]],[[-1]], [[1]],[[-1]], [[1]],[[-1]],[[-1]],[[-1]],[[-1]], [[1]], [[1]], [[1]]],
    "E1" : [[[1, 0],[0, 1]],[[c3, -s3],[s3, c3]],[[-c3, -s3],[s3, -c3]],[[-1, 0],[0, -1]],[[-c3, s3],[-s3, -c3]],[[c3, s3],[-s3, c3]],
             [[1, 0],[0, -1]],[[-c3, s3],[s3, c3]],[[-c3, -s3],[-s3, c3]],[[c3, s3],[s3, -c3]],[[-1, 0],[0, 1]],[[c3, -s3],[-s3, -c3]]],
    "E2" : [[[1, 0],[0, 1]],[[-c3, s3],[-s3, -c3]],[[-c3, -s3],[s3, -c3]],[[1, 0],[0, 1]],[[-c3, s3],[-s3, -c3]],[[-c3, -s3],[s3, -c3]],
             [[-1, 0],[0, 1]],[[c3, -s3],[-s3, -c3]],[[c3, s3],[s3, -c3]],[[c3, s3],[s3, -c3]],[[-1, 0],[ 0, 1]],[[c3, -s3],[-s3, -c3]]]
}
irrm_D8 = {
    "A1" : np.array([[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],
             [[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]]]),
    "A2" : np.array([[[1]], [[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],
            [[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]]]),
    "B1" : np.array([[[1]],[[-1]],[[1]],[[-1]],[[1]],[[-1]],[[1]],[[-1]],
             [[1]],[[1]],[[1]],[[1]],[[-1]],[[-1]],[[-1]],[[-1]]]),
    "B2" : np.array([[[1]],[[-1]],[[1]],[[-1]],[[1]],[[-1]],[[1]],[[-1]],
             [[-1]],[[-1]],[[-1]],[[-1]],[[1]],[[1]],[[1]],[[1]]]),
    "E1" : np.array([[[1, 0],[0, 1]],[[c4, -s4]],[[s4, c4]],[[0, -1],[1, 0]],[[-c4, -s4],[s4, -c4]],[[-1, 0],[0, -1]],[[-c4, s4],[-s4, -c4]],[[0, 1],[-1, 0]],[[c4, s4],[-s4, c4]],
             [[1, 0],[0, -1]],[[0, 1],[1, 0]],[[-1, 0],[0, 1]],[[0, -1],[-1, 0]],[[c4, s4],[s4, -c4]],[[-c4, s4],[s4, c4]],[[-c4, -s4],[-s4, c4]],[[c4, -s4],[-s4, -c4]]]),
    "E2" : np.array([[[1, 0],[0, 1]],[[0, -1],[1, 0]],[[-1, 0],[0, -1]],[[0, 1],[-1, 0]],[[1, 0],[0, 1]],[[0, -1],[1, 0]],[[-1, 0],[0, -1]],[[0, 1],[-1, 0]],
             [[1, 0],[0, -1]],[[-1, 0],[0, 1]],[[1, 0],[0, -1]],[[-1, 0],[0, 1]],[[0, 1],[1, 0]],[[0 ,-1],[-1, 0]],[[0, 1],[1, 0]],[[0, -1],[-1, 0]]]),
    "E3" : np.array([[[1, 0],[0, 1]],[[-c4, s4],[-s4, -c4]],[[0, -1],[1, 0]],[[c4, s4],[-s4, c4]],[[-1, 0],[0, -1]],[[c4, -s4],[s4, c4]],[[0, 1],[-1, 0]],[[-c4, -s4],[s4, -c4]],
             [[-1, 0],[0, 1]],[[0, -1],[-1, 0]],[[1, 0],[0, -1]],[[0, 1],[1, 0]],[[c4, s4],[s4, -c4]],[[-c4, s4],[s4, c4]],[[-c4, -s4],[-s4, c4]],[[c4, -s4],[-s4, -c4]]])
}

irrm_D2h = {
    "Ag"  : np.array([[[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]]]),
    "B1g" : np.array([[[1]], [[1]], [[1]], [[1]],[[-1]],[[-1]],[[-1]],[[-1]]]),
    "B2g" : np.array([[[1]],[[-1]], [[1]],[[-1]],[[-1]], [[1]], [[1]],[[-1]]]),
    "B3g" : np.array([[[1]],[[-1]], [[1]],[[-1]], [[1]],[[-1]],[[-1]], [[1]]]),
    "Au"  : np.array([[[1]],[[-1]],[[-1]], [[1]], [[1]], [[1]],[[-1]],[[-1]]]),
    "B1u" : np.array([[[1]],[[-1]],[[-1]], [[1]],[[-1]],[[-1]], [[1]], [[1]]]),
    "B2u" : np.array([[[1]], [[1]],[[-1]],[[-1]],[[-1]], [[1]],[[-1]], [[1]]]),
    "B3u" : np.array([[[1]], [[1]],[[-1]],[[-1]], [[1]],[[-1]], [[1]],[[-1]]])

} # Cotton ordering is different because I put x in front of y...
irrm_D3h = {
    "A1'" : np.array([[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]]]),
    "A2'" : np.array([[[1]],[[1]],[[1]],[[1]],[[-1]],[[-1]],[[-1]],[[1]],[[1]],[[-1]],[[-1]],[[-1]]]),
    "E'"  : np.array([[[1, 0],[0, 1]],[[1, 0],[0, 1]],[[-c3, -s3],[s3, -c3]],[[-c3, s3],[-s3, -c3]],[[1, 0],[0, -1]],[[-c3, -s3],[-s3, c3]],[[-c3, s3],[s3, c3]],
             [[-c3, -s3],[s3, -c3]],[[-c3, s3],[-s3, -c3]],[[1, 0],[0, -1]],[[-c3, -s3],[-s3, c3]],[[-c3, s3],[s3, c3]]]),
    "A1''" : np.array([[[1]],[[-1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]]]),
    "A1''" : np.array([[[1]],[[-1]],[[1]],[[1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[1]],[[1]],[[1]]]),
    "E''" : np.array([[[1, 0],[0, 1]],[[-1, 0],[0, -1]],[[-c3, -s3],[s3, -c3]],[[-c3, s3],[-s3, -c3]],[[1, 0],[0, -1]],[[-c3, -s3],[-s3, c3]],[[-c3, s3],[s3, c3]],
             [[c3, s3],[-s3, c3]],[[c3, -s3],[s3, c3]],[[-1,  0],[0, 1]],[[c3, s3],[s3, -c3]],[[c3, -s3],[-s3, -c3]]])
             
}
irrm_D4h = {
    "A1g" : np.array([[[1]], [[1]], [[1]],  [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]],   [[1]], [[1]], [[1]], [[1]], [[1]], [[1]]]),
    "A2g" : np.array([[[1]], [[1]], [[1]],  [[1]], [[1]], [[1]],[[-1]],[[-1]],[[-1]],[[-1]],   [[1]], [[1]],[[-1]],[[-1]],[[-1]],[[-1]]]),
    "B1g" : np.array([[[1]], [[1]], [[1]], [[-1]], [[1]],[[-1]], [[1]], [[1]],[[-1]],[[-1]],  [[-1]],[[-1]], [[1]], [[1]],[[-1]],[[-1]]]),
    "B2g" : np.array([[[1]], [[1]], [[1]], [[-1]], [[1]],[[-1]],[[-1]],[[-1]], [[1]], [[1]],  [[-1]],[[-1]],[[-1]],[[-1]], [[1]], [[1]]]),
    "Eg"  : np.array([[[1, 0],[0, 1]],[[-1, 0],[0, -1]],[[1, 0],[0, 1]],
             [[0, -1],[1, 0]],[[-1, 0],[0, -1]],[[0, 1],[-1, 0]],[[1, 0],[0, -1]],[[-1, 0],[0, 1]],[[0, 1],[1, 0]],[[0, -1],[-1, 0]],
             [[0, 1],[-1, 0]],[[0, -1],[1, 0]],[[-1, 0],[0, 1]],[[1, 0],[0, -1]],[[0, -1],[-1, 0]],[[0, 1],[1, 0]]]),
    "A1u" : np.array([ [[1]],[[-1]],[[-1]],  [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]]]),
    "A2u" : np.array([ [[1]],[[-1]],[[-1]],  [[1]], [[1]], [[1]],[[-1]],[[-1]],[[-1]],[[-1]], [[-1]],[[-1]], [[1]], [[1]], [[1]], [[1]]]),
    "B1u" : np.array([ [[1]],[[-1]],[[-1]], [[-1]], [[1]],[[-1]], [[1]], [[1]],[[-1]],[[-1]],  [[1]], [[1]],[[-1]],[[-1]], [[1]], [[1]]]),
    "B2u" : np.array([ [[1]],[[-1]],[[-1]], [[-1]], [[1]],[[-1]],[[-1]],[[-1]], [[1]], [[1]],  [[1]], [[1]], [[1]], [[1]],[[-1]],[[-1]]]),
    "Eu"  : np.array([[[1, 0],[0, 1]],[[1, 0],[0, 1]],[[-1, 0],[0, -1]],
             [[0, -1],[1, 0]],[[-1, 0],[0, -1]],[[0, 1],[-1, 0]],[[1, 0],[0, -1]],[[-1, 0],[0, 1]],[[0, 1],[1, 0]],[[0, -1],[-1, 0]],
             [[0, -1],[1, 0]],[[0, 1],[-1, 0]],[[1, 0],[0, -1]],[[-1, 0],[0, 1]],[[0, 1],[1, 0]],[[0, -1],[-1, 0]]])
}
irrm_D5h = {
    "A1'"  : np.array([[[1]], [[1]],  [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]],
                          [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]]]),
    "A2'"  : np.array([ [[1]], [[1]],  [[1]], [[1]], [[1]], [[1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]],
                          [[1]], [[1]], [[1]], [[1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]]]),
    "E1'"  : np.array([[[1, 0],[0, 1]],[[1, 0],[0, 1]], # E, σh
              [[c25, -s25],[ s25, c25]],[[-c5, -s5],[ s5, -c5]],[[-c5, s5],[ -s5, -c5]],[[c25, s25],[ -s25, c25]], # C5s
              [[1, 0],[0, -1]],[[-c5, s5],[ s5, c5]],[[c25, -s25],[ -s25, -c25]],[[c25, s25],[ s25, -c25]],[[-c5, -s5],[ -s5, c5]],
              [[c25, -s25],[ s25, c25]],[[-c5, -s5],[ s5, -c5]],[[-c5 ,s5],[ -s5, -c5]],[[c25, s25],[ -s25, c25]],
              [[1, 0],[0, -1]],[[-c5, s5],[ s5, c5]],[[c25, -s25],[ -s25, -c25]],[[c25, s25],[ s25, -c25]],[[-c5, -s5],[ -s5, c5]]]),
    "E2'"  : np.array([[[1, 0],[0, 1]],[[1, 0],[0, 1]],
              [[-c5, -s5],[ s5, -c5]],[[c25, s25],[ -s25, c25]],[[c25, -s25],[ s25, c25]],[[-c5, s5],[ -s5, -c5]],
              [[1, 0],[0 ,-1],[c25, -s25]],[[ -s25, -c25]],[[-c5, -s5],[ -s5, c5]],[[-c5, s5],[ s5, c5]],[[c25, s25],[ s25, -c25]],
              [[-c5, -s5],[ s5, -c5]],[[c25, s25],[ -s25, c25]],[[c25, -s25],[ s25, c25]],[[-c5, s5],[ -s5, -c5]],
              [[1, 0],[0, -1]],[[c25, -s25],[ -s25, -c25]],[[-c5, -s5],[ -s5, c5]],[[-c5, s5],[ s5, c5]],[[c25, s25],[ s25, -c25]]]),
    "A1''" : np.array([[[1]],[[-1]],  [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], [[1]],
                         [[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]]]),
    "A2''" : np.array([[[1]],[[-1]],   [[1]], [[1]], [[1]], [[1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]],
                         [[-1]],[[-1]],[[-1]],[[-1]], [[1]], [[1]], [[1]], [[1]], [[1]]]),
    "E1''" : np.array([[[1, 0],[0, 1]],[[-1, 0],[0, -1]], # E, σh
              [[c25, -s25],[ s25, c25]],[[-c5, -s5],[ s5, -c5]],[[-c5, s5],[ -s5, -c5]],[[c25, s25],[ -s25, c25]], # C5s
              [[1, 0],[0, -1]],[[-c5, s5],[ s5, c5]],[[c25, -s25],[ -s25, -c25]],[[c25, s25],[ s25, -c25]],[[-c5, -s5],[ -s5, c5]],
              [[-c25, s25],[ -s25, -c25]],[[c5, s5],[ -s5, c5]],[[c5, -s5],[ s5, c5]],[[-c25, -s25],[ s25, -c25]],
              [[-1, 0],[0, 1]],[[c5, -s5],[ -s5, -c5]],[[-c25, s25],[ s25, c25]],[[-c25, -s25],[ -s25, c25]],[[c5, s5],[ s5, -c5]]]),
    "E2''" : np.array([[[1, 0],[0, 1]],[[-1, 0],[0 ,-1]],
              [[-c5, -s5],[ s5, -c5]],[[c25, s25],[ -s25, c25]],[[c25, -s25],[ s25, c25]],[[-c5, s5],[ -s5, -c5]],
              [[1, 0],[0, -1]],[[c25, -s25],[ -s25, -c25]],[[-c5, -s5],[ -s5 ,c5]],[[-c5, s5],[ s5, c5]],[[c25, s25],[ s25, -c25]],
              [[c5, s5],[ -s5, c5]],[[-c25, -s25],[ s25, -c25]],[[-c25, s25],[ -s25, -c25]],[[c5, -s5],[ s5, c5]],
              [[-1, 0],[0, 1]],[[-c25, s25],[ s25, c25]],[[c5, s5],[ s5, -c5]],[[c5 ,-s5],[ -s5, -c5]],[[-c25, -s25],[ -s25, c25]]])
              
}
irrm_D6h = {
    "A1g" : np.array([ [[1]], [[1]], [[1]], # E, σh, i
               [[1]], [[1]], [[1]], [[1]], [[1]], # Cns
               [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], # C2s
               [[1]], [[1]], [[1]], [[1]], # Sns
               [[1]], [[1]], [[1]], [[1]], [[1]], [[1]]]), # σs
    "A2g" : np.array([ [[1]], [[1]], [[1]], # E, σh, i
               [[1]], [[1]], [[1]], [[1]], [[1]], # Cns
              [[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]], # C2s
               [[1]], [[1]], [[1]], [[1]], # Sns
              [[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]]]), # σs
    "B1g" : np.array([ [[1]],[[-1]], [[1]], # E, σh, i
              [[-1]], [[1]],[[-1]], [[1]],[[-1]], # Cns
               [[1]], [[1]], [[1]],[[-1]],[[-1]],[[-1]], # C2s
               [[1]],[[-1]],[[-1]], [[1]], # Sns
              [[-1]],[[-1]],[[-1]], [[1]], [[1]], [[1]]]), # σs
    "B2g" : np.array([ [[1]],[[-1]], [[1]], # E, σh, i
              [[-1]], [[1]],[[-1]], [[1]],[[-1]], # Cns
              [[-1]],[[-1]],[[-1]], [[1]], [[1]], [[1]], # C2s
               [[1]],[[-1]],[[-1]], [[1]], # Sns
               [[1]], [[1]], [[1]],[[-1]],[[-1]],[[-1]]]), # σs
    "E1g" : np.array([[[1, 0],[0, 1]],[[-1, 0],[0, -1]],[[1, 0],[0, 1]],
              [[c3, -s3],[s3, c3]],[[-c3, -s3],[s3, -c3]],[[-1, 0],[0, -1]],[[-c3, s3],[-s3, -c3]],[[c3, s3],[-s3, c3]],
              [[1, 0],[0, -1]],[[-c3, s3],[s3, c3]],[[-c3, -s3],[-s3, c3]],[[c3, s3],[s3, -c3]],[[-1, 0],[0, 1]],[[c3, -s3],[-s3, -c3]],
              [[-c3, s3],[-s3 -c3]],[[c3, s3],[-s3, c3]],[[c3, -s3],[s3, c3]],[[-c3, -s3],[s3, -c3]],
              [[-1, 0],[0, 1]],[[c3, -s3], [-s3, -c3]],[[c3, s3],[s3, -c3]],[[-c3, -s3],[-s3, c3]],[[1, 0],[0, -1]],[[-c3, s3],[s3, c3]]]),
    "E2g" : np.array([[[1, 0],[0, 1]],[[1, 0],[0, 1]],[[1, 0],[0, 1]],
              [[-c3, s3],[-s3, -c3]],[[-c3, -s3],[s3, -c3]],[[1, 0],[0, 1]],[[-c3, s3],[-s3, -c3]],[[-c3, -s3],[s3, -c3]],
              [[-1, 0],[0, 1]],[[c3, -s3],[-s3, -c3]],[[c3, s3],[s3, -c3]],[[c3, s3],[s3, -c3]],[[-1, 0],[ 0, 1]],[[c3, -s3],[-s3, -c3]],
              [[-c3, s3],[-s3, -c3]],[[-c3, -s3],[s3, -c3]],[[-c3, s3],[-s3, -c3]],[[-c3, -s3],[s3, -c3]],
              [[-1, 0],[0, 1]],[[c3, -s3],[-s3, -c3]],[[c3, s3],[s3, -c3]],[[c3, s3],[s3, -c3]],[[-1, 0],[ 0, 1]],[[c3, -s3],[-s3, -c3]]]),
    "A1u" : np.array([ [[1]],[[-1]],[[-1]], # E, σh, i
               [[1]], [[1]], [[1]], [[1]], [[1]], # Cns
               [[1]], [[1]], [[1]], [[1]], [[1]], [[1]], # C2s
              [[-1]],[[-1]],[[-1]],[[-1]], # Sns
              [[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]]]), # σs
    "A2u" : np.array([ [[1]],[[-1]],[[-1]], # E, σh, i
               [[1]], [[1]], [[1]], [[1]], [[1]], # Cns
              [[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]], # C2s
              [[-1]],[[-1]],[[-1]],[[-1]], # Sns
               [[1]], [[1]], [[1]], [[1]], [[1]], [[1]]]), # σs
    "B1u" : np.array([ [[1]], [[1]],[[-1]],   # E, σh, i
              [[-1]], [[1]],[[-1]], [[1]],[[-1]], # Cns
               [[1]], [[1]], [[1]],[[-1]],[[-1]],[[-1]], # C2s
              [[-1]], [[1]], [[1]],[[-1]], # Sns
               [[1]], [[1]], [[1]],[[-1]],[[-1]],[[-1]]]), # σs
    "B2u" : np.array([ [[1]], [[1]],[[-1]], # E, σh, i
              [[-1]], [[1]],[[-1]], [[1]],[[-1]], # Cns
              [[-1]],[[-1]],[[-1]], [[1]], [[1]], [[1]], # C2s
              [[-1]], [[1]], [[1]],[[-1]], # Sns
              [[-1]],[[-1]],[[-1]], [[1]], [[1]], [[1]]]), # σs
    "E1u" : np.array([[[1, 0],[0, 1]],[[1, 0],[0, 1]],[[-1, 0],[0, -1]],
              [[c3, -s3],[s3, c3]],[[-c3, -s3],[s3, -c3]],[[-1, 0],[0, -1]],[[-c3, s3],[-s3, -c3]],[[c3, s3],[-s3, c3]],
              [[1, 0],[0, -1]],[[-c3, s3],[s3, c3]],[[-c3, -s3],[-s3, c3]],[[c3, s3],[s3, -c3]],[[-1, 0],[0, 1]],[[c3, -s3],[-s3, -c3]],
              [[c3, -s3],[s3, c3]],[[-c3, -s3],[s3, -c3]],[[-c3, s3],[-s3, -c3]],[[c3, s3],[-s3, c3]],
              [[1, 0],[0, -1]],[[-c3, s3],[s3, c3]],[[-c3, -s3],[-s3, c3]],[[c3, s3],[s3, -c3]],[[-1, 0],[0, 1]],[[c3, -s3],[-s3, -c3]]]),
    "E2u" : np.array([[[1, 0],[0, 1]],[[-1, 0],[0, -1]],[[-1, 0],[0, -1]],
              [[-c3, s3],[-s3, -c3]],[[-c3, -s3],[s3, -c3]],[[1, 0],[0, 1]],[[-c3, s3],[-s3, -c3]],[[-c3, -s3],[s3, -c3]],
              [[-1, 0],[0, 1]],[[c3, -s3],[-s3, -c3]],[[c3, s3],[s3, -c3]],[[c3, s3],[s3, -c3]],[[-1, 0],[ 0, 1]],[[c3, -s3],[-s3, -c3]],
              [[c3, -s3],[s3, c3]],[[c3, s3],[-s3, c3]],[[c3, -s3],[s3, c3]],[[c3, s3],[-s3, c3]],
              [[1, 0],[0, -1]],[[-c3, s3],[s3, c3]],[[-c3, -s3],[-s3, c3]],[[-c3, -s3],[-s3, c3]],[[1, 0],[ 0, -1]],[[-c3, s3],[s3, c3]]])
}
irrm_D8h = {
    "A1g" : np.array([[[1]],[[1]],[[1]], # E, σh, i
              [[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]], # C8s
              [[1]],[[1]],[[1]],[[1]], # C2'
              [[1]],[[1]],[[1]],[[1]], # C2''
              [[1]],[[1]],[[1]],[[1]],[[1]],[[1]], # S8
              [[1]],[[1]],[[1]],[[1]], # σvs
              [[1]],[[1]],[[1]],[[1]]]), # σds
    "A2g" : np.array([[[1]],[[1]],[[1]],
              [[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],
              [[-1]],[[-1]],[[-1]],[[-1]],
              [[-1]],[[-1]],[[-1]],[[-1]],
              [[1]],[[1]], [[1]],[[1]],[[1]],[[1]],
              [[-1]],[[-1]],[[-1]],[[-1]],
              [[-1]],[[-1]],[[-1]],[[-1]]]),
    "B1g" : np.array([[[1]],[[1]],[[1]],
              [[-1]],[[1]],[[-1]],[[1]],[[-1]],[[1]],[[-1]],
              [[1]],[[1]],[[1]],[[1]],
              [[-1]],[[-1]],[[-1]],[[-1]],
              [[-1]],[[1]],[[-1]],[[-1]],[[1]],[[-1]],
              [[1]],[[1]],[[1]],[[1]],
              [[-1]],[[-1]],[[-1]],[[-1]]]),
    "B2g" : np.array([[[1]],[[1]],[[1]],
              [[-1]],[[1]],[[-1]],[[1]],[[-1]],[[1]],[[-1]],
              [[-1]],[[-1]],[[-1]],[[-1]],
              [[1]],[[1]],[[1]],[[1]],
              [[-1]],[[1]],[[-1]],[[-1]],[[1]],[[-1]],
              [[-1]],[[-1]],[[-1]],[[-1]],
              [[1]],[[1]],[[1]],[[1]]]),
    "E1g" : np.array([[[1, 0],[0, 1]],[[-1, 0],[0, -1]],[[1, 0],[0, 1]],
              [[c4, -s4],[s4, c4]],[[0, -1],[1, 0]],[[-c4, -s4],[s4, -c4]],[[-1, 0],[0, -1]],[[-c4, s4],[-s4, -c4]],[[0, 1],[-1, 0]],[[c4, s4]],[[-s4, c4]],
              [[1, 0],[0, -1]],[[0, 1],[1, 0]],[[-1, 0],[0, 1]],[[0, -1],[-1, 0]],
              [[c4, s4],[s4, -c4]],[[-c4, s4],[s4, c4]],[[-c4, -s4],[-s4, c4]],[[c4, -s4],[-s4, -c4]],
              [[-c4, s4],[-s4, -c4]],[[0, 1],[-1, 0]],[[c4, s4],[-s4, c4]],[[c4, -s4],[s4, c4]],[[0, -1],[1, 0]],[[-c4, -s4],[s4, -c4]],
              [[-1, 0],[0, 1]],[[0, -1],[-1, 0]],[[1, 0],[0, -1]],[[0, 1],[1, 0]],
              [[-c4, -s4],[-s4, c4]],[[c4, -s4],[-s4, -c4]],[[c4, s4],[s4, -c4]],[[-c4, s4],[s4, c4]]]),
    "E2g" : np.array([[[1, 0],[0, 1]],[[1, 0],[0, 1]],[[1, 0],[0, 1]],
              [[0, -1],[1, 0]],[[-1, 0],[0, -1]],[[0, 1],[-1, 0]],[[1, 0],[0, 1]],[[0, -1],[1, 0]],[[-1, 0],[0, -1]],[[0, 1],[-1, 0]],
              [[1, 0],[0, -1]],[[-1, 0],[0, 1]],[[1, 0],[0, -1]],[[-1, 0],[0, 1]],
              [[0, 1],[1, 0]],[[0, -1],[-1, 0]],[[0, 1],[1, 0]],[[0, -1],[-1, 0]],
              [[0, -1],[1, 0]],[[-1, 0],[0, -1]],[[0, 1],[-1, 0]],[[0 ,-1],[1, 0]],[[-1, 0],[0, -1]],[[0, 1],[-1, 0]],
              [[1, 0],[0 ,-1]],[[-1, 0],[0, 1]],[[1, 0],[0, -1]],[[-1, 0],[0, 1]],
              [[0, 1],[1, 0]],[[0, -1],[-1, 0]],[[0, 1],[1, 0]],[[0, -1],[-1, 0]]]),
    "E3g" : np.array([[[1, 0],[0, 1]],[[-1, 0],[0, -1]],[[1, 0],[0, 1]],
              [[-c4, s4],[-s4, -c4]],[[0, -1],[1, 0]],[[c4, s4],[-s4, c4]],[[-1, 0],[0, -1]],[[c4, -s4],[s4, c4]],[[0, 1],[-1, 0]],[[-c4, -s4],[s4, -c4]],
              [[-1, 0],[0, 1]],[[0, -1],[-1, 0]],[[1, 0],[0, -1]],[[0, 1],[1, 0]],
              [[c4, s4],[s4, -c4]],[[-c4, s4],[s4, c4]],[[-c4, -s4],[-s4, c4]],[[c4, -s4],[-s4, -c4]],
              [[c4, -s4],[s4, c4]],[[0, 1],[-1, 0]],[[-c4, -s4],[s4, -c4]],[[-c4, s4],[-s4, -c4]],[[0, -1],[1, 0]],[[c4, s4],[-s4, c4]],
              [[1, 0],[0, -1]],[[0, 1],[1, 0]],[[-1, 0],[0, 1]],[[0, -1],[-1, 0]],
              [[-c4, -s4],[-s4, c4]],[[c4, -s4],[-s4, -c4]],[[c4, s4],[s4, -c4]],[[-c4, s4],[s4, c4]]]),
    "A1u" : np.array([[[1]],[[-1]],[[-1]], # E, σh, i
              [[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]], # C8s
              [[1]],[[1]],[[1]],[[1]], # C2'
              [[1]],[[1]],[[1]],[[1]], # C2''
              [[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]], # S8
              [[-1]],[[-1]],[[-1]],[[-1]], # σvs
              [[-1]],[[-1]],[[-1]],[[-1]]]), # σds
    "A2u" : np.array([[[1]],[[-1]],[[-1]],
              [[1]],[[1]],[[1]],[[1]],[[1]],[[1]],[[1]],
              [[-1]],[[-1]],[[-1]],[[-1]],
              [[-1]],[[-1]],[[-1]],[[-1]],
              [[-1]],[[-1]],[[-1]],[[-1]],[[-1]],[[-1]],
              [[1]],[[1]],[[1]],[[1]],
              [[1]],[[1]],[[1]],[[1]]]),
    "B1u" : np.array([[[1]],[[-1]],[[-1]],
              [[-1]],[[1]],[[-1]],[[1]],[[-1]],[[1]],[[-1]],
              [[1]],[[1]],[[1]],[[1]],
              [[-1]],[[-1]],[[-1]],[[-1]],
              [[1]],[[-1]], [[1]],[[1]],[[-1]],[[1]],
              [[-1]],[[-1]],[[-1]],[[-1]],
              [[1]],[[1]],[[1]],[[1]]]),
    "B2u" : np.array([[[1]],[[-1]],[[-1]],
              [[-1]],[[1]],[[-1]],[[1]],[[-1]],[[1]],[[-1]],
              [[-1]],[[-1]],[[-1]],[[-1]],
              [[1]],[[1]],[[1]],[[1]],
              [[1]],[[-1]],[[1]],[[1]],[[-1]],[[1]],
              [[1]],[[1]],[[1]],[[1]],
              [[-1]],[[-1]],[[-1]],[[-1]]]),
    "E1u" : np.array([[[1, 0],[0, 1]],[[1, 0],[0, 1]],[[-1, 0],[0, -1]],
              [[c4, -s4],[s4, c4]],[[0, -1],[1, 0]],[[-c4, -s4],[s4, -c4]],[[-1, 0],[0, -1]],[[-c4, s4],[-s4, -c4]],[[0, 1],[-1, 0]],[[c4, s4]],[[-s4, c4]],
              [[1, 0],[0, -1]],[[0, 1],[1, 0]],[[-1, 0],[0, 1]],[[0, -1],[-1, 0]],
              [[c4, s4],[s4, -c4]],[[-c4, s4],[s4, c4]],[[-c4, -s4],[-s4, c4]],[[c4, -s4],[-s4, -c4]],
              [[c4, -s4],[s4, c4]],[[0, -1],[1, 0]],[[-c4, -s4],[s4, -c4]],[[-c4, s4],[-s4, -c4]],[[0, 1],[-1, 0]],[[c4, s4],[-s4, c4]],
              [[1, 0],[0, -1]],[[0 ,1],[1, 0]],[[-1, 0],[0, 1]],[[0, -1],[-1, 0]],
              [[c4, s4],[s4, -c4]],[[-c4, s4],[s4, c4]],[[-c4, -s4],[-s4, c4]],[[c4, -s4],[-s4, -c4]]]),
    "E2u" : np.array([[[1, 0],[0, 1]],[[-1 ,0],[0 ,-1]],[[-1, 0],[0 ,-1]],
              [[0, -1],[1, 0]],[[-1, 0],[0, -1]],[[0, 1],[-1, 0]],[[1, 0],[0, 1]],[[0, -1],[1, 0]],[[-1, 0],[0, -1]],[[0, 1],[-1, 0]],
              [[1, 0],[0 -1]],[[-1, 0],[0, 1]],[[1, 0],[0, -1]],[[-1, 0],[0, 1]],
              [[0, 1],[1, 0]],[[0, -1],[-1, 0]],[[0, 1],[1, 0]],[[0, -1],[-1, 0]],
              [[0, 1],[-1, 0]],[[1, 0],[0, 1]],[[0, -1],[1, 0]],[[0, 1],[-1, 0]],[[1, 0],[0, 1]],[[0, -1],[1, 0]],
              [[-1, 0],[0, 1]],[[1, 0],[0, -1]],[[-1, 0],[0, 1]],[[1, 0],[0, -1]],
              [[0, -1],[-1, 0]],[[0, 1],[1, 0]],[[0, -1],[-1, 0]],[[0, 1],[1, 0]]]),
    "E3u" : np.array([[[1, 0],[0, 1]],[[1, 0],[0, 1]],[[-1, 0],[0, -1]],
              [[-c4, s4],[-s4, -c4]],[[0, -1],[1, 0]],[[c4, s4],[-s4, c4]],[[-1, 0],[0, -1]],[[c4, -s4],[s4, c4]],[[0, 1],[-1, 0]],[[-c4, -s4],[s4, -c4]],
              [[-1, 0],[0, 1]],[[0 ,-1],[-1, 0]],[[1, 0],[0, -1]],[[0, 1],[1, 0]],
              [[c4, s4],[s4, -c4]],[[-c4, s4],[s4, c4]],[[-c4, -s4],[-s4, c4]],[[c4, -s4],[-s4, -c4]],
              [[-c4, s4],[-s4, -c4]],[[0, -1],[1, 0]],[[c4, s4],[-s4, c4]],[[c4, -s4],[s4, c4]],[[0, 1],[-1, 0]],[[-c4, -s4],[s4, -c4]],
              [[-1, 0],[0, 1]],[[0, -1],[-1, 0]],[[1, 0],[0, -1]],[[0, 1],[1, 0]],
              [[c4, s4],[s4, -c4]],[[-c4, s4],[s4, c4]],[[-c4, -s4],[-s4, c4]],[[c4, -s4],[-s4, -c4]]])
}