using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text.RegularExpressions;
using System.Threading;

public static class Program {
    public static void Main() {
        int N = 10000;
        int K = 5000;
        
        long sum = 0;

        var stopWatch = new Stopwatch();

        stopWatch.Start();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < K; j++) {
                sum += i - (j / 2);
            }
        }
        stopWatch.Stop();

        Console.WriteLine(sum);
        Console.WriteLine($"{stopWatch.Elapsed.TotalMilliseconds:N2}");
    }
}
