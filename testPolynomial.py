from unittest import TestCase, main
from Polynomial import Polynomial


class testPolynomial(TestCase):
    # -----------init tests ------------
    def test_init_correct_args(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.coeffs, [1, 2, 3])
        self.assertEqual(p.degree, 2)

    def test_constructor_correct(self):
        p1 = Polynomial([6, 3, 2, 1])
        self.assertEqual(p1.coeffs, [6, 3, 2, 1])
        self.assertEqual(p1.degree, 3)
        p2 = Polynomial([0])
        self.assertEqual(p2.coeffs, [0])
        self.assertEqual(p2.degree, 0)

    def test_constructor_bad(self):
        with self.assertRaises(Exception) as context:
            p1 = Polynomial([4, 's', 9, 8])
        self.assertEqual(str(context.exception),
                         "Coeffs list values(int or float)")
        with self.assertRaises(Exception) as context:
            p2 = Polynomial(['a'])
        self.assertEqual(str(context.exception),
                         "Coeffs list values(int or float)")

    def test_init_empty_list(self):
        self.assertRaises(TypeError, Polynomial, [])

    def test_init_no_list(self):
        self.assertRaises(TypeError, Polynomial, "1")

    def test_init_incorrect_list(self):
        self.assertRaises(TypeError, Polynomial, ["1", 2])

    def test_init_float_values(self):
        p = Polynomial([1.0, 2.0, 3.0])
        self.assertEqual(p.coeffs, [1.0, 2.0, 3.0])
        self.assertEqual(p.degree, 2)

    # -----------= tests ------------

    def test_eq_true(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 3])
        self.assertTrue(p1 == p2)

    def test_eq_false(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])
        self.assertFalse(p1 == p2)

    def test_eq_other_is_constant(self):
        p1 = Polynomial([2])
        p2 = 2
        self.assertTrue(p1 == p2)

    def test_eq_big_self_other_is_not_polynomial(self):
        p1 = Polynomial([2, 0, 0])
        p2 = 2
        self.assertFalse(p1 == p2)

    def test_eq_other_is_string(self):
        p1 = Polynomial([2, 0, 0])
        self.assertRaises(TypeError, p1.__eq__, "2")

    #----------------add_test--------------
    def test_add(self):
        p0 = Polynomial([3, 2, 1])
        p1 = Polynomial([2, 1])
        p2 = Polynomial([4, -3, -2.5, 1])

        res = p0 + p1
        self.assertEqual(res.coeffs, [3, 4, 2])

        res = p0 + p2
        self.assertEqual(res.coeffs, [4, 0, -0.5, 2])

    def test_add_with_null(self):
        p0 = Polynomial([3, 2, 1])
        p3 = Polynomial([-3, -2, -1])
        p4 = Polynomial([4.4, -3, -2, -1])

        res = p0 + p3
        self.assertEqual(res.coeffs, [0])

        res = p0 + p4
        self.assertEqual(res.coeffs, [4.4, 0, 0, 0])

    def test__add_bad(self):
        p0 = Polynomial([3, 2, 1])
        p5 = "3x2+2x+1"

        with self.assertRaises(Exception) as context:
            res = p0 + p5
        self.assertEqual(str(context.exception),"int or false p1+p2")

    def test_add_with_one_Value(self):
        p0 = Polynomial([3, 2, 1])
        p6 = Polynomial([3])
        p7 = 3
        p8 = Polynomial([0])

        res = p0 + p6
        self.assertEqual(res.coeffs, [3, 2, 4])

        res = p6 + p7
        self.assertEqual(res.coeffs, [6])

        res = p0 + p7
        self.assertEqual(res.coeffs, [3, 2, 4])

        res = p8 + p7
        self.assertEqual(res.coeffs, [3])

    def test_radd_base(self):
        p0 = Polynomial([3, 2, 1])
        p1 = Polynomial([2, 1])
        p2 = 1

        res = p1 + p0
        self.assertEqual(res.coeffs, [3, 4, 2])

        res = p2 + p0
        self.assertEqual(res.coeffs, [3, 2, 2])

        # ============= neg tests =============

    def test_neg(self):
        p0 = Polynomial([3, 2, 1])
        p1 = Polynomial([-3, -2, -1])
        p2 = -p0
        p3 = Polynomial([0])
        p4 = -p3
        self.assertTrue(p0 == -p1)
        self.assertTrue(-p0 == p1)
        self.assertTrue(p2 == p1)
        self.assertTrue(p3 == p4)

    def test_add_same_polyn_size(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1, 2])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [2, 4])
        self.assertEqual(p3.degree, 1)

    def test_add_different_polyn_size_first_larger(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 3, 5])
        self.assertEqual(p3.degree, 2)

    def test_add_different_polyn_size_second_larger(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1, 2, 3])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 3, 5])
        self.assertEqual(p3.degree, 2)

    def test_add_negative_values(self):
        p1 = Polynomial([1, -1])
        p2 = Polynomial([-1, 1])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)

    def test_add_left_term_is_const(self):
        p1 = 1
        p2 = Polynomial([1, 2, 3])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 2, 4])
        self.assertEqual(p3.degree, 2)

    def test_add_zero_values(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([0, 0])
        p3 = p1 + p2
        self.assertEqual(p3, p1)
        self.assertEqual(p3.degree, 2)

    def test_add_positive_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 1
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 3])
        self.assertEqual(p3.degree, 1)

    def test_add_incorrect_constant(self):
        p1 = Polynomial([1, 2])
        self.assertRaises(TypeError, p1.__add__, "11")

    def test_add_negative_constant(self):
        p1 = Polynomial([1, 2])
        p2 = -1
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 1])
        self.assertEqual(p3.degree, 1)

    def test_add_zero_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 0
        p3 = p1 + p2
        self.assertEqual(p3, p1)
        self.assertEqual(p3.degree, 1)

    def test_add_positive_float_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 2.4
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 4.4])
        self.assertEqual(p3.degree, 1)

    def test_add_zero_degree_polynom(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 3])
        self.assertEqual(p3.degree, 1)

    # ------------------- neg tests -----------------
    def test_neg(self):
        p1 = Polynomial([5, 8, 1])
        p2 = Polynomial([-5, -8, -1])
        self.assertTrue(p1 == -p2)
        self.assertTrue(-p1 == p2)

    # --------------------sub tests -----------------
    def test_sub_base(self):
        p0 = Polynomial([3, 2, 1])
        p1 = Polynomial([2, 1])
        p2 = Polynomial([4, 3, 2.5, 1])

        p3 = p0 - p1
        self.assertEqual(p3.coeffs, [3, 0, 0])

        p3 = p2 - p0
        self.assertEqual(p3.coeffs, [4, 0, 0.5, 0])

    def test_sub_bad(self):
        p0 = Polynomial([3, 2, 1])
        p5 = "8x2+2x+1"

        with self.assertRaises(Exception) as context:
            p3 = p0 - p5
        self.assertEqual(str(context.exception),
                         "('Coeffs list values(int or float)', '8x2+2x+1')")

    def test_rsub_base(self):
        p0 = Polynomial([3, 2, 1])
        p1 = Polynomial([2, 1])
        p2 = 1

        p3 = p1 - p0
        self.assertEqual(p3.coeffs, [-3, 0, 0])

        p3 = p2 - p0
        self.assertEqual(p3.coeffs, [-3, -2, 0])

    # --------------------mul tests -----------------
    def test_mul_same_polyn_size(self):
        p1 = Polynomial([1, 1])
        p2 = Polynomial([1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1, 2, 1])
        self.assertEqual(p3.degree, 2)

    def test_mul_different_polyn_size(self):
        p1 = Polynomial([1, 1, 1])
        p2 = Polynomial([1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1, 2, 2, 1])
        self.assertEqual(p3.degree, 3)

    def test_mul_zero_polyns(self):
        p1 = Polynomial([0, 1, 0])
        p2 = Polynomial([0, 0, 0, 0, 0])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)

    def test_mul_negative_values(self):
        p1 = Polynomial([1, -1, 1])
        p2 = Polynomial([-1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [-1, 2, -2, 1])
        self.assertEqual(p3.degree, 3)

    def test_mul_zero_values(self):
        p1 = Polynomial([1, -1, 1])
        p2 = Polynomial([0, 0, 0, 0])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)

    def test_mul_left_term_is_const(self):
        p1 = 2
        p2 = Polynomial([9, 2, 3])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [18, 4, 6])
        self.assertEqual(p3.degree, 2)

    def test_mul_zero_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 0
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)

    def test_mul_float_constant(self):
        p1 = Polynomial([1, 5])
        p2 = 1.4
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1.4, 7])
        self.assertEqual(p3.degree, 1)

    def test_mul_one_value_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 1
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, p1.coeffs)
        self.assertEqual(p3.degree, 1)

    def test_mul_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 5
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [5, 10])
        self.assertEqual(p3.degree, 1)

    def test_mul_incorrect_constant(self):
        p1 = Polynomial([1, 2])
        self.assertRaises(TypeError, p1.__mul__, "5")

    # ---------------str tests -------------------

    def test_str_base(self):
        p0 = Polynomial([1, 1, 1, 1])
        p1 = Polynomial([6, 3, 4, 1])
        p2 = Polynomial([-1, -3, -2, -1])
        p3 = Polynomial([-10, 5.5, 2, -1])
        p4 = Polynomial([2, 1])

        self.assertEqual(str(p0), "x3+x2+x+1")
        self.assertEqual(str(p1), "6x3+3x2+4x+1")
        self.assertEqual(str(p2), "-x3-3x2-2x-1")
        self.assertEqual(str(p3), "-10x3+5.5x2+2x-1")
        self.assertEqual(str(p4), "2x+1")

    def test_str_plus_with_null(self):
        p1 = Polynomial([4, 3, 2, 0])
        p2 = Polynomial([4, 3, 0, 1])
        p3 = Polynomial([4, 0, 0, 1])
        p4 = Polynomial([4, 0, 0, 0])
        p5 = Polynomial([0, 3, 2, 0])
        p6 = Polynomial([0, 0, 0, 1])

        self.assertEqual(str(p1), "4x3+3x2+2x")
        self.assertEqual(str(p2), "4x3+3x2+1")
        self.assertEqual(str(p3), "4x3+1")
        self.assertEqual(str(p4), "4x3")
        self.assertEqual(str(p5), "3x2+2x")
        self.assertEqual(str(p6), "1")

    def test_str_minus_with_null(self):
        p1 = Polynomial([-4, -3, -2, 0])
        p2 = Polynomial([-4, -3, 0, -1])
        p3 = Polynomial([-4, 0, 0, -1])
        p4 = Polynomial([-4, 0, 0, 0])
        p5 = Polynomial([0, -3, -2, 0])
        p6 = Polynomial([0, 0, 0, -1])

        self.assertEqual(str(p1), "-4x3-3x2-2x")
        self.assertEqual(str(p2), "-4x3-3x2-1")
        self.assertEqual(str(p3), "-4x3-1")
        self.assertEqual(str(p4), "-4x3")
        self.assertEqual(str(p5), "-3x2-2x")
        self.assertEqual(str(p6), "-1")

    def test_str_zero_values(self):
        p1 = Polynomial([0, 0, 0])
        self.assertEqual(str(p1), '0')

    def test_str_first_float_zero_values(self):
        p1 = Polynomial([0.0, 0.0, 0.0])
        self.assertEqual(str(p1), '0')

    def test_str_first_value_is_zero(self):
        p1 = Polynomial([0, 2, 3])
        self.assertEqual(str(p1), '2x+3')

    def test_str_first_value_is_one(self):
        p1 = Polynomial([1, 2, 3])
        self.assertEqual(str(p1), 'x2+2x+3')

    def test_str_all_values_are_one(self):
        p1 = Polynomial([1, 1, 1])
        self.assertEqual(str(p1), 'x2+x+1')

    def test_str_last_value_is_zero(self):
        p1 = Polynomial([1, 8, 0])
        self.assertEqual(str(p1), 'x2+8x')

    def test_str_first_three_value_is_zero(self):
        p1 = Polynomial([0, 0, 0, 1])
        self.assertEqual(str(p1), '1')

    def test_str_one_value_is_zero(self):
        p1 = Polynomial([0, 1, 0])
        self.assertEqual(str(p1), 'x')

    def test_str_one_value_is_minus_zero(self):
        p1 = Polynomial([0, -1, 0])
        self.assertEqual(str(p1), '-x')

if __name__ == "__main__":
    main()
