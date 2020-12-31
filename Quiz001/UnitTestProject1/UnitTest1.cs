using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Diagnostics;
using Quiz001;

namespace UnitTestProject1
{

    [TestClass]
    public class UnitTest1
    {
        public string Validate()
        {
            string s = "";
            for (int i = 0; i <= 9000; i++)
            {
                s += i.ToString();
            }
            return s;
        }

        [TestMethod]
        public void TestMethod1()
        {
            string validateString = Validate();
            Stopwatch sw = new Stopwatch();
            sw.Restart();
            bool error = false;
            for (int i = 0; i < 100; i++)
            {
                if (validateString == Test.GetAnswer2())
                {

                }
                else
                {
                    error = true;
                    break;
                }
            }
            sw.Stop();
            if (error)
            {
                Assert.IsFalse(error, "字串比對錯誤。");
            }
            else
            {
                //0.022869482999999996
                double averageSeconds = sw.Elapsed.TotalSeconds / 100.0;
                Assert.IsFalse(averageSeconds > 0.001, "速度測試未通過，平均耗時" + averageSeconds.ToString("0.000000") + "秒");
            }
        }
    }
}
