using System;
using System.Linq;
using RedditSharp;
using RedditSharp.Things;

namespace c0db3rb0t_redditbot
{
    class RedditBot
    {
        public RedditBot(String password)
        {
            BotWebAgent userAgent = new BotWebAgent("vitalc0d3r", password, "zC2ev-zjX8P_5A", "CazRtoCuSIjY5829OV7H9NwO4O8", "http://localhost:8080");
            Reddit reddit = new Reddit(userAgent, false);
            Subreddit subreddit = reddit.GetSubreddit("pcmasterrace");

            foreach (Post post in subreddit.New.Take(100))
            {
                Console.WriteLine(post.Title + "\n" + post + "\n");
            }
        }
    }
}
