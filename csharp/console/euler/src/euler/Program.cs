using System;
using System.Diagnostics;
using euler._003;

namespace euler
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var stopWatch = Stopwatch.StartNew();

            Problem003 problem = new Problem003();

            Console.WriteLine("{0}", problem.Solution());
            Console.WriteLine("Execution of program took {0} milliseconds to execute", stopWatch.ElapsedMilliseconds);
            Console.ReadLine();
        }
    }
}
