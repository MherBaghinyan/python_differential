from project_files.multy_parametric.multiparametric import *


def _multi_differential(item, t_level, d_level, t_value, d_value):
    "returns a differential of given matrix"

    z_matrix = [[0] * t_level for x in range(d_level)]
    for i in range(0, t_level):
        for j in range(0, d_level):
                z_matrix[i][j] = item_multi_transform(item, i, j, t_value, d_value)
    return z_matrix


# get division image value
def get_div_image_(k1_value, k2_value, image_x, image_y):
    item = 0

    y_k_0 = image_y[0][0]
    x_k_0 = image_x[0][0]

    if k1_value == 0 and k2_value == 0:
        return x_k_0 / y_k_0

    # if k1_value == 0 and k2_value != 0:
    #     for p2 in range(1, k2_value + 1):
    #         item += get_div_image_(0, k2_value - p2, image_x, image_y) * image_y[0][p2]
    #     return (image_x[0][k2_value] - item) / y_k_0
    #
    # if k1_value != 0 and k2_value == 0:
    #     for p1 in range(1, k1_value + 1):
    #         item += get_div_image_(k1_value - p1, 0, image_x, image_y) * image_y[p1][0]
    #     return (image_x[k1_value][0] - item) / y_k_0

    for p1 in range(0, k1_value + 1):
        for p2 in range(0, k2_value + 1):
            if p1 != p2 != 0:
                item += get_div_image_(k1_value - p1, k2_value - p2, image_x, image_y) * image_y[p1][p2]

    return (image_x[k1_value][k2_value] - item) / y_k_0


function_x = 7*d + t + 3
function_y = t**2 - d + 1

div_finction = function_x / function_y
print(div_finction)

k1_value = 2
k2_value = 2
t_value = 0
d_value = 0

# image_x = _multi_differential(function_x, k1_value + 1, k2_value + 1, t_value, d_value)
# image_y = _multi_differential(function_y, k1_value + 1, k2_value + 1, t_value, d_value)
#
# print(image_x)
# print(image_y)
#
# z_image = 0
# z_images_matrix = [[0] * (k1_value + 1) for x in range((k2_value + 1))]
#
# for k1 in range(0, k1_value + 1):
#     for k2 in range(0, k2_value + 1):
#         z_images_matrix[k1][k2] = get_div_image_(k1, k2, image_x, image_y)
#         z_image += z_images_matrix[k1][k2] * ((t-t_value)**k1)*((d-d_value)**k2)
#
# print("----------------")
# print(z_images_matrix)
# print("----------------")
# print("z_image = ", z_image)
