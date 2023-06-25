import sys
import pandas as pd
import numpy as np
from scipy import stats

OUTPUT_TEMPLATE = (
    '"Did more/less users use the search feature?" p-value:  {more_users_p:.3g}\n'
    '"Did users search more/less?" p-value:  {more_searches_p:.3g}\n'
    '"Did more/less instructors use the search feature?" p-value:  {more_instr_p:.3g}\n'
    '"Did instructors search more/less?" p-value:  {more_instr_searches_p:.3g}'
)


def perform_ab_analysis(data):
    control_group = data[data['uid'] % 2 == 0]
    treatment_group = data[data['uid'] % 2 != 0]

    control_users_with_search = (control_group['search_count'] > 0).sum()
    treatment_users_with_search = (treatment_group['search_count'] > 0).sum()
    contingency_table_q1 = pd.crosstab(index=[control_users_with_search, treatment_users_with_search],
                                       columns=[len(control_group), len(treatment_group)])
    _, more_users_p = stats.chi2_contingency(contingency_table_q1, correction=False)[:2]

    control_search_counts = control_group['search_count']
    treatment_search_counts = treatment_group['search_count']
    _, more_searches_p = stats.mannwhitneyu(control_search_counts, treatment_search_counts, alternative='two-sided')

    control_instructors = control_group[control_group['is_instructor']]
    treatment_instructors = treatment_group[treatment_group['is_instructor']]

    control_instr_with_search = (control_instructors['search_count'] > 0).sum()
    treatment_instr_with_search = (treatment_instructors['search_count'] > 0).sum()
    contingency_table_q3 = pd.crosstab(index=[control_instr_with_search, treatment_instr_with_search],
                                       columns=[len(control_instructors), len(treatment_instructors)])
    _, more_instr_p = stats.chi2_contingency(contingency_table_q3, correction=False)[:2]

    control_instr_search_counts = control_instructors['search_count']
    treatment_instr_search_counts = treatment_instructors['search_count']
    _, more_instr_searches_p = stats.mannwhitneyu(control_instr_search_counts, treatment_instr_search_counts,
                                                 alternative='two-sided')

    return more_users_p, more_searches_p, more_instr_p, more_instr_searches_p


def main():
    
    input_file = sys.argv[1]

    data = pd.read_json(input_file, orient='records', lines=True)

    # Perform A/B analysis
    more_users_p, more_searches_p, more_instr_p, more_instr_searches_p = perform_ab_analysis(data)

    # Output
    print(OUTPUT_TEMPLATE.format(
        more_users_p=more_users_p,
        more_searches_p=more_searches_p,
        more_instr_p=more_instr_p,
        more_instr_searches_p=more_instr_searches_p,
    ))


if __name__ == '__main__':
    main()
