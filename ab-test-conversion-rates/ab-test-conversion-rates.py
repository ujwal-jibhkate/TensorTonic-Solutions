import math
from statistics import NormalDist

def ab_test_conversion(control_conversions: int, control_n: int, treatment_conversions: int, treatment_n: int, alpha: float = 0.05) -> dict:
    """
    Returns lift, z, p_value, ci_low, ci_high and significant for a two-proportion z-test.
    """
    control_rate = control_conversions / control_n
    treatment_rate = treatment_conversions / treatment_n
    lift = treatment_rate - control_rate

    total_conversions = control_conversions + treatment_conversions
    total_n = control_n + treatment_n
    pooled_rate = total_conversions / total_n

    if pooled_rate == 0.0 or pooled_rate == 1.0:
        return {
            "lift": lift,
            "z": 0.0,
            "p_value": 1.0,
            "ci_low": 0.0,
            "ci_high": 0.0,
            "significant": False
        }

    pooled_se = math.sqrt(pooled_rate * (1 - pooled_rate) * ((1 / control_n) + (1 / treatment_n)))
    z = lift / pooled_se

    p_value = math.erfc(abs(z) / math.sqrt(2))

    unpooled_se = math.sqrt(
        (control_rate * (1 - control_rate) / control_n) + 
        (treatment_rate * (1 - treatment_rate) / treatment_n)
    )
    quantile = NormalDist().inv_cdf(1 - alpha / 2)
    margin_of_error = quantile * unpooled_se

    ci_low = lift - margin_of_error
    ci_high = lift + margin_of_error

    significant = p_value < alpha

    return {
        "lift": lift,
        "z": z,
        "p_value": p_value,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "significant": significant
    }