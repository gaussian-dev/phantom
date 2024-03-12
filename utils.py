import numpy as np

def cast_f32_to_modq(v: np.float32, q: np.uint32):
    '''
    Rounds floating point value v and casts to unsigned representation modulus q

    Panics: 
    |v| > q/2
    '''
    assert abs(v.round()).astype(np.uint32) < (q << 1)

    v = v.round()
    if v < 0:
        return q - abs(v.round()).astype(np.uint32)
    else:
        return v.round().astype(np.uint32)
