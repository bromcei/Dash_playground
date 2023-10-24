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

    def check_2array_test(self, test_name, arr_1, arr_2):
        if test_name == self.two_ind_tests[0]:
            stat, p = mannwhitneyu(arr_1, arr_2)
            return stat, p
        if test_name == self.two_ind_tests[1]:
            stat, p = ttest_ind(arr_1, arr_2)
            return stat, p