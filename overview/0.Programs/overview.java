import java.util.Random;

public class overview {
	public static int modExp(int y, int k, int n) throws InterruptedException
	{
		int r = 1;
		while(k > 0)
		{
			if(k % 2 == 1)
			{
                int ytmp = y;
				while(ytmp > 0)
				{
                    if(ytmp % 2 == 1)
                    {
                        Thread.sleep(1);
                    }
                    ytmp = ytmp >> 1;
                }
			}
			k = k >> 1;
		}
		return r % n;
	}
	
	public static void main(String[] args) throws InterruptedException
	{
		int n = 10;
        int[] bits_val = new int[11];
        for(int j = 1; j < Math.pow(2, n); j++)
        {
            int y = j;
            int cnt = 0;
            while(y > 0)
            {
                if(y % 2 == 1)
                    cnt += 1;
                y = y >> 1;
            }
            if(bits_val[cnt] == 0)
                bits_val[cnt] = j;
            else
            {
                if(bits_val[cnt] % 2 == 0 && j % 2 != 0)
                    bits_val[cnt] = j;
                else if(bits_val[cnt] % 2 != 0 && j % 2 == 0)
                    bits_val[cnt] = j;
                
            }
        }
		for(int i = 1; i < Math.pow(2, n); i++)
		{
			int k = i;
            double duration = 0.0;
            for(int r = 1; r < 11; r++)
            {
                int y = bits_val[r];
                long startTime = System.nanoTime();
                modExp(y, k, n);
                long endTime = System.nanoTime();
                long elapsedTime = endTime - startTime;
                duration = (double)elapsedTime;
                System.out.println(duration/1000);
			}
			System.out.println("***");
		}
	}
}
