import numpy as np
from scipy.integrate import odeint

def hydro_model(L, nx, T, dt, R):
    dx = L / (nx - 1)
    x = np.linspace(0, L, nx)
    g = 9.81
    h0 = 1.0
    u0 = 0.0
    y0 = np.zeros(2 * nx)
    y0[:nx] = h0
    y0[nx:] = u0

    def rhs(y, t):
        h = y[:nx]
        u = y[nx:]
        dydt = np.zeros_like(y)

        # Rainfall Condition
        rain = R if t <= 10 else 0.0
        
        u[0] = 0.0
        u[-1] = 0.0
        
        dydt[:nx] = -u * (np.roll(h, -1) - np.roll(h, 1)) / (2 * dx) + rain
        dydt[nx:] = -g * (np.roll(h, -1) - np.roll(h, 1)) / (2 * dx) - u * (np.roll(u, -1) - np.roll(u, 1)) / (2 * dx)
        
        return dydt

    t = np.arange(0, T, dt)
    y = odeint(rhs, y0, t)
    h = y[:, :nx]
    
    return x, t, h
