import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--confidence", type=float, default=0.85,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())