# delete work space
rm(list = ls(all = TRUE))
graphics.off()

setwd("C:/Users/MSalehjahromi/Desktop/OS") 

library("survival")
library("survcomp")
library(survminer)

ICON <- read.csv(
  "ICON_Pred_allMTV.csv",
  header=TRUE)
ICON$OS <- ICON$OS/12

PROSPECT <- read.csv(
  "PROSPECT_Pred_MTV_TLG_pall.csv",
  header=TRUE)
# PROSPECT$OS <- PROSPECT$OS/365

TCIA <- read.csv(
  "TCIA_Pred_MTV_TLG_pall.csv",
  header=TRUE)
TCIA$OS <- TCIA$OS/365

HUGO <- read.csv(
  "HUGO_MTV_TLG_volume_PAll.csv",
  header=TRUE)
HUGO$OS <- HUGO$OS/12

trainData <- rbind(ICON[,c(6,14,15)],PROSPECT[,c(6,14,15)])
#trainData <- ICON[,c(4,14,15)]
trainPredictor <- as.data.frame(trainData[,1])
colnames(trainPredictor) <- c("MTV_2.5")

testData <- rbind(TCIA[,c(7,15,16)],HUGO[,c(9,17,18)])
#testData <- rbind(TCIA[,c(5,15,16)],HUGO[,c(3,17,18)],PROSPECT[,c(4,14,15)])
testPredictor <- as.data.frame(testData[,1])
colnames(testPredictor) <- c("MTV_2.5")

# train the model
model <- coxph(Surv(OS,OS_events) ~ MTV_2.5, data = trainData)
summary(model)

# ttrainPredictor <- as.data.frame(trainPredictor)
risk.train <- predict(model,newdata = trainPredictor,type="risk")
stratify.train <- factor(risk.train >= quantile(risk.train,0.50))
fit.train <- survfit(Surv(trainData$OS,trainData$OS_events) ~ stratify.train)

custom_theme <- function() {
  theme_survminer() %+replace%
    theme(
      plot.title=element_text(size = 14, color = "black",hjust=0.5,face = "bold"),
      axis.text.x = element_text(size = 14, color = "black", face = "bold"),
      legend.text = element_text(size = 14, color = "black", face = "bold"),
      legend.title = element_text(size = 14, color = "black", face = "bold"),
      axis.text.y = element_text(size = 14, color = "black", face = "bold"),
      axis.title.x = element_text(size = 14, color = "black", face = "bold"),
      axis.title.y = element_text(size = 14, color = "black", face = "bold") , #angle=(90))
    )
}

#           palette = c("#E7B800","#2E9FDF"),
ggsurvplot(fit.train, data = trainData,title = "Training",ggtheme=custom_theme(),
           conf.int = FALSE,
           pval = TRUE,
           fun = "pct",
           risk.table = TRUE,
           xlab = "Time (years)",
           ylab = "OS (%)",
           xlim = c(0, 5.5),
           #ylim = c(50,100),
           risk.table.fontsize =5,
           size = 1,
           linetype = "strata",
           
           palette = c("#00A878", "#FF0000"),
           
           risk.table.col = "strata",
           #legend = "bottom",
           legend.title = "Group",
           legend.labs = c("Low",
                           "High"))

# test the model
# ttestPredictor <- as.data.frame(testPredictor)
risk.test <- predict(model, newdata = testPredictor, type="risk")
stratify.test <- factor(risk.test >= quantile(risk.train,0.5))
stratify.test <- factor(risk.test >= quantile(risk.test,0.50))
fit.test <- survfit(Surv(testData$OS, testData$OS_events) ~ stratify.test)


ggsurvplot(fit.test, data = testData,title = "Testing",ggtheme=custom_theme(),
           conf.int = FALSE,
           pval = TRUE,
           fun = "pct",
           risk.table = TRUE,
           xlab = "Time (years)",
           ylab = "OS (%)",
           xlim = c(0, 10),
           risk.table.fontsize =5,
           size = 1,
           linetype = "strata",
           palette = c("#00A878", "#FF0000"),
           
           risk.table.col = "strata",
           #legend = "bottom",
           legend.title = "Group",
           legend.labs = c("Low",
                           "High"))