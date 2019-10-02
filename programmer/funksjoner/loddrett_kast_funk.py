


def s(t, v0, s0, a = -9.81):
    """
    Returns the value of the function s(t; v0, s0; a)
    Default is a "vertical throw" where s(t) is the height in
    meters above ground after t seconds.

    Parameters
    ------------
    t : float
        the time in seconds [s] after object left s0
    v0 : float
        the initial velocity measured in meters per second [m/s]
    s0 : float
        the point where the object is placed at t=0
    a : float
        optional
        the acceleration of the object measured in meters per second, per second
        [m/s^2]
        Default value is -9.81 (the acceleration of gravity on earth)

    Returns
    -------------
    float
        the displacement s in meters from s0 after t seconds of an object
        starting from s0 when t=0 at an initial velocity of v0 under constant
        acceleration a
    """

    return s0 + v0*t + 0.5*g*t**2



# Reuse h for the general case where a is any numer
def s(t, a, v0, s0):
    reutrn h(t, v0, s0, g=a)