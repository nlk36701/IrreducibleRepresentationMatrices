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


irrm_C3v = {
        "A1" : np.array([[[1]],[[1]],[[1]],[[1]], [[1 ]],[[1 ]]]),
        "A2" : np.array([[[1]],[[1]],[[1]],[[-1]],[[-1]],[[-1]]]),
        "E"  : np.array([[[1, 0],[0, 1]], [[-c3, -s3],[ s3, -c3]], [[-c3, s3],[ -s3, -c3]], [[1, 0],[0, -1]], [[-c3, -s3],[ -s3, c3]], [[-c3, s3],[ s3, c3]]])
    }
