import operator


class Polynomial(object):
    # constructor

    def __init__(self, coeffs):
        if isinstance(coeffs, Polynomial):
            self.coeffs = coeffs.coeffs[:]
        if not isinstance(coeffs, list):
            raise TypeError("Coeffs list or constant")
        if len(coeffs) == 0:
            raise TypeError("Coeffs list empty")
        if all(isinstance(c, (int, float)) for c in coeffs):
            pass
        else:
            raise TypeError("Coeffs list values(int or float)")
        large_degree = next((i for i, c in enumerate(coeffs) if c != 0), -1)
        self.coeffs = coeffs[large_degree:]

    @property
    def degree(self):
        return len(self.coeffs) - 1

    # p2 + p1
    def __radd__(self, argument):
        return self + argument

    # p1+p2
    def __add__(self, argument):
        if isinstance(argument, Polynomial):
            if self.degree > argument.degree:
                a1 = self.coeffs
                a2 = [0] * (self.degree - argument.degree) + argument.coeffs
            elif argument.degree > self.degree:
                a1 = [0] * (argument.degree - self.degree) + self.coeffs
                a2 = argument.coeffs
            else:
                a1 = self.coeffs
                a2 = argument.coeffs
            return Polynomial(list(map(operator.add, a1, a2)))
        elif isinstance(argument, (int, float)):
            result = Polynomial(self.coeffs)
            result.coeffs[-1] += argument
            return result
        else:
            raise TypeError("int or false p1+p2")

    # -p
    def __neg__(self):
        return Polynomial([-coeff for coeff in self.coeffs])

    # p1 - p2
    def __sub__(self, argument):
        if isinstance(argument, (int, float, Polynomial)):
            return self.__add__(-argument)
        else:
            raise TypeError('Coeffs list values(int or float)', argument)

    # p2 - p1
    def __rsub__(self, argument):
        if isinstance(argument, (int, float, Polynomial)):
            return (self.__neg__()).__add__(argument)
        else:
            raise TypeError('Coeffs list values(int or float)', argument)

    # p1 == p2
    def __eq__(self, argument):
        if isinstance(argument, (int, float)):
            if len(self.coeffs) == 1:
                return self.coeffs[0] == argument
            else:
                return False
        elif isinstance(argument, Polynomial):
            return self.coeffs == argument.coeffs
        else:
            raise TypeError("p1==p2")

    # p1!=p2
    def __ne__(self, argument):
        return not self == argument

    # p1 * p2
    def __mul__(self, argument):
        if isinstance(argument, Polynomial):
            result = [0] * (self.degree + argument.degree + 1)
            for i, self_coef in enumerate(self.coeffs):
                for j, other_coef in enumerate(argument.coeffs):
                    result[i + j] += self_coef * other_coef
            return Polynomial(result)
        elif isinstance(argument, (int, float)):
            result = Polynomial([coef * argument for coef in self.coeffs])
            return result
        else:
            raise TypeError("polynomial* polynomial and int or float constant")

    # p2 * p1
    def __rmul__(self, argument):
        return self * argument

    # return str
    def __str__(self):
        result = []
        for power, coeff in enumerate(self.coeffs):
            if coeff:
                if power == 0:
                    if len(self.coeffs) > 2:
                        power = 'x' + str(len(self.coeffs) - 1 - power)
                        if abs(coeff) != 1:
                            result.append(('-' + str(abs(coeff)) if coeff < 0 else '' + str(coeff)) + power)
                        else:
                            result.append(('-' if coeff < 0 else '') + power)
                    elif len(self.coeffs) == 2:
                        power = 'x'
                        if abs(coeff) != 1:
                            result.append(('-' + str(abs(coeff)) if coeff < 0 else '' + str(coeff)) + power)
                        else:
                            result.append(('-' if coeff < 0 else '') + power)
                    elif len(self.coeffs) == 1:
                        power = ''
                        result.append(('-' + str(abs(coeff)) if coeff < 0 else '' + str(coeff)) + power)
                elif power == len(self.coeffs) - 2:
                    power = 'x'
                    if abs(coeff) != 1:
                        result.append(('-' + str(abs(coeff)) if coeff < 0 else '+' + str(coeff)) + power)
                    else:
                        result.append(('-' if coeff < 0 else '+') + power)
                elif power == len(self.coeffs) - 1:
                    power = ''
                    result.append(('-' + str(abs(coeff)) if coeff < 0 else '+' + str(coeff)) + power)
                else:
                    power = 'x' + str(len(self.coeffs) - 1 - power)
                    if abs(coeff) != 1:
                        result.append(('-' + str(abs(coeff)) if coeff < 0 else '+' + str(coeff)) + power)
                    else:
                        result.append(('-' if coeff < 0 else '+') + power)
        if result:
            return ''.join(result)
        else:
            return "0"
