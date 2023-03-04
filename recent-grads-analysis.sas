/* Generated Code (IMPORT) */
/* Source File: recentgrad(SAS Project Information).csv */
/*SourceFile Download Link: https://github.com/fivethirtyeight/data/blob/master/college-majors/recent-grads.csv
/* Source Path: /home/u61332145/sasuser.v94 */
/* Code generated on: 4/30/22, 10:31 PM */

%web_drop_table(WORK.IMPORT);
FILENAME REFFILE 
	'/home/u61332145/sasuser.v94/recentgrad(SAS Project Information).csv';

PROC IMPORT DATAFILE=REFFILE DBMS=CSV OUT=WORK.IMPORT;
	GETNAMES=YES;
RUN;

PROC CONTENTS DATA=WORK.IMPORT;
RUN;

%web_open_table(WORK.IMPORT);

Proc means data=Import Mean Std max q1 median q3 min maxdec=2;
	Var College_jobs Non_college_jobs low_wage_jobs Employed;
Run;

Title "Figure 1: Histogram of Number of college jobs for Recent Grad Survey (n=173)";

Proc sgplot data=import;
	histogram college_jobs;
	Xaxis label="Number of People";
Run;

Proc sgplot data=import;
	title1 "Figure 2: Boxplot of Number of college_jobs for Recent Grad Survey (n=173)";
	vbox college_jobs;
	yaxis label="Number of People" valueshint min=-2 max=15000;
Run;

Title "Figure 3: Histogram of Number of Non college jobs for Recent Grad Survey (n=173)";

Proc sgplot data=import;
	histogram non_college_jobs;
	Xaxis label="Number of People";
Run;

Proc sgplot data=import;
	title1 "Figure 4: Boxplot of Number of non college jobs for Recent Grad Survey (n=173)";
	vbox non_college_jobs;
	yaxis label="Number of People" valueshint min=-2 max=15000;
Run;

Title 
	"Figure 5: Histogram of Low Wage Employees for Recent Grad Survey (n=173)";

Proc sgplot data=import;
	histogram low_wage_jobs;
	Xaxis label="Number of People";
Run;

Proc sgplot data=import;
	title1 "Figure 6: Boxplot of Low Wage Employees for Recent Grad Survey (n=173)";
	vbox low_wage_jobs;
	yaxis label="Number of People" valueshint min=-2 max=15000;
Run;

Proc Freq data=import;
	Tables Major Major_Category;
Run;
* The issue with a pie and bar chart for these variables is that every major
Only happens once in the dataset therefore the pie and bar would both be equal
;
Title "Figure 7: Pie Chart of Major of Recent Grad Survey (n=173)";

Proc template;
	define statgraph pie;
		begingraph;
		layout region;
		piechart category=Major / Datalabellocation=inside datalabelcontent=all 
			categorydirection=clockwise Start=180 Name="pie";
		discretelegend='pie' / Title='Major';
		Endlayout;
		Endgraph;
	End;
Run;

Proc sgrender data=import template=pie;
run;

Title;

Proc sgplot data=import;
	title 'Figure 8: Bar chart of Major for Recent Grad Survey (n=173)';
	vbar=Major;
	xaxis label='Major';
Run;
Title "Figure 9: Pie Chart of Major of Recent Grad Survey (n=173)";

Proc template;
	define statgraph pie;
		begingraph;
		layout region;
		piechart category=Major_category / Datalabellocation=inside datalabelcontent=all 
			categorydirection=clockwise Start=180 Name="pie";
		discretelegend='pie' / Title='Major';
		Endlayout;
		Endgraph;
	End;
Run;

Proc sgrender data=import template=pie;
run;

Title;

Proc sgplot data=import;
	title 'Figure 10: Bar chart of Major for Recent Grad Survey (n=173)';
	vbar=Major_category;
	xaxis label='Major';
Run;
Data import;
Set import;
If college_jobs<1000 then collegeJobAp = "Less than 1000";
Else if college_jobs>=1000 and college_jobs <= 5000 then collegeJobAp = "Between 1000 and 5000";
Else if college_jobs >5000 then collegeJobAp = "Greater than 5000";
Run;
Proc Freq data=import;
	Tables collegeJobAp;
	Title"Table 3: Frequency Table of students in college jobs in recent grad survey (n=173)";
Run;
Title "Figure 11: College Job Distribution of College grad survey (n=173)";
Proc template;
Define STATGRAPH pie;
	begingraph;
		layout region;
			Piechart category = collegeJobAp /
			datalabellocation=inside
			datalabelcontent=all
			categorydirection=clockwise
			Start=180 Name='pie';
			Discretelegend'pie'/
			Title='College Jobs';
		Endlayout;
	Endgraph;
End;
Run;
Proc sgrender Data=import
template=pie;
Run;
Title;
Proc sgplot data=import;
	title'Bar Chart of College Job for College Grad Survey (n=173)'
	vbar = collegeJobAp;
	xaxis label= 'Number of People';
	Run;
	*Insufficent data to produce a plot;
Proc Means data=import Mean std max q1 median q3 min maxdec=2;
Var Unemployed Employed Full_Time Total;
Class Major Major_Category;
Run;
Proc sort data=import;
By Major;
Run;
Title "Figure X: Histogram of College Jobs by Major Category for Recent Job Survey (n=173)";
proc sgplot data=import;
histogram college_jobs / group=major_category transparency= 0.5 scale=count;
density college_jobs / type=normal group=major_category;
keylegend / location=inside position = topright across = 1;
Xaxis label= "Number of People";
Yaxis label= "Number of Majors";
run;
title;
Proc freq data=import;
	Tables Major_Category*Major;
Run;


Title1 "Figure 12: 100% Stacked bar Chart for Recent Job Survey (n=173)";
proc sgplot data=import pctlevel=group;
vbar major_category / group=major stat=pct seglabel;
run;
Proc Means data=import Mean std max q1 median q3 min maxdec=2;
Var college_jobs;
Class Major_Category;
Run;
Proc sgplot data=import;
	Title1 'Side by Side Boxplots of Major Category';
	Title2 'By College Jobs';
	vbox college_jobs / category=major_category;
	yaxis label= 'Major Category' valueshint min=2 max = 15000;
	Run;
	title;

proc sgplot data= import;
	Title 'Scatterplot of college jobs by non college jobs (n=173)';
	reg x = college_jobs y = non_college_jobs / ClM CLI;
	Xaxis label= "number of college jobs";
	Yaxis Label= "number of non college jobs";
Run;
Proc Corr Data=import;
Var college_jobs;
with non_college_jobs;
Title "Table 6: Correlation Coefficent of college jobs by non_college jobs";
rUN;
