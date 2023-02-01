import cv2
import numpy as np

def draw_gradient_alpha_rectangle(frame, BGR_Channel, rectangle_position, rotate):
    (xMin, yMin), (xMax, yMax) = rectangle_position
    height = yMax - yMin
    width = xMax - xMin
    color = np.array(BGR_Channel, np.uint8)[np.newaxis, :]
    if rotate == 1 or rotate == 3:
        mask1 = np.rot90(np.repeat(np.tile(np.linspace(1, 0, height), (width, 1))[:, :, np.newaxis], 3, axis=2), rotate)
    elif rotate == 0 or rotate == 2:
        mask1 = np.rot90(np.repeat(np.tile(np.linspace(1, 0, width), (height, 1))[:, :, np.newaxis], 3, axis=2), rotate)
    else:
        raise Exception(f"invalid rotation value (expected int 0-3): {rotate}")
    frame[yMin:yMax, xMin:xMax, :] = mask1 * frame[yMin:yMax, xMin:xMax, :] + (1-mask1) * color

    return frame

def main():
    frame = np.zeros((300, 300, 3), np.uint8)
    frame[:,:,:] = 255

    frame = draw_gradient_alpha_rectangle(frame, (42, 175, 121), ((0, 0), (300, 300)), 3)

    cv2.imshow('frame', frame)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
