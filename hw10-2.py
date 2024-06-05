import numpy as np
import matplotlib.pyplot as plt
import scipy


np.random.seed(30)


def f(x):
    return x**2


a = 0
b = 2


def monte_carlo_integrate(func, a, b, n):
    vals = np.random.uniform(a, b, n)
    y = [func(val) for val in vals]

    y_mean = np.sum(y)/n
    integ = (b-a) * y_mean

    return integ


scipy_quad_result = scipy.integrate.quad(f, a, b)[0]
print("Значення інтегралу обличлено scipy.integrate.quad:", scipy_quad_result)
print()


for n in [100, 1000, 10000, 100000]:
    monte_carlo_result = monte_carlo_integrate(f, a, b, n)
    print(f"Значення інтегралу методом Монте Карло n={n}:", monte_carlo_result)
    diff = abs(scipy_quad_result - monte_carlo_result)
    print("Різниця результатів:", diff, "або",
          round(diff/scipy_quad_result*100, 3), "%")
    print()


def make_plot():
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' +
                 str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()
