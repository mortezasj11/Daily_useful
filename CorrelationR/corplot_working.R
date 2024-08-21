########################################
library(corrplot)
setwd("E:/papers/CT2PET/CorrelationCSVs/")
X_meta = read.csv("ICON_Pred_allMTV.csv",sep=",",header = TRUE)
Y_meta = read.csv("ICON_Truth_allMTV.csv",sep=",",header = TRUE)
X=X_meta[,3:12]
Y=Y_meta[,3:12]

rownames(Y)=Y_meta$MRN
rownames(X)=X_meta$MRN

ex_Y <- log2(as.matrix(Y+1))  # remove duplicates
ex_Y1=data.frame(ex_Y)

ex_X <- log2(as.matrix(X+1))  # remove duplicates
ex_X1=data.frame(ex_X)
#apply Z-score normalization to fex
ex_normY <- as.data.frame(scale(ex_Y1[1:10]))
ex_normX <- as.data.frame(scale(ex_X1[1:10]))

rownames(ex_normY)=Y_meta$MRN      #print(colnames(Y_meta))
rownames(ex_normX)=X_meta$MRN   

xx = ex_normX[,c("MTV_0.5","TLG_0.5","MTV_1.5","TLG_1.5","MTV_2.5","TLG_2.5","MTV_3.5","TLG_3.5","SUV_max","SUV_mean")]
yy = ex_normY[,c("MTV_0.5","TLG_0.5","MTV_1.5","TLG_1.5","MTV_2.5","TLG_2.5","MTV_3.5","TLG_3.5","SUV_max","SUV_mean")]

df2 <- cor(xx,yy, use = "na.or.complete")
corrplot(df2, is.corr = FALSE, , col.lim = c(0, 1),tl.col = "black")

################################################################################

setwd("E:/papers/CT2PET/CorrelationCSVs/")
X_meta = read.csv("PROSPECT_Pred_MTV_TLG_pall.csv",sep=",",header = TRUE)
Y_meta = read.csv("PROSPECT_True_MTV_TLG_pall.csv",sep=",",header = TRUE)
X=X_meta[,3:12]
Y=Y_meta[,3:12]

rownames(Y)=Y_meta$MRN
rownames(X)=X_meta$MRN

ex_Y <- log2(as.matrix(Y+1))  # remove duplicates
ex_Y1=data.frame(ex_Y)

ex_X <- log2(as.matrix(X+1))  # remove duplicates
ex_X1=data.frame(ex_X)
#apply Z-score normalization to fex
ex_normY <- as.data.frame(scale(ex_Y1[1:10]))
ex_normX <- as.data.frame(scale(ex_X1[1:10]))

rownames(ex_normY)=Y_meta$MRN      #print(colnames(Y_meta))
rownames(ex_normX)=X_meta$MRN   

xx = ex_normX[,c("MTV_0.5","TLG_0.5","MTV_1.5","TLG_1.5","MTV_2.5","TLG_2.5","MTV_3.5","TLG_3.5","SUV_max","SUV_mean")]
yy = ex_normY[,c("MTV_0.5","TLG_0.5","MTV_1.5","TLG_1.5","MTV_2.5","TLG_2.5","MTV_3.5","TLG_3.5","SUV_max","SUV_mean")]

df2 <- cor(xx,yy, use = "na.or.complete")
corrplot(df2, is.corr = FALSE, , col.lim = c(0, 1),tl.col = "black")

################################################################################

setwd("E:/papers/CT2PET/CorrelationCSVs/")
X_meta = read.csv("TCIA_Pred_MTV_TLG_pall.csv",sep=",",header = TRUE)
Y_meta = read.csv("TCIA_True_MTV_TLG_pall.csv",sep=",",header = TRUE)
X=X_meta[,3:12]
Y=Y_meta[,3:12]

rownames(Y)=Y_meta$MRN
rownames(X)=X_meta$MRN

ex_Y <- log2(as.matrix(Y+1))  # remove duplicates
ex_Y1=data.frame(ex_Y)

ex_X <- log2(as.matrix(X+1))  # remove duplicates
ex_X1=data.frame(ex_X)
#apply Z-score normalization to fex
ex_normY <- as.data.frame(scale(ex_Y1[1:10]))
ex_normX <- as.data.frame(scale(ex_X1[1:10]))

rownames(ex_normY)=Y_meta$MRN      #print(colnames(Y_meta))
rownames(ex_normX)=X_meta$MRN   

xx = ex_normX[,c("MTV_0.5","TLG_0.5","MTV_1.5","TLG_1.5","MTV_2.5","TLG_2.5","MTV_3.5","TLG_3.5","SUV_max","SUV_mean")]
yy = ex_normY[,c("MTV_0.5","TLG_0.5","MTV_1.5","TLG_1.5","MTV_2.5","TLG_2.5","MTV_3.5","TLG_3.5","SUV_max","SUV_mean")]

df2 <- cor(xx,yy, use = "na.or.complete")
corrplot(df2, is.corr = FALSE, , col.lim = c(0, 1),tl.col = "black")


################################
################################
################################
################################
################################


############################# TCIA  ################################################

setwd("E:/papers/CT2PET/CorrelationCSVs/")
X_meta = read.csv("TCIA_Pred_MTV_TLG_pall.csv",sep=",",header = TRUE)
Y_meta = read.csv("TCIA_True_MTV_TLG_pall.csv",sep=",",header = TRUE)
X=X_meta[,3:12]
Y=Y_meta[,3:12]


clip_SUVmaxY = Y$SUV_max
clip_SUVmaxY[clip_SUVmaxY>7.0]=7.0
Y[["SUV_max7_gt"]] <- clip_SUVmaxY
X[["SUV_max7_syn"]] <- X$SUV_max


rownames(Y)=Y_meta$MRN
rownames(X)=X_meta$MRN

ex_Y <- log2(as.matrix(Y+1))  # remove duplicates
ex_Y1=data.frame(ex_Y)

ex_X <- log2(as.matrix(X+1))  # remove duplicates
ex_X1=data.frame(ex_X)
#apply Z-score normalization to fex
ex_normY <- as.data.frame(scale(ex_Y1[1:11]))
ex_normX <- as.data.frame(scale(ex_X1[1:11]))

rownames(ex_normY)=Y_meta$MRN      #print(colnames(Y_meta))
rownames(ex_normX)=X_meta$MRN   

xx = ex_normX[,c("MTV_0.5","TLG_0.5","MTV_1.5","TLG_1.5","MTV_2.5","TLG_2.5","MTV_3.5","TLG_3.5","SUV_max","SUV_mean","SUV_max7_syn")]
yy = ex_normY[,c("MTV_0.5","TLG_0.5","MTV_1.5","TLG_1.5","MTV_2.5","TLG_2.5","MTV_3.5","TLG_3.5","SUV_max","SUV_mean","SUV_max7_gt")]

df2 <- cor(xx,yy, use = "na.or.complete")
corrplot(df2, is.corr = FALSE, , col.lim = c(0, 1),tl.col = "black")

############################# PROSPECT  ################################################

setwd("E:/papers/CT2PET/CorrelationCSVs/")
X_meta = read.csv("PROSPECT_Pred_MTV_TLG_pall.csv",sep=",",header = TRUE)
Y_meta = read.csv("PROSPECT_True_MTV_TLG_pall.csv",sep=",",header = TRUE)
X=X_meta[,3:12]
Y=Y_meta[,3:12]


clip_SUVmaxY = Y$SUV_max
clip_SUVmaxY[clip_SUVmaxY>7.0]=7.0
Y[["SUV_max7_gt"]] <- clip_SUVmaxY
X[["SUV_max7_syn"]] <- X$SUV_max


rownames(Y)=Y_meta$MRN
rownames(X)=X_meta$MRN

ex_Y <- log2(as.matrix(Y+1))  # remove duplicates
ex_Y1=data.frame(ex_Y)

ex_X <- log2(as.matrix(X+1))  # remove duplicates
ex_X1=data.frame(ex_X)
#apply Z-score normalization to fex
ex_normY <- as.data.frame(scale(ex_Y1[1:11]))
ex_normX <- as.data.frame(scale(ex_X1[1:11]))

rownames(ex_normY)=Y_meta$MRN      #print(colnames(Y_meta))
rownames(ex_normX)=X_meta$MRN   

xx = ex_normX[,c("MTV_0.5","TLG_0.5","MTV_1.5","TLG_1.5","MTV_2.5","TLG_2.5","MTV_3.5","TLG_3.5","SUV_max","SUV_mean","SUV_max7_syn")]
yy = ex_normY[,c("MTV_0.5","TLG_0.5","MTV_1.5","TLG_1.5","MTV_2.5","TLG_2.5","MTV_3.5","TLG_3.5","SUV_max","SUV_mean","SUV_max7_gt")]

df2 <- cor(xx,yy, use = "na.or.complete")
corrplot(df2, is.corr = FALSE, , col.lim = c(0, 1),tl.col = "black")

############################# ICON  ################################################
setwd("E:/papers/CT2PET/CorrelationCSVs/")
X_meta = read.csv("ICON_Pred_allMTV.csv",sep=",",header = TRUE)
Y_meta = read.csv("ICON_Truth_allMTV.csv",sep=",",header = TRUE)
X=X_meta[,3:12]
Y=Y_meta[,3:12]


clip_SUVmaxY = Y$SUV_max
clip_SUVmaxY[clip_SUVmaxY>7.0]=7.0
Y[["SUV_max7_gt"]] <- clip_SUVmaxY
X[["SUV_max7_syn"]] <- X$SUV_max


rownames(Y)=Y_meta$MRN
rownames(X)=X_meta$MRN

ex_Y <- log2(as.matrix(Y+1))  # remove duplicates
ex_Y1=data.frame(ex_Y)

ex_X <- log2(as.matrix(X+1))  # remove duplicates
ex_X1=data.frame(ex_X)
#apply Z-score normalization to fex
ex_normY <- as.data.frame(scale(ex_Y1[1:11]))
ex_normX <- as.data.frame(scale(ex_X1[1:11]))

rownames(ex_normY)=Y_meta$MRN      #print(colnames(Y_meta))
rownames(ex_normX)=X_meta$MRN   

xx = ex_normX[,c("MTV_0.5","TLG_0.5","MTV_1.5","TLG_1.5","MTV_2.5","TLG_2.5","MTV_3.5","TLG_3.5","SUV_max","SUV_mean","SUV_max7_syn")]
yy = ex_normY[,c("MTV_0.5","TLG_0.5","MTV_1.5","TLG_1.5","MTV_2.5","TLG_2.5","MTV_3.5","TLG_3.5","SUV_max","SUV_mean","SUV_max7_gt")]

df2 <- cor(xx,yy, use = "na.or.complete")
corrplot(df2, is.corr = FALSE, , col.lim = c(0, 1),tl.col = "black")
