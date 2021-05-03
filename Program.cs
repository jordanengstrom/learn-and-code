using System;

namespace learn_and_code
{

    public class Card
    {
        public int Shape { get; set; }
        public int Color { get; set; }
        public int Shade { get; set; }
        public int Number { get; set; }
        public Card(int shape, int color, int shade, int number) {
            Shape = shape;
            Color = color;
            Shade = shade;
            Number = number;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
