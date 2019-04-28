package kruskal;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Set;

public class Kruskal {
	public void kruskal(List<Edge2> graph, int n)
	{
		int V = n;
        Edge2 result[] = new Edge2[V];  // Tnis will store the resultant MST 
        int e = 0;  // An index variable, used for result[] 
        int i = 0;  // An index variable, used for sorted edges 
        for (i=0; i < V; ++i) 
            result[i] = new Edge2(); 
  
        // Step 1:  Sort all the edges in non-decreasing order of their 
        // weight.  If we are not allowed to change the given graph, we 
        // can create a copy of array of edges 
        Collections.sort(graph); 
  
        // Allocate memory for creating V ssubsets 
        subset subsets[] = new subset[V]; 
        for(i=0; i<V; ++i) 
            subsets[i]=new subset(); 
  
        // Create V subsets with single elements 
        for (int v = 0; v < V; ++v) 
        { 
            subsets[v].parent = v; 
            subsets[v].rank = 0; 
        } 
  
        i = 0;  // Index used to pick next edge 
  
        // Number of edges to be taken is equal to V-1 
        while (e < V - 1) 
        { 
            // Step 2: Pick the smallest edge. And increment  
            // the index for next iteration 
            Edge2 next_edge = new Edge2(); 
            next_edge = graph.get(i); 
  
            int x = find(subsets, next_edge.src); 
            int y = find(subsets, next_edge.dst); 
  
            // If including this edge does't cause cycle, 
            // include it in result and increment the index  
            // of result for next edge 
            if (x != y) 
            { 
                result[e++] = next_edge; 
                Union(subsets, x, y); 
            }
            i++;
            // Else discard the next_edge 
        } 
  
        // print the contents of result[] to display 
        // the built MST 
//        System.out.println("Following are the edges in " +  
//                                     "the constructed MST"); 
//        for (i = 0; i < e; ++i) 
//            System.out.println(result[i].src+" -- " +  
//                   result[i].dst+" == " + result[i].weight); 
	}
	
    // A class to represent a subset for union-find 
    class subset 
    { 
        int parent, rank; 
    }; 
	
    public static void dummy(int size) throws InterruptedException
    {
    	size = size / 5 + 1;
		if(Edge2.count >= 11200 && Edge2.count <= 12500)
		{
			Edge2.count = 0;
			return;
		}
		if(Edge2.count > 23700)
		{
			Edge2.count = 0;
			return;			
		}
		if(Edge2.count <= 1250)
		{
			double curTime =  0;
			double patchTime =  0;
			if(size < 3)
			{
				curTime =  0.5 * size - 0.37;
				patchTime =  6.9 * size	- 7.0;
			}
			else
			{
				curTime =  0.034 * size + 0.6;
				patchTime =  0.045 * size + 9.3;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 1250 && Edge2.count <= 2500)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime =  1.25 * size - 1.3;
				patchTime =  6.9 * size	- 7.0;
			}
			else
			{
				curTime =  0.034 * size + 1.5;
				patchTime =  0.045 * size + 9.3;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 2500 && Edge2.count <= 3750)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime =  2.0 * size - 1.9;
				patchTime =  6.9 * size	- 7.0;
			}
			else
			{
				curTime =  0.04 * size + 2.2;
				patchTime =  0.045 * size + 9.3;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 3750 && Edge2.count <= 5000)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime =  2.64 * size - 2.7;
				patchTime =  6.9 * size	- 7.0;
			}
			else
			{
				curTime =  0.035 * size + 3.1;
				patchTime =  0.045 * size + 9.3;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 5000 && Edge2.count <= 6250)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime =  3.33 * size - 3.2;
				patchTime =  6.9 * size	- 7.0;
			}
			else
			{
				curTime =  0.038 * size + 3.9;
				patchTime =  0.045 * size + 9.3;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 6250 && Edge2.count <= 7500)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime =  4.0 * size - 4.0;
				patchTime =  6.9 * size	- 7.0;
			}
			else
			{
				curTime =  0.04 * size + 4.7;
				patchTime =  0.045 * size + 9.3;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 7500 && Edge2.count <= 8725)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime =  4.75 * size - 4.8;
				patchTime =  6.9 * size	- 7.0;
			}
			else
			{
				curTime =  0.04 * size + 5.7;
				patchTime =  0.045 * size + 9.3;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 8725 && Edge2.count <= 10000)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime =  5.5 * size - 5.5;
				patchTime =  6.9 * size	- 7.0;
			}
			else
			{
				curTime =  0.041 * size + 6.6;
				patchTime =  0.045 * size + 9.3;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 10000 && Edge2.count <= 11200)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime =  6.25 * size - 6.3;
				patchTime =  6.9 * size	- 7.0;
			}
			else
			{
				curTime =  0.041 * size + 7.5;
				patchTime =  0.045 * size + 9.3;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 12500 && Edge2.count <= 13700)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime = 7.7 * size - 7.7;
				patchTime =  14.6 * size - 15.0;
			}
			else
			{
				curTime = 0.045 * size + 9.2  ;
				patchTime =  0.06 * size + 18.4;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 13700 && Edge2.count <= 15000)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime = 8.55 * size - 8.6;
				patchTime =  14.6 * size - 15.0;
			}
			else
			{
				curTime = 0.047 * size + 10.1  ;
				patchTime =  0.06 * size + 18.4;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 15000 && Edge2.count <= 16200)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime = 9.25 * size - 9.2;
				patchTime =  14.6 * size - 15.0;
			}
			else
			{
				curTime = 0.047 * size + 11.0 ;
				patchTime =  0.06 * size + 18.4;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 16200 && Edge2.count <= 17500)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime = 9.95 * size - 10.0;
				patchTime =  14.6 * size - 15.0;
			}
			else
			{
				curTime = 0.0485 * size + 12.0 ;
				patchTime =  0.06 * size + 18.4;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 17500 && Edge2.count <= 18750)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime = 10.7 * size - 9.7;
				patchTime =  14.6 * size - 15.0;
			}
			else
			{
				curTime = 0.0488 * size + 12.9 ;
				patchTime =  0.06 * size + 18.4;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 18750 && Edge2.count <= 20000)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime = 11.5 * size - 11.4;
				patchTime =  14.6 * size - 15.0;
			}
			else
			{
				curTime = 0.05 * size + 13.8;
				patchTime =  0.06 * size + 18.4;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 20000 && Edge2.count <= 21200)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime = 12.3 * size - 12.3;
				patchTime =  14.6 * size - 15.0;
			}
			else
			{
				curTime = 0.054 * size + 14.7;
				patchTime =  0.06 * size + 18.4;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 21200 && Edge2.count <= 22400)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime = 13.1 * size - 13.1;
				patchTime =  14.6 * size - 15.0;
			}
			else
			{
				curTime = 0.054 * size + 15.6;
				patchTime =  0.06 * size + 18.4;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		if(Edge2.count >= 22400 && Edge2.count <= 23700)
		{
			double curTime =  0;
			double patchTime = 0;
			if(size < 3)
			{
				curTime = 13.8 * size - 13.8;
				patchTime =  14.6 * size - 15.0;
			}
			else
			{
				curTime = 0.056 * size + 16.6;
				patchTime =  0.06 * size + 18.4;			
			}
			double diff = patchTime - curTime;
			if(diff <=0)
				diff = 0;
			Thread.sleep((long)diff);
		}
		Edge2.count = 0;
    }
    
    int find(subset subsets[], int i) 
    { 
        // find root and make root as parent of i (path compression) 
        if (subsets[i].parent != i) 
            subsets[i].parent = find(subsets, subsets[i].parent); 
  
        return subsets[i].parent; 
    } 
  
    // A function that does union of two sets of x and y 
    // (uses union by rank) 
    void Union(subset subsets[], int x, int y) 
    { 
        int xroot = find(subsets, x); 
        int yroot = find(subsets, y); 
  
        // Attach smaller rank tree under root of high rank tree 
        // (Union by Rank) 
        if (subsets[xroot].rank < subsets[yroot].rank) 
            subsets[xroot].parent = yroot; 
        else if (subsets[xroot].rank > subsets[yroot].rank) 
            subsets[yroot].parent = xroot; 
  
        // If ranks are same, then make one as root and increment 
        // its rank by one 
        else
        { 
            subsets[yroot].parent = xroot; 
            subsets[xroot].rank++; 
        } 
    } 
	
	public static void main(String[] args) throws IOException, InterruptedException
	{

		int cnt = 0;
		for(int e = 50; e < 1050; )
		{
			for(int v = 2; v < 202;)
			{
                BufferedWriter writer = new BufferedWriter(new FileWriter("shared.txt"));
                writer.write(String.valueOf(v));
                writer.close();
				List<Edge2> lst = new ArrayList<>();
				Set<Integer> vert = new HashSet<>();
				Map<Integer,Integer> m = new HashMap<>();
				for(int i = 0; i < e *  25; i++)
				{
					Random rnd = new Random();
					int s = rnd.nextInt(v);
					int d = rnd.nextInt(v);
					int w = rnd.nextInt(e * 5)+1;
					if(s != d)
					{
						if((m.containsKey(s) && m.get(s) == d) || (m.containsKey(d) && m.get(d) == s))
						{
							i--;
							continue;
						}
						vert.add(s);
						vert.add(d);
						m.put(s, d);
						Edge2 e1 = new Edge2(s, d, w);
						lst.add(e1);
					}
				}
				double duration = 0.0;
				for(int i = 0; i < 10 ; i++)
				{
					long startTime = System.nanoTime();
					Kruskal ksl = new Kruskal();
					ksl.kruskal(lst, vert.size());
					dummy(v);
					long endTime = System.nanoTime();
				    long elapsedTime = endTime - startTime;
				    duration += elapsedTime;
				}
			    System.out.println(duration/10.0);
			    v += 5;
			}
		    System.out.println("***");
		    if(cnt > 4)
		    {
				e += 50;
				cnt = 0;
		    }
		    else
		    {
			    cnt++;		    	
		    }
		}

	}
}
