# This also works :)
library('fda')
library('fda.usc')
library('dbscan')
library("Cairo")
library("conclust")
library("data.table")

args = commandArgs(trailingOnly=TRUE)
# args[1] --> name of input file
# args[2] --> 0 for derivative=0 and 1 for derivative 1
# args[3] --> 'kl','lp','fdata','pca','deriv','fourier','hshift','basis'
# args[4] --> 1) norm = '0', '1', '2' only if args[3] is one of 'lp', 'fdata', 'deriv' 
#             2) nderiv = 0...n only if args[3] is one 'deriv', 'basis'
# args[5] --> the epsilon indistinguishably
# args[6] --> 'kmean' or 'hclust'
# args[7] --> 0 = do not write label to output, 1 = write the label to output

MyData <- as.matrix(read.csv(file=args[1]))
N <- dim(MyData)[2]
X <- dim(MyData)[1]
Data <- t(as.matrix(MyData)[1:X,2:N])/1000
orgData <- Data/1000000
orgX <- X

rng = seq(1,X,1)
nbasis = X
max_X <- 1


namefile = strsplit(args[1],"/")[[1]][2]

init = paste("Figures/initial_",namefile, ".png",sep = '')
Cairo(file=init,
      bg="white",
      type="png",
      units="in",
      width=12,
      height=9,
      pointsize=12,
      dpi=200)
par(mar=c(7, 6, 1, 1) + 0.2)

matplot(rng,t(orgData),type='l', axes=F, xlab = '', ylab = '', lwd = 2)
axis(2, ylim=c(0,t(orgData)),lwd=2, cex.axis = 3, font = 2)
mtext(2,text="Time",line=3, cex = 3)
axis(1, xlim=rng,lwd=2, cex.axis = 3, font = 2)
mtext(1,text="Public inputs ",line=4, cex = 3)
dev.off()


# We assume the input is sent as soon as the previous one received!
# for(i in 1:(N-1))
# {
#   sum = 0
#   for(j in 1:X)
#   {
#     sum = sum + Data[i,j]
#     Data[i,j] = sum
#   }
# }

for(i in 1:(N-1))
{
  epoch = 2
  cur_time = Data[i,1]
  last_pred = 0
  for(j in 2:X)
  {
    while(Data[i,j] > max(cur_time,last_pred) + 2**(epoch-1))
    {
      # cur_time = max(cur_time,last_pred) + 2**(epoch-1)
      epoch = epoch + 1
    }
    cur_time = max(cur_time,last_pred) + 2**(epoch-1)
    Data[i,j] = cur_time
    # prev_time = cur_time
    # last_pred = Data[i,j]
  }
}

start_time <- as.numeric(Sys.time())*1000

bsp1 <- create.bspline.basis(norder = 2, breaks=rng , nbasis = nbasis)
fd1 <- smooth.basis(rng , y=t(Data), bsp1)

# for derivative = 0
if(args[2]=='0'){
  compFunctionalData <- fdata(fd1$fd, rng)}

# for derivative = 1
if(args[2]=='1'){
  fd1 = deriv.fd(fd1$fd)
  compFunctionalData <- fdata(fd1, rng)
  }

if(args[3]=='kl'){
  dist <- metric.kl(compFunctionalData)
}
if(args[3]=='lp'){
  dist <- metric.lp(compFunctionalData,lp = as.integer(args[4]))
  dist <- dist/max_X
}
if(args[3]=='fdata'){
  dist <- norm.fdata(compFunctionalData, lp = as.integer(args[4]))
}
if(args[3]=='pca'){
  dist <- semimetric.pca(compFunctionalData)
}
if(args[3]=='deriv'){
  dist <- semimetric.deriv(compFunctionalData,nderiv = as.integer(args[4]))
}
if(args[3]=='fourier'){
  dist <- semimetric.fourier(compFunctionalData)
}
if(args[3]=='hshift'){
  dist <- semimetric.hshift(compFunctionalData)
}
if(args[3]=='basis'){
  dist <- semimetric.basis(compFunctionalData, lp = as.integer(args[4]))
}

krng<- 1:N
d1 <- as.numeric(args[5])
d2 <- d1

links <- c()
notLinks <- c()

dist1 <- dist
dist1[dist1 <= d1] <- 0
dist1[dist1 > d1] <- 1
cantLink <- which(dist1!=0,arr.ind = T)

if(args[6] == 'hclust')
{
  clusters <- hclust(dist(dist))

  for(k in krng)
  {
    clusterCut = as.vector(cutree(clusters, k))

    flag_inter = FALSE;
    for(i in 1:nrow(cantLink))
    {
      if(length(cantLink) == 0)
        break;
      p1 = cantLink[i,1]
      p2 = cantLink[i,2]
      if(clusterCut[p1] == clusterCut[p2])
      {
          flag_inter = TRUE;
          break;
      }
    }
    if(!flag_inter)
    {
      break;
    }
    print(k)
  }
}
if(args[6] == 'kmeans')
{

  mustLink = matrix(, nrow = 0, ncol = 0)

  for(cls in krng)
  {
    pred <- ckmeans(dist, k=cls, mustLink, cantLink)
    if(length(pred) > 1)
      break
    print(cls)
  }
  clusterCut <- pred
  k = cls
}

end_time <- as.numeric(Sys.time())*1000
print(end_time-start_time, digits=15)

vecCol <- c()
clusterCut = as.vector(cutree(clusters, k))
colorsRain = rainbow(k)
colorsRain <- sample(colorsRain)
i <- 1
for(lab in clusterCut)
{
  vecCol[i] <- colorsRain[lab]
  i <- i + 1
}

final = paste("Figures/final_",namefile, ".png",sep = '')
Cairo(file=final,
      bg="white",
      type="png",
      units="in",
      width=12,
      height=9,
      pointsize=14,
      dpi=200)
par(mar=c(7, 6, 2,2) + 0.2)

matplot(rng,t(Data),type='l',col=clusterCut,  axes=F, xlab = '', ylab = '', lwd = 2)
axis(2, ylim=c(0,t(Data)),lwd=2, cex.axis = 3, font = 2)
mtext(2,text="Time",line=3, cex = 3)
axis(1, xlim=rng,lwd=2, cex.axis = 3, font = 2)
mtext(1,text="Public inputs",line=4, cex = 3)
dev.off()

print("Number of functional clusters is: ")
print(k)

min_guess = .Machine$integer.max
guess = 0.0
Shannon = 0.0
for(clust in 1:k)
{
  indicies = which(clusterCut == clust)
  elements = dist[indicies]
  # max_val = max(elements)
  # overhead = overhead + max_val * length(elements)
  if(min_guess > length(elements))
    min_guess = length(elements)
  guess = guess + length(elements)**2
  Shannon = Shannon + length(elements) * log2(length(elements)+0.00001)
}
print("Min Guess entropy is: ")
print(min_guess)
print("Guessing entropy is: ")
print(guess/(2*N))
print("Shannon entropy is: ")
print(Shannon/(N))
overhead = 0.0
distances = c()
for(clust in 1:k)
{
  indicies = which(clusterCut == clust)
  elements = Data[indicies,]
  val = max(elements)
  overhead = overhead + val * length(elements)
  distances[clust] = max(elements)
}
print("Double Scheme overhead is (divide to initial overhead to get percentage): ")
print(overhead/(N))