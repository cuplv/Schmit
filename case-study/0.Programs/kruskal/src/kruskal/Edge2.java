package kruskal;

public class Edge2 implements Comparable<Edge2> {
	int src;
	int dst;
	int weight;
	public static int count;
	public Edge2()
	{
	}
	public Edge2(int s,int d, int w)
	{
		this.src = s;
		this.dst = d;
		this.weight = w;
	}
	
	public int compareTo(Edge2 compareEdge)
    {
		count++;
        return this.weight-compareEdge.weight;
    }

}
