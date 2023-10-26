from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy.stats import mannwhitneyu
from scipy.stats import wilcoxon



class StatsCalc():
    def __init__(self):
        self.two_ind_tests = ["ttest_ind", "mannwhitneyu"]

    def get_two_ind_tests(self):
        return self.two_ind_tests
    def check_norm_dist(self, arr_1, arr_2):
        cat_1_norm_test, cat_1_norm_p = normaltest(arr_1)
        cat_2_norm_test, cat_2_norm_p = normaltest(arr_2)
        return cat_1_norm_test, cat_1_norm_p, cat_2_norm_test, cat_2_norm_p

    def get_hypothesis_by_test_name(self, test_name):
        if test_name == self.two_ind_tests[0]:
            hypothesis = [
                "1. H0: the means of the samples are equal.",
                "2. H1: the means of the samples are unequal."]
            return hypothesis

        if test_name == self.two_ind_tests[1]:
            hypothesis = [
                "1. H0: the distributions of both samples are equal",
                "2. H1: the distributions of both samples are not equal."]
            return hypothesis

    def check_2array_test(self, test_name, arr_1, arr_2):
        if test_name == self.two_ind_tests[0]:
            stat, p = ttest_ind(arr_1, arr_2)
            if p > 0.05:
                hypothesis_result = f"Probably the same mean. Stat={stat}, p_score={p}"
            else:
                hypothesis_result = f"Probably NOT the same mean. Stat={stat}, p_score={p}"
            return hypothesis_result

        if test_name == self.two_ind_tests[1]:
            stat, p = mannwhitneyu(arr_1, arr_2)
            if p > 0.05:
                hypothesis_result = f"Probably the same distribution. Stat={stat}, p_score={p}"
            else:
                hypothesis_result = f"Probably NOT the same distribution. Stat={stat}, p_score={p}"
            return hypothesis_result
