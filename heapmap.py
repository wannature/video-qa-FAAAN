from keras.models import *
from keras.callbacks import *
import keras.backend as K
from model import *
from data import *
import cv2
import argparse


def visualize_class_activation_map(model_path, img_path, output_path):
	model = load_model(model_path)
	original_img = cv2.imread(img_path, 1)
	width, height, _ = original_img.shape

	# Reshape to the network input shape (3, w, h).
	img = np.array([np.transpose(np.float32(original_img), (2, 0, 1))])

	# Get the 512 input weights to the softmax.
	class_weights = model.layers[-1].get_weights()[0]
	final_conv_layer = get_output_layer(model, "conv5_3")
	get_output = K.function([model.layers[0].input], [final_conv_layer.output, model.layers[-1].output])
	[conv_outputs, predictions] = get_output([img])
	conv_outputs = conv_outputs[0, :, :, :]

	# Create the class activation map.
	cam = np.zeros(dtype=np.float32, shape=conv_outputs.shape[1:3])
	for i, w in enumerate(class_weights[:, 1]):
		cam += w * conv_outputs[i, :, :]
	print
	"predictions", predictions
	cam /= np.max(cam)
	cam = cv2.resize(cam, (height, width))
	heatmap = cv2.applyColorMap(np.uint8(255 * cam), cv2.COLORMAP_JET)
	heatmap[np.where(cam < 0.2)] = 0
	img = heatmap * 0.5 + original_img
	cv2.imwrite(output_path, img)

if __name__ == '__main__':
	visualize_class_activation_map("","","")

