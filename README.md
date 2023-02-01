# Draw a rectangle with Gradient Color using OpenCV
### Example
```python
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
```

### Parameters
* **frame**: The image would be display(numpy type).
* **BGR_Channel**: The gradient color chart(BGR Channel).
* **rectangle_position**: The position of rectangle.
* **rotate**: The direction of gradient.

## Image
![GITHUB]( https://github.com/jerryhouuu/Draw-Gradient-Alpha-Rectangle-using-openCV/blob/master/imgs/example1.jpg "rotate: 0")
**rotate: 0** 
![GITHUB]( https://github.com/jerryhouuu/Draw-Gradient-Alpha-Rectangle-using-openCV/blob/master/imgs/example2.jpg "rotate: 1")
**rotate: 1** 
![GITHUB]( https://github.com/jerryhouuu/Draw-Gradient-Alpha-Rectangle-using-openCV/blob/master/imgs/example3.jpg "rotate: 2")
**rotate: 2** 
![GITHUB]( https://github.com/jerryhouuu/Draw-Gradient-Alpha-Rectangle-using-openCV/blob/master/imgs/example4.jpg "rotate: 3")
**rotate: 3** 
