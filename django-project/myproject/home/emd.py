from cv2 import *


def calc_histogram(src):
    # Convert to HSV
    hsv = cv.CreateImage(cv.GetSize(src), 8, 3)
    cv.CvtColor(src, hsv, cv.CV_BGR2HSV)

    # Extract the H and S planes
    size = cv.GetSize(src)
    h_plane = cv.CreateMat(size[1], size[0], cv.CV_8UC1)
    s_plane = cv.CreateMat(size[1], size[0], cv.CV_8UC1)
    cv.Split(hsv, h_plane, s_plane, None, None)
    planes = [h_plane, s_plane]

    #Define numer of bins
    h_bins = 30
    s_bins = 32

    #Define histogram size
    hist_size = [h_bins, s_bins]

    # hue varies from 0 (~0 deg red) to 180 (~360 deg red again */
    h_ranges = [0, 180]

    # saturation varies from 0 (black-gray-white) to 255 (pure spectrum color)
    s_ranges = [0, 255]

    ranges = [h_ranges, s_ranges]

    #Create histogram
    hist = cv.CreateHist([h_bins, s_bins], cv.CV_HIST_ARRAY, ranges, 1)

    #Calc histogram
    cv.CalcHist([cv.GetImage(i) for i in planes], hist)

    cv.NormalizeHist(hist, 1.0)

    #Return histogram
    return hist


def calc_em(hist_1, hist_2, h_bins, s_bins):
    #Define number of rows
    num_rows = h_bins * s_bins
    sig1 = cv.CreateMat(num_rows, 3, cv.CV_32FC1)
    sig2 = cv.CreateMat(num_rows, 3, cv.CV_32FC1)

    for h in range(h_bins):
        for s in range(s_bins):
            bin_val = cv.QueryHistValue_2D(hist_1, h, s)
            cv.Set2D(sig1, h * s_bins + s, 0, cv.Scalar(bin_val))
            cv.Set2D(sig1, h * s_bins + s, 1, cv.Scalar(h))
            cv.Set2D(sig1, h * s_bins + s, 2, cv.Scalar(s))

            bin_val = cv.QueryHistValue_2D(hist_2, h, s)
            cv.Set2D(sig2, h * s_bins + s, 0, cv.Scalar(bin_val))
            cv.Set2D(sig2, h * s_bins + s, 1, cv.Scalar(h))
            cv.Set2D(sig2, h * s_bins + s, 2, cv.Scalar(s))

    #This is the important line were the OpenCV EM algorithm is called
    return cv.CalcEMD2(sig1, sig2, cv.CV_DIST_L2)


def compare_images(src, dest):
    #Load image 1
    src1 = cv.LoadImage(src)

    #Load image 1
    src2 = cv.LoadImage(dest)

    # Get histograms
    hist1 = calc_histogram(src1)
    hist2 = calc_histogram(src2)

    # Compare histograms using earth mover's
    hist_comp = calc_em(hist1, hist2, 30, 32)

    #Print solution
    #print(hist_comp)

    return hist_comp


if __name__ == "__main__":
    pass
