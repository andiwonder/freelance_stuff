from django.db import models
from datetime import datetime

# Create your models here.
class NAIC_Sub_Industry_Code_11(models.Model):
  class_code = models.IntegerField(blank=False)
  class_sub_code = models.IntegerField(blank=False, db_index=True)
  industry = models.CharField(max_length=200)
  class Meta:
    db_table = "11_NAIC_SUB_INDUSTRY_CODE"

class NAIC_Sub_Industry_Code_54(models.Model):
  class_code = models.IntegerField(blank=False)
  class_sub_code = models.IntegerField(blank=False, db_index=True)
  industry = models.CharField(max_length=200)
  class Meta:
    db_table = "54_NAIC_SUB_INDUSTRY_CODE"   

class EO_Pricing_Model_Base_Rate(models.Model):
  annual_sales = models.FloatField(blank=False, db_index=True)
  base_rate = models.FloatField(blank=False)
  class Meta:
    db_table = "EO_PRICING_MODEL_BASE_RATE"

class EO_Pricing_Model_Deductible(models.Model):
  deductible_amount = models.IntegerField(blank=False, db_index=True)
  multiplier = models.FloatField(blank=False)
  class Meta:
    db_table = "EO_PRICING_MODEL_DEDUCTIBLE"

class EO_Pricing_Model_Limit(models.Model):
  occurence_limit = models.IntegerField(blank=False, db_index=True)
  increased_limit_factor = models.FloatField(blank=False)
  class Meta:
    db_table = "EO_PRICING_MODEL_LIMIT"

class EO_Pricing_Model_Marginal(models.Model):
  annual_sales = models.FloatField(blank=False, db_index=True)
  marginal_price = models.FloatField(blank=False)
  class Meta:
    db_table = "EO_PRICING_MODEL_MARGINAL"

class Errors_Omissions_Policy_Details(models.Model):
  class_sub_code = models.IntegerField(blank=False, db_index=True)
  need_for_policy = models.CharField(max_length=200, blank=False)
  placeholder = models.CharField(max_length=200, blank=False)
  class Meta:
    db_table = "ERRORS_OMISSIONS_POLICY_DETAILS"

class Hazard_Rate_Multiplier(models.Model):
  hazard_level_rating =  models.IntegerField(blank=False, db_index=True)
  rate_multiplier = models.FloatField(blank=False)
  class Meta:
    db_table = "HAZARD_RATE_MULTIPLIER"

class NAIC_Industry_Code(models.Model):
  class_code = models.IntegerField(blank=False, db_index=True)
  industry = models.CharField(max_length=200, blank=False)
  class Meta:
    db_table = "NAIC_INDUSTRY_CODE"

class NAIC_Sub_Industry_Hazard_Rating(models.Model):
  class_sub_code = models.IntegerField(blank=False, db_index=True)
  hazard_level_rating = models.IntegerField(blank=False)
  class Meta:
    db_table = "NAIC_SUB_INDUSTRY_HAZARD_RATING"

class BOP_EnEnhancements(models.Model):
  naic = models.IntegerField(blank=False, null=False)
  enhance1  = models.CharField(max_length=200, blank=True)
  enhance2  = models.CharField(max_length=200, blank=True)
  enhance3  = models.CharField(max_length=200, blank=True)
  enhance4  = models.CharField(max_length=200, blank=True)
  enhance5  = models.CharField(max_length=200, blank=True)
  enhance6  = models.CharField(max_length=200, blank=True)
  enhance7  = models.CharField(max_length=200, blank=True)
  enhance8  = models.CharField(max_length=200, blank=True)
  enhance9  = models.CharField(max_length=200, blank=True)
  enhance10 = models.CharField(max_length=200, blank=True)
  enhance11 = models.CharField(max_length=200, blank=True)
  enhance12 = models.CharField(max_length=200, blank=True)
  enhance13 = models.CharField(max_length=200, blank=True)
  enhance14 = models.CharField(max_length=200, blank=True)
  enhance15 = models.CharField(max_length=200, blank=True)
  class Meta:
    db_table = "BOP_Naic_Policy_Enhancements"

class BOP_Examples(models.Model):
  naic = models.IntegerField(null = False)
  example = models.CharField(max_length=500, null = False)
  class Meta:
    db_table = "BOP_Naic_Policy_Examples"

class BOP_Exclusions(models.Model):
  naic = models.IntegerField(null = False)
  exclusion1 = models.CharField(max_length=200, null=False, blank=True)
  exclusion2 = models.CharField(max_length=200, null=False, blank=True)
  exclusion3 = models.CharField(max_length=200, null=False, blank=True)
  exclusion4 = models.CharField(max_length=200, null=False, blank=True)
  exclusion5 = models.CharField(max_length=200, null=False, blank=True)
  exclusion6 = models.CharField(max_length=200, null=False, blank=True)
  exclusion7 = models.CharField(max_length=200, null=False, blank=True)
  exclusion8 = models.CharField(max_length=200, null=False, blank=True)
  exclusion9 = models.CharField(max_length=200, null=False, blank=True)
  exclusion10 = models.CharField(max_length=200, null=False, blank=True)
  exclusion11 = models.CharField(max_length=200, null=False, blank=True)
  exclusion12 = models.CharField(max_length=200, null=False, blank=True)
  exclusion13 = models.CharField(max_length=200, null=False, blank=True)
  exclusion14 = models.CharField(max_length=200, null=False, blank=True)
  exclusion15 = models.CharField(max_length=200, null=False, blank=True)
  BOP_Dummy = models.CharField(max_length=200, null=False, blank=True)
  class Meta:
    db_table = "BOP_Naic_Policy_Exclusions"

class CV_Enhancements(models.Model):
  naic = models.IntegerField(blank=False, null=False)
  enhance1  = models.CharField(max_length=200, blank=True)
  enhance2  = models.CharField(max_length=200, blank=True)
  enhance3  = models.CharField(max_length=200, blank=True)
  enhance4  = models.CharField(max_length=200, blank=True)
  enhance5  = models.CharField(max_length=200, blank=True)
  enhance6  = models.CharField(max_length=200, blank=True)
  enhance7  = models.CharField(max_length=200, blank=True)
  enhance8  = models.CharField(max_length=200, blank=True)
  enhance9  = models.CharField(max_length=200, blank=True)
  enhance10 = models.CharField(max_length=200, blank=True)
  enhance11 = models.CharField(max_length=200, blank=True)
  enhance12 = models.CharField(max_length=200, blank=True)
  enhance13 = models.CharField(max_length=200, blank=True)
  enhance14 = models.CharField(max_length=200, blank=True)
  enhance15 = models.CharField(max_length=200, blank=True)
  class Meta:
    db_table = "CV_Naic_Policy_Enhancements"

class CV_Examples(models.Model):
  naic = models.IntegerField(null = False)
  example = models.CharField(max_length=500, null = False)
  class Meta:
    db_table = "CV_Naic_Policy_Examples"

class CV_Exclusions(models.Model):
  naic = models.IntegerField(null = False)
  exclusion1 = models.CharField(max_length=200, null=False, blank=True)
  exclusion2 = models.CharField(max_length=200, null=False, blank=True)
  exclusion3 = models.CharField(max_length=200, null=False, blank=True)
  exclusion4 = models.CharField(max_length=200, null=False, blank=True)
  exclusion5 = models.CharField(max_length=200, null=False, blank=True)
  exclusion6 = models.CharField(max_length=200, null=False, blank=True)
  exclusion7 = models.CharField(max_length=200, null=False, blank=True)
  exclusion8 = models.CharField(max_length=200, null=False, blank=True)
  exclusion9 = models.CharField(max_length=200, null=False, blank=True)
  exclusion10 = models.CharField(max_length=200, null=False, blank=True)
  exclusion11 = models.CharField(max_length=200, null=False, blank=True)
  exclusion12 = models.CharField(max_length=200, null=False, blank=True)
  exclusion13 = models.CharField(max_length=200, null=False, blank=True)
  exclusion14 = models.CharField(max_length=200, null=False, blank=True)
  exclusion15 = models.CharField(max_length=200, null=False, blank=True)
  CV_Dummy = models.CharField(max_length=200, null=False, blank=True)
  class Meta:
    db_table = "CV_Naic_Policy_Exclusions"

class CY_Base_Rate_1st_Party(models.Model):
  coverage_limit = models.IntegerField(null = False)
  base_rate = models.IntegerField(null = False)
  class Meta:
    db_table = "CY_Base_Rate_1st_Party"

class CY_Base_Rate_3rd_Party(models.Model):
  coverage_limit = models.IntegerField(null = False)
  base_rate = models.IntegerField(null = False)
  class Meta:
    db_table = "CY_Base_Rate_3rd_Party"

class CY_Deductible_Factor(models.Model):
  deductible_amount = models.IntegerField(null = False)
  deductible_factor = models.FloatField(null = False)
  class Meta:
    db_table = "CY_Deductible_Factor"

class CY_Hazard_Rate_Multiplier(models.Model):
  hazard_level_rating =  models.IntegerField(blank=False, db_index=True)
  rate_multiplier = models.FloatField(blank=False)
  class Meta:
    db_table = "CY_Hazard_Rate_Multiplier"

class CY_Increased_Limit_Factor_1st_Party(models.Model):
  data_breach_expense_limit = models.IntegerField(null = False)
  increased_limit_factor = models.FloatField(null = False)
  class Meta:
    db_table = "CY_Increased_Limit_Factor_1st_Party"

class CY_Increased_Limit_Factor_3rd_Party(models.Model):
  data_breach_expense_limit = models.IntegerField(null = False)
  increased_limit_factor = models.FloatField(null = False)
  class Meta:
    db_table = "CY_Increased_Limit_Factor_3rd_Party"

class CY_Naic_Industry_Hazard_Rating(models.Model):
  naic_code = models.IntegerField(null = False)
  hazard_level_rating = models.IntegerField(null = False)
  class Meta:
    db_table = "CY_Naic_Industry_Hazard_Rating"

class CY_Enhancements(models.Model):
  naic = models.IntegerField(blank=False, null=False)
  enhance1  = models.CharField(max_length=200, blank=True)
  enhance2  = models.CharField(max_length=200, blank=True)
  enhance3  = models.CharField(max_length=200, blank=True)
  enhance4  = models.CharField(max_length=200, blank=True)
  enhance5  = models.CharField(max_length=200, blank=True)
  enhance6  = models.CharField(max_length=200, blank=True)
  enhance7  = models.CharField(max_length=200, blank=True)
  enhance8  = models.CharField(max_length=200, blank=True)
  enhance9  = models.CharField(max_length=200, blank=True)
  enhance10 = models.CharField(max_length=200, blank=True)
  enhance11 = models.CharField(max_length=200, blank=True)
  enhance12 = models.CharField(max_length=200, blank=True)
  enhance13 = models.CharField(max_length=200, blank=True)
  enhance14 = models.CharField(max_length=200, blank=True)
  enhance15 = models.CharField(max_length=200, blank=True)
  class Meta:
    db_table = "CY_Naic_Policy_Enhancements"

class CY_Examples(models.Model):
  naic = models.IntegerField(null = False)
  example = models.CharField(max_length=500, null = False)
  class Meta:
    db_table = "CY_Naic_Policy_Examples"

class CY_Exclusions(models.Model):
  naic = models.IntegerField(null = False)
  exclusion1 = models.CharField(max_length=200, null=False, blank=True)
  exclusion2 = models.CharField(max_length=200, null=False, blank=True)
  exclusion3 = models.CharField(max_length=200, null=False, blank=True)
  exclusion4 = models.CharField(max_length=200, null=False, blank=True)
  exclusion5 = models.CharField(max_length=200, null=False, blank=True)
  exclusion6 = models.CharField(max_length=200, null=False, blank=True)
  exclusion7 = models.CharField(max_length=200, null=False, blank=True)
  exclusion8 = models.CharField(max_length=200, null=False, blank=True)
  exclusion9 = models.CharField(max_length=200, null=False, blank=True)
  exclusion10 = models.CharField(max_length=200, null=False, blank=True)
  exclusion11 = models.CharField(max_length=200, null=False, blank=True)
  exclusion12 = models.CharField(max_length=200, null=False, blank=True)
  exclusion13 = models.CharField(max_length=200, null=False, blank=True)
  exclusion14 = models.CharField(max_length=200, null=False, blank=True)
  exclusion15 = models.CharField(max_length=200, null=False, blank=True)
  CY_Dummy = models.CharField(max_length=200, null=False, blank=True)
  class Meta:
    db_table = "CY_Naic_Policy_Exclusions"

class DO_Enhancements(models.Model):
  naic = models.IntegerField(blank=False, null=False)
  enhance1  = models.CharField(max_length=200, blank=True)
  enhance2  = models.CharField(max_length=200, blank=True)
  enhance3  = models.CharField(max_length=200, blank=True)
  enhance4  = models.CharField(max_length=200, blank=True)
  enhance5  = models.CharField(max_length=200, blank=True)
  enhance6  = models.CharField(max_length=200, blank=True)
  enhance7  = models.CharField(max_length=200, blank=True)
  enhance8  = models.CharField(max_length=200, blank=True)
  enhance9  = models.CharField(max_length=200, blank=True)
  enhance10 = models.CharField(max_length=200, blank=True)
  enhance11 = models.CharField(max_length=200, blank=True)
  enhance12 = models.CharField(max_length=200, blank=True)
  enhance13 = models.CharField(max_length=200, blank=True)
  enhance14 = models.CharField(max_length=200, blank=True)
  enhance15 = models.CharField(max_length=200, blank=True)
  class Meta:
    db_table = "DO_Naic_Policy_Enhancements"

class DO_Examples(models.Model):
  naic = models.IntegerField(null = False)
  example = models.CharField(max_length=500, null = False)
  class Meta:
    db_table = "DO_Naic_Policy_Examples"

class DO_Exclusions(models.Model):
  naic = models.IntegerField(null = False)
  exclusion1 = models.CharField(max_length=200, null=False, blank=True)
  exclusion2 = models.CharField(max_length=200, null=False, blank=True)
  exclusion3 = models.CharField(max_length=200, null=False, blank=True)
  exclusion4 = models.CharField(max_length=200, null=False, blank=True)
  exclusion5 = models.CharField(max_length=200, null=False, blank=True)
  exclusion6 = models.CharField(max_length=200, null=False, blank=True)
  exclusion7 = models.CharField(max_length=200, null=False, blank=True)
  exclusion8 = models.CharField(max_length=200, null=False, blank=True)
  exclusion9 = models.CharField(max_length=200, null=False, blank=True)
  exclusion10 = models.CharField(max_length=200, null=False, blank=True)
  exclusion11 = models.CharField(max_length=200, null=False, blank=True)
  exclusion12 = models.CharField(max_length=200, null=False, blank=True)
  exclusion13 = models.CharField(max_length=200, null=False, blank=True)
  exclusion14 = models.CharField(max_length=200, null=False, blank=True)
  exclusion15 = models.CharField(max_length=200, null=False, blank=True)
  DO_Dummy = models.CharField(max_length=200, null=False, blank=True)
  class Meta:
    db_table = "DO_Naic_Policy_Exclusions"

class EO_Enhancements(models.Model):
  naic = models.IntegerField(blank=False, null = False)
  enhance1  = models.CharField(max_length=200, blank=True)
  enhance2  = models.CharField(max_length=200, blank=True)
  enhance3  = models.CharField(max_length=200, blank=True)
  enhance4  = models.CharField(max_length=200, blank=True)
  enhance5  = models.CharField(max_length=200, blank=True)
  enhance6  = models.CharField(max_length=200, blank=True)
  enhance7  = models.CharField(max_length=200, blank=True)
  enhance8  = models.CharField(max_length=200, blank=True)
  enhance9  = models.CharField(max_length=200, blank=True)
  enhance10 = models.CharField(max_length=200, blank=True)
  enhance11 = models.CharField(max_length=200, blank=True)
  enhance12 = models.CharField(max_length=200, blank=True)
  enhance13 = models.CharField(max_length=200, blank=True)
  enhance14 = models.CharField(max_length=200, blank=True)
  enhance15 = models.CharField(max_length=200, blank=True)
  class Meta:
    db_table = "EO_Naic_Policy_Enhancements"

class EO_Examples(models.Model):
  naic = models.IntegerField(null = False)
  example = models.CharField(max_length=500, null = False)
  class Meta:
    db_table = "EO_Naic_Policy_Examples"

class EO_Exclusions(models.Model):
  naic = models.IntegerField(null = False)
  exclusion1 = models.CharField(max_length=200, null=False, blank=True)
  exclusion2 = models.CharField(max_length=200, null=False, blank=True)
  exclusion3 = models.CharField(max_length=200, null=False, blank=True)
  exclusion4 = models.CharField(max_length=200, null=False, blank=True)
  exclusion5 = models.CharField(max_length=200, null=False, blank=True)
  exclusion6 = models.CharField(max_length=200, null=False, blank=True)
  exclusion7 = models.CharField(max_length=200, null=False, blank=True)
  exclusion8 = models.CharField(max_length=200, null=False, blank=True)
  exclusion9 = models.CharField(max_length=200, null=False, blank=True)
  exclusion10 = models.CharField(max_length=200, null=False, blank=True)
  exclusion11 = models.CharField(max_length=200, null=False, blank=True)
  exclusion12 = models.CharField(max_length=200, null=False, blank=True)
  exclusion13 = models.CharField(max_length=200, null=False, blank=True)
  exclusion14 = models.CharField(max_length=200, null=False, blank=True)
  exclusion15 = models.CharField(max_length=200, null=False, blank=True)
  EO_Dummy = models.CharField(max_length=200, null=False, blank=True)
  class Meta:
    db_table = "EO_Naic_Policy_Exclusions"

class GL_Enhancements(models.Model):
  naic = models.IntegerField(blank=False, null = False)
  enhance1  = models.CharField(max_length=200, blank=True)
  enhance2  = models.CharField(max_length=200, blank=True)
  enhance3  = models.CharField(max_length=200, blank=True)
  enhance4  = models.CharField(max_length=200, blank=True)
  enhance5  = models.CharField(max_length=200, blank=True)
  enhance6  = models.CharField(max_length=200, blank=True)
  enhance7  = models.CharField(max_length=200, blank=True)
  enhance8  = models.CharField(max_length=200, blank=True)
  enhance9  = models.CharField(max_length=200, blank=True)
  enhance10 = models.CharField(max_length=200, blank=True)
  enhance11 = models.CharField(max_length=200, blank=True)
  enhance12 = models.CharField(max_length=200, blank=True)
  enhance13 = models.CharField(max_length=200, blank=True)
  enhance14 = models.CharField(max_length=200, blank=True)
  enhance15 = models.CharField(max_length=200, blank=True)
  class Meta:
    db_table = "GL_Naic_Policy_Enhancements"

class GL_Examples(models.Model):
  naic = models.IntegerField(null = False)
  example = models.CharField(max_length=500, null = False)
  class Meta:
    db_table = "GL_Naic_Policy_Examples"

class GL_Exclusions(models.Model):
  naic = models.IntegerField(null = False)
  exclusion1 = models.CharField(max_length=200, null=False, blank=True)
  exclusion2 = models.CharField(max_length=200, null=False, blank=True)
  exclusion3 = models.CharField(max_length=200, null=False, blank=True)
  exclusion4 = models.CharField(max_length=200, null=False, blank=True)
  exclusion5 = models.CharField(max_length=200, null=False, blank=True)
  exclusion6 = models.CharField(max_length=200, null=False, blank=True)
  exclusion7 = models.CharField(max_length=200, null=False, blank=True)
  exclusion8 = models.CharField(max_length=200, null=False, blank=True)
  exclusion9 = models.CharField(max_length=200, null=False, blank=True)
  exclusion10 = models.CharField(max_length=200, null=False, blank=True)
  exclusion11 = models.CharField(max_length=200, null=False, blank=True)
  exclusion12 = models.CharField(max_length=200, null=False, blank=True)
  exclusion13 = models.CharField(max_length=200, null=False, blank=True)
  exclusion14 = models.CharField(max_length=200, null=False, blank=True)
  exclusion15 = models.CharField(max_length=200, null=False, blank=True)
  GL_Dummy = models.CharField(max_length=200, null=False, blank=True)
  class Meta:
    db_table = "GL_Naic_Policy_Exclusions"

# class NAIC_4_Digit_Industry_Code(models.Model):
# class NAIC_Industry_Code(models.Model):
# class NAIC_Policy_Recommendations(models.Model):
# class NAIC_Sub_Industry_Hazard_Rating(models.Model):
# class Policy_Description(models.Model):
# class Policy_Input_Questions(models.Model):


class WC_Enhancements(models.Model):
  naic = models.IntegerField(blank=False, null = False)
  enhance1  = models.CharField(max_length=200, blank=True)
  enhance2  = models.CharField(max_length=200, blank=True)
  enhance3  = models.CharField(max_length=200, blank=True)
  enhance4  = models.CharField(max_length=200, blank=True)
  enhance5  = models.CharField(max_length=200, blank=True)
  enhance6  = models.CharField(max_length=200, blank=True)
  enhance7  = models.CharField(max_length=200, blank=True)
  enhance8  = models.CharField(max_length=200, blank=True)
  enhance9  = models.CharField(max_length=200, blank=True)
  enhance10 = models.CharField(max_length=200, blank=True)
  enhance11 = models.CharField(max_length=200, blank=True)
  enhance12 = models.CharField(max_length=200, blank=True)
  enhance13 = models.CharField(max_length=200, blank=True)
  enhance14 = models.CharField(max_length=200, blank=True)
  enhance15 = models.CharField(max_length=200, blank=True)
  class Meta:
    db_table = "WC_Naic_Policy_Enhancements"

class WC_Examples(models.Model):
  naic = models.IntegerField(null = False)
  example = models.CharField(max_length=500, null = False)
  class Meta:
    db_table = "WC_Naic_Policy_Examples"

class WC_Exclusions(models.Model):
  naic = models.IntegerField(null = False)
  exclusion1 = models.CharField(max_length=200, null=False, blank=True)
  exclusion2 = models.CharField(max_length=200, null=False, blank=True)
  exclusion3 = models.CharField(max_length=200, null=False, blank=True)
  exclusion4 = models.CharField(max_length=200, null=False, blank=True)
  exclusion5 = models.CharField(max_length=200, null=False, blank=True)
  exclusion6 = models.CharField(max_length=200, null=False, blank=True)
  exclusion7 = models.CharField(max_length=200, null=False, blank=True)
  exclusion8 = models.CharField(max_length=200, null=False, blank=True)
  exclusion9 = models.CharField(max_length=200, null=False, blank=True)
  exclusion10 = models.CharField(max_length=200, null=False, blank=True)
  exclusion11 = models.CharField(max_length=200, null=False, blank=True)
  exclusion12 = models.CharField(max_length=200, null=False, blank=True)
  exclusion13 = models.CharField(max_length=200, null=False, blank=True)
  exclusion14 = models.CharField(max_length=200, null=False, blank=True)
  exclusion15 = models.CharField(max_length=200, null=False, blank=True)
  CV_Dummy = models.CharField(max_length=200, null=False, blank=True)
  class Meta:
    db_table = "WC_Naic_Policy_Exclusions"

