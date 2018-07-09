from django.shortcuts import render
from pdb import set_trace as bp
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from insurance.models import (
  NAIC_Sub_Industry_Code_11, 
  NAIC_Sub_Industry_Code_54, 
  EO_Pricing_Model_Deductible,
  EO_Pricing_Model_Limit,
  EO_Pricing_Model_Base_Rate, 
  EO_Pricing_Model_Marginal, 
  Errors_Omissions_Policy_Details, 
  Hazard_Rate_Multiplier, 
  NAIC_Industry_Code, 
  NAIC_Sub_Industry_Hazard_Rating )
from insurance.lib.helper import getBaseRate

# Create your views here.
def index(request):
  # return HttpResponse('Hello from insurance')

  return render(request, 'insurance/index.html', {
    'title': 'Latest policies'
  })

# sub_industry = NAIC_Sub_Industry_Code_11.objects.first()['industry']
@csrf_exempt
def create_policy(request):
  # To fetch the list of all the major Industries
  # Fetches the class code of the Industry based on the input
  # Fetches the Sub-Industry based on the Class Code
  # Gets the 4 digit sub-class-code based on the User Input
  # Query to get the Hazard class multiplier for the specific Sub-Industry
  # User Inputs
  # Select appropriate Deductible multiplier
  # User input
  # Select appropriate Increased Limit Factor
  # Asks the User for his Annual revenue to calculate the Base price

  all_industries = NAIC_Industry_Code.objects.all()  
  class_code = NAIC_Industry_Code.objects.filter(class_code = request.POST['class_code'])[0].class_code
  sub_industry = NAIC_Sub_Industry_Code_54.objects.first().industry
  class_sub_code = NAIC_Sub_Industry_Code_54.objects.first().class_sub_code
  hazard_level_rating = NAIC_Sub_Industry_Hazard_Rating.objects.filter(class_sub_code = class_sub_code)[0].hazard_level_rating
  hazard_rate_multiplier = Hazard_Rate_Multiplier.objects.filter(hazard_level_rating = hazard_level_rating)[0].rate_multiplier
  deductible_amount = request.POST['deductible_amount']  
  deductible_multiplier = EO_Pricing_Model_Deductible.objects.filter(deductible_amount = deductible_amount)[0].multiplier  
  coverage_limit = request.POST['coverage_limit']    
  inc_limit_factor = EO_Pricing_Model_Limit.objects.filter(occurence_limit = coverage_limit)[0].increased_limit_factor
  ann_revenue_norm = int(request.POST['ann_revenue'])/1000
  base_marginal_rate = getBaseRate(ann_revenue_norm)
  marginal_rate = 1
  base_rate = 0
  if len(base_marginal_rate) == 1 :
    base = EO_Pricing_Model_Base_Rate.objects.filter(annual_sales = base_marginal_rate[0])[0].base_rate
    base_rate = base
  else :
    base = EO_Pricing_Model_Base_Rate.objects.filter(annual_sales = base_marginal_rate[0])[0].base_rate
    marginal_rate = EO_Pricing_Model_Marginal.objects.filter(annual_sales = base_marginal_rate[1])[0].marginal_price
    base_rate = base + (ann_revenue_norm - base_marginal_rate[0]) * marginal_rate
  premium_price = float(base_rate * hazard_rate_multiplier * deductible_multiplier * inc_limit_factor * 1.4)
  return HttpResponse(premium_price)

def policy_details(request, policy_code, naic_code):
  print(request)
  print(policy_code)
  print(naic_code)
  return HttpResponse("OK")

def policy_description(request):
  print(request)
  return HttpResponse("OK")

# 'policy_description
# 'create_policy