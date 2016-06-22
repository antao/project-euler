using System;
using System.Collections.Generic;
using System.Linq;

namespace euler._003
{
    /// <summary>
    /// The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?
    /// </summary>
    public class Problem003 : ISolution
    {
        public string Solution()
        {
            var number = 600851475143;
            var list = new List<long>();

            while (number % 2 == 0)
            {
                list.Add(number);
                number = number / 2;
            }

            for (int i = 3; i <= Math.Sqrt(number); i = i + 2)
            {
                while (number % i == 0)
                {
                    list.Add(number);
                    number = number / i;
                }
            }

            if (number > 2)
            {
                list.Add(number);
            }

            // Linq extensions
            return string.Format("{0}", list.Min());
        }
    }
}
