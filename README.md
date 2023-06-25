## AB-Analyze

AB-Analyze is a Python program designed to perform A/B analysis on user search behavior, comparing the effectiveness of two different interface designs. The program utilizes data from the provided `searches.json` file to analyze user engagement and calculate p-values for differences in search feature usage and search frequency. Additionally, it includes an analysis specifically focused on instructors.

### Problem

The main problem addressed by AB-Analyze is to determine whether the new design of the search feature has a significant impact on user behavior compared to the original design. The program aims to answer two key questions:

1. Did more users engage with the search feature when presented with the new design?
2. Did users who were exposed to the new design perform more searches compared to those who experienced the original design?

### Approach

AB-Analyze follows a systematic approach to conduct the A/B analysis. The program implements the following steps:

1. Load the provided `searches.json` file using Pandas, orienting the data as records.
2. Split the users into two groups based on their unique user IDs (UID): those with odd-numbered UIDs represent the treatment group exposed to the new design, while those with even-numbered UIDs form the control group using the original design.
3. Analyze the proportion of users who engaged with the search feature in each group. This involves calculating the fraction of users with a search count greater than zero.
4. Determine if there is a significant difference in search feature engagement between the treatment and control groups using a nonparametric test, such as the chi-square test or Fisher's exact test.
5. Calculate the number of searches per user for each group.
6. Perform a nonparametric test, such as the Mann-Whitney U test, to assess if there is a significant difference in search frequency between the treatment and control groups.
7. Repeat the above analyses specifically for the subgroup of instructors within the dataset.
8. Report the p-values obtained from the statistical tests conducted in a consistent output format.

### Usage

To use AB-Analyze, follow these steps:

1. Ensure you have Python 3 installed on your system.
2. Clone the AB-Analyze repository to your local machine.
3. Install the necessary dependencies by running `pip install -r requirements.txt`.
4. Run the `ab_analysis.py` script, providing the path to the `searches.json` file as a command-line argument.
   ```
   python ab_analysis.py searches.json
   ```
5. The program will perform the A/B analysis and display the p-values for search feature engagement and search frequency differences.
6. Review the output and interpret the results to draw conclusions about the impact of the new design on user search behavior.

### Results

AB-Analyze generates p-values for the different analyses conducted. These p-values provide a measure of the statistical significance of any observed differences between the treatment and control groups. By comparing the p-values against a pre-defined significance level (e.g., 0.05), you can determine if the differences in search feature engagement and search frequency are statistically significant.

### Conclusion

AB-Analyze offers a practical solution for evaluating the impact of interface design changes using A/B analysis. By analyzing user search behavior, the program enables data-driven decision-making in the realm of user interface optimization. Whether you're a UX designer, product manager, or researcher, AB-Analyze can provide valuable insights into the effectiveness of interface modifications.
