using System;
using RedditSharp;

namespace c0db3rb0t_redditbot
{
    class Program
    {
        static void Main(string[] args)
        {
            RedditBot redditBot;

            try
            {
                redditBot = new RedditBot(args[0]);
            }

            catch (Exception exception)
            {
                Console.WriteLine("An error has occured, try again! \n" + exception.Data + "\n" + exception.StackTrace + "\n");

                System.Environment.Exit(1);
            }
        }
    }
}