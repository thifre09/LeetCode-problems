public class Solution
{
    public int LengthOfLastWord(string s)
    {
        int i = 1;
        int k = 0;
        s = s.TrimEnd();

        while (true)
        {
            try
            {
                if (s[s.Length - i] == ' ')
                {
                    int retorno = k;
                    return retorno;
                }
                else
                {
                    i += 1;
                    k += 1;
                }
            }
            catch (System.Exception)
            {
                return k;
            }
                
        }
    }

    public static void Main()
    {
        Console.WriteLine(new Solution().LengthOfLastWord(" ola"));
    }
}