import numpy as np


def gridgen(ib, ie, jb, je, nx, ny, xl, yl, zl):
    dx = xl / nx
    dy = yl / ny

    disw = np.zeros((nx, ny))
    dise = np.zeros((nx, ny))
    dinw = np.zeros((nx, ny))
    dine = np.zeros((nx, ny))
    djsw = np.zeros((nx, ny))
    djse = np.zeros((nx, ny))
    djnw = np.zeros((nx, ny))
    djne = np.zeros((nx, ny))
    answ = np.zeros((nx, ny))
    anse = np.zeros((nx, ny))
    annw = np.zeros((nx, ny))
    anne = np.zeros((nx, ny))
    aesw = np.zeros((nx, ny))
    aese = np.zeros((nx, ny))
    aenw = np.zeros((nx, ny))
    aene = np.zeros((nx, ny))
    vlsw = np.zeros((nx, ny))
    vlse = np.zeros((nx, ny))
    vlnw = np.zeros((nx, ny))
    vlne = np.zeros((nx, ny))
    xsw = np.zeros((nx, ny))
    ysw = np.zeros((nx, ny))
    xse = np.zeros((nx, ny))
    yse = np.zeros((nx, ny))
    xnw = np.zeros((nx, ny))
    ynw = np.zeros((nx, ny))
    xne = np.zeros((nx, ny))
    yne = np.zeros((nx, ny))

    xsw[0, 0] = -dx / 2.0
    ysw[0, 0] = -dy / 2.0
    xse[0, 0] = 0.0
    yse[0, 0] = -dy / 2.0
    xnw[0, 0] = -dx / 2.0
    ynw[0, 0] = 0.0
    xne[0, 0] = 0.0
    yne[0, 0] = 0.0

    for j in range(jb, je + 2):
        xsw[0, j] = xsw[0, j - 1]
        ysw[0, j] = ysw[0, j - 1] + dy
        xse[0, j] = xse[0, j - 1]
        yse[0, j] = yse[0, j - 1] + dy
        xnw[0, j] = xnw[0, j - 1]
        ynw[0, j] = ynw[0, j - 1] + dy
        xne[0, j] = xne[0, j - 1]
        yne[0, j] = yne[0, j - 1] + dy

    for j in range(jb - 1, je + 2):
        for i in range(ib, ie + 2):
            xsw[i, j] = xsw[i - 1, j] + dx
            ysw[i, j] = ysw[i - 1, j]
            xse[i, j] = xse[i - 1, j] + dx
            yse[i, j] = yse[i - 1, j]
            xnw[i, j] = xnw[i - 1, j] + dx
            ynw[i, j] = ynw[i - 1, j]
            xne[i, j] = xne[i - 1, j] + dx

    for j in range(jb - 1, je + 2):
        for i in range(ib - 1, ie + 2):
            disw[i, j] = 0.5 * dx
            dise[i, j] = 0.5 * dx
            dinw[i, j] = 0.5 * dx
            dine[i, j] = 0.5 * dx
            djsw[i, j] = 0.5 * dy
            djse[i, j] = 0.5 * dy
            djnw[i, j] = 0.5 * dy
            djne[i, j] = 0.5 * dy
            answ[i, j] = disw[i, j] * zl
            anse[i, j] = dise[i, j] * zl
            annw[i, j] = dinw[i, j] * zl
            anne[i, j] = dine[i, j] * zl
            aesw[i, j] = djsw[i, j] * zl
            aese[i, j] = djse[i, j] * zl
            aenw[i, j] = djnw[i, j] * zl
            aene[i, j] = djne[i, j] * zl
            vlsw[i, j] = disw[i, j] * djsw[i, j] * zl
            vlse[i, j] = dise[i, j] * djse[i, j] * zl
            vlnw[i, j] = dinw[i, j] * djnw[i, j] * zl
            vlne[i, j] = dine[i, j] * djne[i, j] * zl

    return dx, dy, disw, dise, dinw, dine, djsw, djse, djnw, djne, answ, anse, annw, anne, aesw, aese, aenw, aene, vlsw, vlse, vlnw, vlne, xsw, ysw, xse, yse, xnw, ynw, xne, yne
