using System;
using System.Text;

namespace Quiz001
{
    public class Test
    {
        public static string GetAnswer()
        {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i <= 9000; i++)
            {
                sb.Append(i.ToString());
            }
            return sb.ToString();
        }

        public static string GetAnswer2()
        {
            string s = "";
            for (int i = 0; i <= 9000; i++)
            {
                s += i.ToString();
            }
            return s;
        }

    }
}
