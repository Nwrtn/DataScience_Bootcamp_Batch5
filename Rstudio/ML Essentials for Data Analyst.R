##Pima Indians Diabetes

data("PimaIndiansDiabetes")


#check complete

df <- PimaIndiansDiabetes

mean(complete.cases(PimaIndiansDiabetes))


check_complete <- function(df) mean(complete.cases(df))

check_complete(df)

#glimpse data

glimpse(df)


#check distribution

df %>%
  count(diabetes)


df %>%
  count(diabetes)%>%
  mutate(pct = n/sum(n))

#in this case there is imbalance pct. Do not use accuracy value !




##Split data

set.seed(42)
id <- createDataPartition(y = df$diabetes,
                          p = 0.8,
                          list = FALSE)

train_df <- df[id, ]
test_df <- df[-id, ]

nrow(train_df)
nrow(test_df)


##Train model

set.seed(42)

ctrl <- trainControl(
  method = "cv",
  number = 5,
  verboseIter = TRUE
)


logis_model <- train(
  diabetes ~.,
  data = train_df,
  method = "glm",
  metric = "Accuracy",
  preProcess = c("center", "scale"),
  trControl = ctrl
)

#train model with method ramdomforest

set.seed(42)

ctrl <- trainControl(
  method = "cv",
  number = 5,
  verboseIter = TRUE
)


logis_model <- train(
  diabetes ~.,
  data = train_df,
  method = "rf",
  metric = "Accuracy",
  preProcess = c("center", "scale"),
  trControl = ctrl
)




#change metric=Accuracy to metric=ROC  #AUC

set.seed(42)

ctrl <- trainControl(
  method = "cv",
  number = 5,
  classProbs = TRUE,
  summaryFunction = twoClassSummary,
  verboseIter = TRUE
)


rf_model <- train(
  diabetes ~.,
  data = train_df,
  method = "rf",
  metric = "ROC",
  preProcess = c("center", "scale"),
  trControl = ctrl
)


## Test model
#prediction

p <- predict(rf_model, newdata = test_df)

mean(p == test_df$diabetes)



#confusionmatrix

confusionMatrix(p, test_df$diabetes)



#set possitive class
###Positive class should be value that interests us

confusionMatrix(p, test_df$diabetes,
                positive = "pos")


confusionMatrix(p, test_df$diabetes,
                positive = "pos",
                mode = "prec_recall")


#-----------------------------------

##Decision tree

df <- PimaIndiansDiabetes

glimpse(df)


##Split data

set.seed(42)
id <- createDataPartition(y = df$diabetes,
                          p = 0.8,
                          list = FALSE)

train_df <- df[id, ]
test_df <- df[-id, ]


##Train model

#tune length #tune capacity parameter or cp
set.seed(99)
tree_model <- train(diabetes ~ .,
                    data = train_df,
                    method = "rpart",
                    tuneLength = 10,
                    trControl = trainControl(
                      method = "cv",
                      number = 5
                    ))

#tunegrid #cp = seq(0.001, 0.3, by = 0.005)

set.seed(99)
myGrid <- data.frame(cp = seq(0.001, 0.3, by = 0.005))
tree_model <- train(diabetes ~ .,
                    data = train_df,
                    method = "rpart",
                    tuneGrid = myGrid,
                    trControl = trainControl(
                      method = "cv",
                      number = 5
                    ))



##Plot graph with rpart.plot

library(rpart.plot)

rpart.plot(tree_model$finalModel)



##random forest from tree model

library(MLmetrics)

set.seed(99)

myGridrf <- data.frame(mtry = 2:7)

rf_model <- train(diabetes ~ .,
                    data = train_df,
                    method = "rf",
                    metric = "AUC",
                    tuneGrid = myGridrf,
                    trControl = trainControl(
                      method = "cv",
                      number = 5,
                      verboseIter = TRUE,
                      classProbs = TRUE,
                      summaryFunction = prSummary
                    ))

##normalize features

set.seed(99)

myGridrf <- data.frame(mtry = 2:7)

rf_model <- train(diabetes ~ .,
                  data = train_df,
                  method = "rf",
                  metric = "AUC",
                  preProcess = c("center", "scale", "nzv"),
                  tuneGrid = myGridrf,
                  trControl = trainControl(
                    method = "cv",
                    number = 5,
                    verboseIter = TRUE,
                    classProbs = TRUE,
                    summaryFunction = prSummary
                  ))


##Test Model

p <- predict(rf_model, newdata = test_df)

confusionMatrix(p, test_df$diabetes,
                mode = "prec_recall",
                positive = "pos")

#----------------------------------------------------

##Ridge / Lasso Regression

df %>% glimpse()



##train model
##help with overfitting
##alpha=0 ridge
##alpha=1 lasso


set.seed(42)

myGridridgelasso <- expand.grid(alpha = 0:1,
                                lambda = seq(0.001, 1, length = 20 ))

regularized_model <- train(
  diabetes ~ .,
  data = train_df,
  method = "glmnet",
  tuneGrid = myGridridgelasso,
  trControl = trainControl(
    method = "cv",
    number = 5,
    verboseIter = TRUE
  )
)


regularized_model


##test model

p <- predict(regularized_model, newdata = test_df)

confusionMatrix(p, test_df$diabetes,
                mode = "prec_recall",
                positive = "pos")








