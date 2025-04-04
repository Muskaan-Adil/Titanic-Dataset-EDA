### Detailed Report

---

#### 1. **Basic Data Inspection**:
To start, I took a look at the basic structure of the dataset. I printed out the first and last five rows to ensure the data was loaded correctly and to get a sense of its content. I also checked the dataset's **columns** to confirm the available features and used the `info()` method to inspect the data types and missing values. The `describe()` method gave me a summary of the numerical features, which helped me understand the range and distribution of values like `Age` and `Fare`.

#### 2. **Missing Values**:
I examined the dataset for any missing values, which could affect the analysis or model performance. By using `isnull().sum()`, I identified which columns had missing values. I also visualized missing data using the `missingno` library’s matrix plot to get a better understanding of the missing data patterns across the dataset.

#### 3. **Distribution of Numerical Features**:
Next, I analyzed the distribution of key numerical features: `Age` and `Fare`. For both of these, I used **histograms with KDE** to visualize their distributions. This helped me see how the values of these variables are spread out and whether there were any significant outliers. For instance, the `Age` distribution appeared to be relatively normal, while the `Fare` distribution was skewed right, indicating some passengers paid significantly higher fares.

#### 4. **Visualizing Categorical Variables**:
To understand the distribution of categorical features like `Sex` and `Embarked`, I used **count plots**. These plots helped me visualize how many male and female passengers were present, and also how passengers were distributed across the three embarkation points (`C`, `Q`, `S`).

#### 5. **Relationship Between Age and Survival**:
I was interested in seeing how survival was related to age, so I created a **boxplot** to compare the distribution of `Age` between survivors and non-survivors. From this plot, I observed that the survival rates did not significantly differ by age; however, younger passengers did seem to have a slightly higher chance of survival.

#### 6. **Relationship Between Pclass and Survival**:
Next, I explored whether passenger class (`Pclass`) affected survival rates. I used a **count plot** to show the distribution of survival by class. The plot clearly showed that first-class passengers had the highest survival rate, followed by second and third-class passengers.

#### 7. **Correlation Matrix**:
Finally, I wanted to understand the relationships between the numerical features. Using a **correlation matrix** (via a heatmap), I identified that `SibSp` and `Parch` (family size) were positively correlated, while other features like `Age` and `Fare` showed weak or no significant correlations. This matrix gave me insights into which features might be important for further analysis or modeling.

---

### Final Thoughts:
This EDA provided a solid foundation for understanding the dataset, visualizing key variables, and identifying any data issues (like missing values). The next steps could involve handling the missing data, feature engineering, or even moving forward with building a predictive model if needed.