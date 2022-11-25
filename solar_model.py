# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def sign(x):
    """Определяет знак числа"""
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        else:
            r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
            tan = (body.y - obj.y) / (body.x - obj.x)
            cos = (1 / (tan ** 2 + 1)) ** (1 / 2)
            sin = (1 - cos ** 2) ** (1 / 2)
            print("cos ", cos, "sin", sin)
            body.Fx = sign(
                obj.x - body.x) * gravitational_constant * body.m * obj.m / r ** 2 * cos
            body.Fy = sign(
                obj.y - body.y) * gravitational_constant * body.m * obj.m / r ** 2 * sin


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    print(body.Vx, body.Vy)
    print(body.x, body.y)
    ax = body.Fx / body.m
    ay = body.Fy / body.m
    print(ax, ay)
    body.x += body.Vx
    body.y += body.Vy
    body.Vx += ax * dt
    body.Vy += ay * dt
    # FIXME: not done recalculation of y coordinate!


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
