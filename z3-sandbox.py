from z3 import Int, Ints, solve, Implies

# x = Int('x')
# y = Int('y')
# solve(x > 2, y < 10, x + 2*y == 7)

r1t1m1, r1t2m1, r1t1m2, r1t2m2, r2t1m1, r2t2m1, r2t1m2, r2t2m2 = Ints('r1t1m1 r1t2m1 r1t1m2 r1t2m2 r2t1m1 r2t2m1 r2t1m2 r2t2m2')

solve(r1t1m1 >= 0, r1t2m1 >= 0, r1t1m2 >= 0, r1t2m2 >= 0,
      r2t1m1 >= 0, r2t2m1 >= 0, r2t1m2 >= 0, r2t2m2 >= 0,
      #
      r1t1m1 + r2t1m1 + r1t2m1 + r2t2m1 == 1,
      r1t1m2 + r2t1m2 + r1t2m2 + r2t2m2 == 1,
      #
      r1t1m1 + r1t1m2 <= 1,
      r2t1m1 + r2t1m2 <= 1
      )

r1t1, r1t2, r1t3, r2t1, r2t2, r2t3 = Ints('r1t1 r1t2 r1t3 r2t1 r2t2 r2t3')

solve(r1t1 >= 0, r1t1 <= 5, r1t2 >= 0, r1t2 <= 5, r1t3 >= 0, r1t3 <= 5,
      r2t1 >= 0, r2t1 <= 5, r2t2 >= 0, r2t2 <= 5, r2t3 >= 0, r2t3 <= 5,
      #
      r1t1 != r1t2, r1t1 != r2t1, r1t1 != r2t2, r1t1 != r1t3, r1t1 != r2t3, r1t2 != r1t3,
      r2t1 != r2t2, r2t1 != r2t3, r2t2 != r2t3,
      r1t1 + r1t2 + r1t3 + r2t1 + r2t2 + r2t3 == 1 + 2 + 3 + 4 + 5)

# The same with arrays

# easier if the session is one of the indices instead of the values? how to represent collisions?

# optimization to minimize number of collisions based on the peoples' selections of the sessions

s1r, s1t, s2r,  s2t, s3r, s3t, s4r, s4t, s5r, s5t = Ints('s1r s1t s2r s2t s3r s3t s4r s4t s5r s5t')
solve(s1r > 0, s1r <= 3, s2r > 0, s2r <= 3, s3r > 0, s3r <= 3, s4r > 0, s4r <= 3, s5r > 0, s5r <= 3,
      s1t > 0, s1t <= 2, s2t > 0, s2t <= 2, s2t > 0, s2t <= 2, s4t > 0, s4t <= 2, s5t > 0, s5t <= 2,
      #
      Implies(s1t == s2t, s1r != s2r),
      Implies(s1t == s3t, s1r != s3r), Implies(s1t == s4t, s1r != s4r), Implies(s1t == s5t, s1r != s5r),
      #
      Implies(s2t == s3t, s2r != s3r), Implies(s2t == s4t, s2r != s4r), Implies(s2t == s5t, s2r != s5r),
      #
      Implies(s3t == s4t, s3r != s4r), Implies(s3t == s5t, s3r != s5r),
      #
      Implies(s4t == s5t, s4r != s5r))



# if somebody wants to attend 2 and 3
#
