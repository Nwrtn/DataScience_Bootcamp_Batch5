install.packages("mlbench")

library(tidyverse)
library(dplyr)
library(nnet)
library(NeuralNetTools)
library(mlbench)

data("BreastCancer")
data("BostonHousing")

head(BostonHousing)

## 1. Build Linear Regression
## predict medv (BostonHousing)


head(BostonHousing)

##medv = F(rm,dis,rad)
##medv = intercept + b1*rm + b2*dis + b3*rad

lmBH <- lm(medv ~ rm + dis + rad, data = BostonHousing)

coefsBH <- coef(lmBH)

##if rm = 7, dis = 5.50, rad = 3

coefsBH[[1]]+coefsBH[[2]]*7+coefsBH[[3]]*5.50+coefsBH[[4]]*3


BostonHousing$pred_medv <- predict(lmBH)


##RMSE Root Mean Square error

squared_errorBH <- (BostonHousing$medv - BostonHousing$pred_medv)**2

(rmseBH <- sqrt(mean(squared_errorBH)))




##Split data

set.seed(42)
n <- nrow(BostonHousing)
id <- sample(1:n, size = n*0.8)
train_dataBH <- BostonHousing[id, ]
test_dataBH <- BostonHousing[-id, ]


##train model

model1 <- lm(medv ~ rm + indus, data = BostonHousing)

pred_trainBH <- predict(model1)

error_trainBH <- train_dataBH$medv - train_dataBH$pred_medv

(rmseBH_train <- sqrt(mean(error_trainBH**2)))


##test model

pred_testBH <- predict(model1, newdata = test_dataBH)

error_testBH <- test_dataBH$medv - pred_testBH

(rmseBH_test <- sqrt(mean(error_testBH**2)))


##print result

cat("RMSE Train:", rmseBH_train,
    "\nRMSE Test:", rmseBH_test)


##_________________________________________




## 2. Build Logistic Regression
## predict class (BreastCancer)

head(BreastCancer)

str(BreastCancer)

class(BreastCancer$Class)

BreastCancer <- na.omit(BreastCancer)

##create frequency table

table(BreastCancer$Class)

BreastCancer <- BreastCancer %>%
  mutate(Class_label = ifelse(BreastCancer$Class == "malignant",1,0))
glimpse(BreastCancer)


##split data

set.seed(42)
nBC <- nrow(BreastCancer)
idBC <- sample(1:nBC, size = nBC*0.7)
trainBC <- BreastCancer[idBC, ]
testBC <- BreastCancer[-idBC, ]

##train model

logis_model <- glm(Class_label ~ Bl.cromatin,
                   data = trainBC,
                   family = "binomial")

pred_trainBC <- predict(logis_model, data = trainBC, type = "response")


trainBC$predClass <- ifelse(pred_trainBC >=0.5, 1,0)

##check accuracy of train model 0.9016736

trainBC$Class_label==trainBC$predClass

mean(trainBC$Class_label==trainBC$predClass)



##test model

pred_testBC <- predict(logis_model, newdata = testBC, type = "response")

testBC$predClass <- ifelse(pred_testBC >=0.5, 1,0)

##check accuracy of test model 0.9219512

testBC$Class_label==testBC$predClass

mean(testBC$Class_label==testBC$predClass)


##confusion matrix

confm <- table(testBC$Class_label, testBC$predClass,
               dnn = c("Actual","Predicted"))

## Model Evaluation

confm[1, 1]  #actual=0,predicted=0
confm[1, 2]  #actual=0,predicted=1
confm[2, 1]  #actual=1,predicted=0
confm[2, 2]  #actual=1,predicted=1


##accuracy 0.9219512

cat("Accuracy:", (confm[1, 1]+confm[2, 2])/ sum(confm))


##precision 0.8970588

cat("Precision:", confm[2, 2]/(confm[2, 2]+confm[1, 2]))


##recall 0.8714286

cat("Recall:", confm[2, 2] / (confm[2, 2] + confm[2, 1]))


#F1 = 2*((precision*recall)/(precision+recall)) = 0.884058

cat("F1:", 2*((0.8970588*0.8714286) / (0.8970588+0.8714286)))





##_________________________________________




## 3. Build Neural Network
## predict class (BreastCancer)


set.seed(42)
nBC <- nrow(BreastCancer)
idBC <- sample(1:nBC, size = nBC*0.7)
trainBC2 <- BreastCancer[idBC, ]
testBC2 <- BreastCancer[-idBC, ]

neunetBC <- nnet(Class ~ Bl.cromatin, data = trainBC2, size = 3)


#plot network

plotnet(neunetBC)


#show weights of model

summary(neunetBC)


#model evaluation

pBC <- predict(neunetBC, newdata = testBC2, type = "class")

mean(pBC == testBC2$Class)
