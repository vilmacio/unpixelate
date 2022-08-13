import gaussian
import shape
import lut

def apply(image, weight = 6, output_scale = 800):

    hr_image = shape.resize(image)

    image_smothing = gaussian.apply(hr_image, weight)

    lut_result = lut.apply(image_smothing)

    result = shape.resize(lut_result, output_scale)

    return result