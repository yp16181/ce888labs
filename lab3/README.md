# Lab3



- [ ] Load the data from `bank-additional-full.csv`
- [ ] Use a classifier (anything, but `ExtraTreesClassifier` with 100 estimators is the easiest option) on the data with outcome/output variable "y"
![scaterplot](./2.png?raw=true)	
![scaterplot](./1.png?raw=true)	
*  Convert to dummies using `df_dummies = pd.get_dummies(df)`
* Columns "y_no" and "duration" must be deleted - use something like `del df_copy["attribute"]` for this
* Plot histogram of the label `y_yes`
* Get the values and run a classifier (with outcome `y_yes`)
* Report the results of 10-Kfold stratified cross-validation
* Get sample importances and a confusion matrix





