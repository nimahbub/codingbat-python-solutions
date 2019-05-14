def make_bricks(small, big, goal):
"""
We want to make a row of bricks that is goal inches long.
We have a number of small bricks (1 inch each) and big bricks (5 inches each).
Return True if it is possible to make the goal by choosing from the given bricks.
This is a little harder than it looks and can be done without any loops
"""
  if goal > small + big * 5:
    return False
  else:
    if (goal % 5 <= small):
      return True
    return False


  
  ##===================================================================================================
  
  def lone_sum(a, b, c):
    
    """
    Given 3 int values, a b c, return their sum. However, 
    if one of the values is the same as another of the values, it does not count towards the sum.
    
    """
    if (a ==b  and a ==c and b ==c ):
      return 0
    elif(a==b):
      return c
    elif(a==c):
      return b

    elif(b==c):
      return a
    else:
      return a+b+c
    
    
    
    ##=============================================================================================>>>
    def lucky_sum(a, b, c):
          """   
          Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count
          towards the sum and values to its right do not count. So for example, 
          if b is 13, then both b and c do not count.
          """
      if (a !=13 and b!=13 and c!=13):
          return a+b+c
      if(a==13):
          return 0
      if (b==13):
          return a
      if (c==13):
        return a+b



  
  
  
  
