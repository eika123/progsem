from pylab import *


# models for drag force, density, viscosity, pressure, temperature

def dynamic_viscosity(Tc):
    # model from 
    # https://onlinelibrary.wiley.com/doi/pdf/10.1002/9780470516430.app2

    # usable for Tk between 100 and 800  degrees kelvin
    #            Tc between -173 and 526 degrees centigrade

    Tk = Tc + 273.15
    mu  = 1.458E-6*(Tk**1.5)/(Tk + 110.4)
    return mu


def air_density(P, Tc):
    Tk = Tc - 273.15
    Ra = 287.05         #J/kg K
    rho = P/(Ra*Tk)
    return rho


def barometric_pressure_temperature_density(h):
    # implementation of barometric pressure model from wikipedia

    R = 8.3144598   # J/(mol K)
    g = 9.80665     # gravitational acceleration m/s**2
    M = 0.0289644   # molecular mass of air kg/mol


    def layer_values(h):
        hbs = [-610, 11000, 20000, 32000, 47000, 51000, 71000]
        Pbs = [108900, 22632.10, 5474.89, 868.02, 110.91, 66.94, 3.96]
        Tbs = [292.15, 216.65, 216.65, 228.65, 270.65, 270.65, 214.65] # kelvin
        Ls = [6.5, 0, -1, -2.8, 0, +2.8, +2.0]
        rhos = [1.2985, 0.36391, 0.01322, 0.00143, 0.00086, 0.000064]

        if h >= hbs[-1]:
            return hbs[-1], Pbs[-1], Tbs[-1], Ls[-1], rhos[-1]

        for i in range(len(hbs)):
            if hbs[i] - h > 0:
                hb, Pb, Tb, Lb, rho_b = hbs[i - 1], Pbs[i - 1], Tbs[i - 1], \
                                            Ls[i - 1], rhos[i - 1]
                return hb, Pb, Tb, Lb, rho_b
    
    hb, Pb, Tb, Lb, rho_b = layer_values(h)

    if Lb != 0:
        T_ratio = Tb/(Tb + Lb*(h - hb)/1000)

        P = Pb*T_ratio**(g*M/(R*Lb))
        rho = rho_b*T_ratio**(1 + g*M/(R*Lb))
    else:
        P = Pb*exp(-g*M*(h - hb)/(R*Tb))
        rho = (P/Pb)*rho_b

    # estimate temperature in centigrade from temperature lapse
    Tk = -(h - hb)*Lb/1000 + Tb
    Tc = Tk - 273.15

    return P, Tc, rho
        


def reynolds_number(rho, v, L, mu):
    Re = rho*abs(v)*L/mu
    return Re


def drag_force(T, v, h, rho, time_since_parachute_opened):

    # ad notam: rho model makes the vertical speed decrease linearly instead of being constant
    # at terminal velocity 

    if time_since_parachute_opened:
        D = 11 # diameter in meters of parachute
        L = D/2
        r = D/2
        parachute_coeff = min(time_since_parachute_opened/8.0, 1)
        A = max(parachute_coeff*pi*r**2, 1.5)
        mu = dynamic_viscosity(T) 
        Re = reynolds_number(rho, v, L, mu)
        if Re > 5.0E5:
            Cd = 0.15
        else:
            Cd = 0.2
        
        drag_force = 0.5*(rho*Cd*A)*v**2

    else:
        A = 1.5
        L = 4*1.1
        mu = dynamic_viscosity(T) 
        Re = reynolds_number(rho, v, L, mu)
        if Re > 5.0E5:
            s = 0.02
            Cd = s*log((Re - 5E5)/2E5 + 0.1*s) 
        else:
            s = 1.0*5E5
            Cd = 1.0*exp((5.0E5 - Re)/s)
        
        drag_force = 0.5*(rho*Cd*A)*v**2
    
    return drag_force, Re, mu


def simulate_fall(height, mass, dt=5E-3):

    def gravity(h):
        # model from https://en.wikipedia.org/wiki/Gravity_of_Earth#Altitude
        
        g0 = 9.80665    # gravitational constant    m/s**2 
        R = 6371.0088E3 # mean earth radius         m 
        return g0*(R/(R + h))**2

    # initial conditions
    v0 = 0                  # initial vertical velocity     m/s
    h0 = height             # from height h                 m
    

    # use second order accurate central difference scheme
    # (h(t + dt) - h(t - dt))/2dt = Df
    # h(t + dt) = h(t - dt) + 2dt*Df

    # storage
    v = [v0]
    h = [h0]
    t = [0]
    Reynolds_numbers = []
    dynamic_viscosity_values = []

    # make first timestep
    P, T, rho = barometric_pressure_temperature_density(h[0])
    G = gravity(h[0])*mass
    D, Re, mu = drag_force(T, v[-1], h[-1], rho, time_since_parachute_opened=0)
    sum_forces = D - G
    a = sum_forces/mass     # acceleration
    v_new = v0 + a*dt
    h_new = h0 + 0.5*v_new*dt


    v.append(v_new)
    h.append(h_new)
    t.append(dt)
    Reynolds_numbers.append(Re)
    Reynolds_numbers.append(Re)
    dynamic_viscosity_values.append(mu)
    dynamic_viscosity_values.append(mu)


    time_since_parachute_opened = 0
    while h[-1] > 0:

        if h[-1] < 2900:
            time_since_parachute_opened += dt

        #parachute = False

        # get atmospheric parameters
        P, T, rho = barometric_pressure_temperature_density(h[-1])

        #G = gravity(h[-1])*mass
        G = 9.81*mass
        D, Re, mu = drag_force(T, v[-1], abs(h[-1]), rho, time_since_parachute_opened=time_since_parachute_opened)

        #D = simple_drag_force(v[-1], parachute)
        sum_forces = D - G
        a = sum_forces/mass     # acceleration



        v_new = v[-1] + dt*a
        h_new = h[-1] + dt*v[-1]
        t_new = t[-1] + dt

        if abs(h[-1] - h[0]) < 1000:
            print(f't = {t_new:{9}.{6}},        v = {v_new:{9}.{2}},    h={h_new:{9}.{2}},      ' +\
                f'Re = {Re:{14}.{4}},      a = {a:{9}.{4}} ')

        v.append(v_new)
        h.append(h_new)
        t.append(t_new)
        #Reynolds_numbers.append(Re)
        #dynamic_viscosity_values.append(mu)
    
    #return h, v, Reynolds_numbers, t
    return h, v, t


    
def calculate_atmospheric_parameters():

    N = 32000
    h = linspace(0, 80000, N)
    P = zeros(N)
    T = zeros(N)
    rho = zeros(N)

    for i in range(N):
        P[i], T[i], rho[i] = barometric_pressure_temperature_density(h[i])


    temps = linspace(-100, 20, 12) 
    mu = zeros(len(temps))
    for i in range(len(temps)):
        mu[i] = dynamic_viscosity(temps[i])
        print(mu[i])

    return h, P, T, rho, temps, mu


def simple_drag_force(v, time_since_parachute_opened):
    if time_since_parachute_opened:
        k = 1*min(1, time_since_parachute_opened/8)
    else:
        k = 0.1
    return k*v**2


def plot_atmospheric_parameters():

    h, P, T, rho, temps, mu = calculate_atmospheric_parameters()

    plot(P, h)
    xlabel('Pressure')
    ylabel('altitude')
    grid()
    show()

    plot(T, h)
    grid()
    xlabel('Temperature')
    ylabel('altitude')
    show()


    plot(rho, h)
    grid()
    xlabel('density rho')
    ylabel('altitude')
    show()

    plot(temps, mu)
    grid()
    ylabel('viscosity mu')
    xlabel('temperature centigrade')
    show()


if __name__ == '__main__':
    from contextlib import closing
    import shelve

    from numpy import savetxt

    height = 80000
    mass = 30
    #h, v, Re, t = simulate_fall(height, mass, dt=1E-3)
    h, v, t = simulate_fall(height, mass, dt=1E-3)

    plot(t, h)
    xlabel('time [s]')
    ylabel('altitude [m]')
    grid()
    show()
    figure()

    """
    plot(t, Re)
    xlabel('time [s]')
    ylabel('Reynolds number')
    grid()
    show()
    """



    plot(t, v)
    xlabel('time [s]')
    ylabel('vertical speed [m]')
    grid()
    show()
    figure()



    """
    The open command generates a context manager, which is important for 
    handling external resources, such as files. In contrast to this command, 
    shelve.open does not create a context manager by itself. 
    The closing command from the contextlib module is needed to transform it 
    into an appropriate context manager. Consider the following example of restoring the file:
    """

    

    savetxt('jump_simulation_data_time_altitude.txt',[t, h] , delimiter=',', header='time, altitude')
    savetxt('jump_simulation_data_time_velocity.txt',[t, v] , delimiter=',', header='time, velocity')
