import random
import numpy as np

def predict(seed):
    random.seed(seed)
    return {
		'number': np.float32(random.random())
	}
