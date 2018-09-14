import numpy as np

def fspecial_gaussian(shape, sigma):
	''' MATLAB-mimicking implementation from GitHub:
	    https://stackoverflow.com/questions/17190649/
	        how-to-obtain-a-gaussian-filter-in-python '''
	m,n = [(ss-1)/2 for ss in shape]
	y,x = np.ogrid[-m:m+1, -n:n+1]
	h = np.exp( -(x*x + y*y) / (2*sigma*sigma) )
	h[h < np.finfo(h.dtype).eps*h.max()] = 0
	sumh = h.sum()
	if sumh != 0:
		h /= sumh
	return(h)


def get_density_map_gaussian(image_data, annotation_data, is_verbose=False):
	''' Python implementation of the method in the repo '''
	h, w = image_data.shape[:2]
	image_density = np.zeros((h, w))
	n_annotations = annotation_data.shape[0]
	H = fspecial_gaussian(shape=(15, 15), sigma=4.0)

	if n_annotations == 0:
		return(image_density)
	if n_annotations == 1:
		x = max(0, min(w - 1, int(np.round(annotation_data[0, 0]))))
		y = max(0, min(h - 1, int(np.round(annotation_data[0, 1]))))
		image_density[y, x] = 255
		return(image_density)

	for k in range(annotation_data.shape[0]):
		x = max(0, min(w - 1, int(np.round(annotation_data[k, 0]))))
		y = max(0, min(h - 1, int(np.round(annotation_data[k, 1]))))
		x1 = x - 7
		x2 = x + 7
		y1 = y - 7
		y2 = y + 7

		dfx1, dfy1, dfx2, dfy2 = (0, 0, 0, 0)
		change_H = False
		if x1 < 0:
			dfx1 = np.abs(x1)
			x1 = 0
			change_H = True
		if y1 < 0:
			dfy1 = np.abs(y1)
			y1 = 0
			change_H = True
		if x2 >= w:
			dfx2 = x2 - w + 1
			x2 = w - 1
			change_H = True
		if y2 >= h:
			dfy2 = y2 - h + 1
			y2 = h - 1
			change_H = True
		if is_verbose:
			print('w: {}, h: {}'.format(w, h))
			print('x1: {}, x2: {}, y1: {}, y2: {}'.format(x1, x2, y1, y2))
			print('dfx1: {}, dfx2: {}, dfy1: {}, dfy2: {}'.format(
				dfx1, dfx2, dfy1, dfy2))
		H_mod = fspecial_gaussian(
			shape=(15 - (dfy1 + dfy2), 15 - (dfx1 + dfx2)),
			sigma=4.0) if change_H else H
		image_density[y1:y2+1, x1:x2+1] += H_mod
	return(image_density)

