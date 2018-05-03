# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a property).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import *


class TaxPayerFilingStatus(Enum):
    __order__ = "non_filing filing filing_with_schedular_income"
    non_filing = u'Non-filing taxpayer'
    filing = u'Filing taxpayer'
    filing_with_schedular_income = u'Filing taxpayer with schedular income'


class tax_payer_filing_status(Variable):
    value_type = Enum
    possible_values = TaxPayerFilingStatus
    default_value = TaxPayerFilingStatus.non_filing
    entity = Person
    definition_period = YEAR
    label = u""
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512331.html"


class annual_gross_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Annual gross income"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512333.html"


class annual_total_deduction(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Annual total deduction"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512336.html"


class net_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Net income"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512339.html"

    def formula(person, period, parameters):
        net_income_calc = person('annual_gross_income', period) - person('annual_total_deduction', period)

        return (
            net_income_calc * (net_income_calc > 0)
            )


class net_loss(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Net loss"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512339.html"

    def formula(person, period, parameters):
        net_income_calc = person('annual_gross_income', period) - person('annual_total_deduction', period)

        return (
            net_income_calc * (net_income_calc < 0)
            )


class taxable_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Net loss"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512344.html"

    def formula(person, period, parameters):
        return (person('net_income', period) - person('available_tax_loss', period))


class available_tax_loss(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Available tax loss"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1520575.html#DLM1520774"


# This variable is a pure input: it doesn't have a formula
class salary(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salary"
    reference = "https://law.gov.example/salary"  # Always use the most official source


# Openfisca example function, to be removed
class disposable_income(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Actual amount available to the person at the end of the month"
    reference = "https://stats.gov.example/disposable_income"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.

    def formula(person, period, parameters):
        return (
            + person('salary', period)
            + person('basic_income', period)
            - person('income_tax', period)
            - person('social_security_contribution', period)
            )

# This file is from the OpenFisca default country template and as such can be removed
