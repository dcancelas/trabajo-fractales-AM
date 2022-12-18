# Análisis Matemático: Trabajo fractales

`f = z**2 - 0.59255 * z**-1`

### Método de Newton

`g = z - f / derf`

![](https://raw.githubusercontent.com/dcancelas/trabajo-fractales-AM/master/fractal_Newton.png)

### Método de Halley

`g = z - (2 * f * derf) / (2 * derf**2 - f * der2f)`

![](https://raw.githubusercontent.com/dcancelas/trabajo-fractales-AM/master/fractal_Halley.png)

### Método de Chebyshev

`g = z - (1 + (f * der2f / derf**2) / 2) * (f / derf)`

![](https://raw.githubusercontent.com/dcancelas/trabajo-fractales-AM/master/fractal_Chebyshev.png)

## Bibliografía

*   Julia set of z^2 - 0.59255z^-1 (<http://usefuljs.net/fractals/docs/rational_maps.html>)

