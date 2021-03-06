"""TODO: Add missing doctring."""

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.periods import MONTH
from openfisca_core.variables import Variable

# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person


class accommodation_supplement__below_income_threshold(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = "Income is below Accommodation Supplement threshold?"
    definition_period = MONTH


class accommodation_supplement__below_cash_threshold(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = "Cash is below Accommodation Supplement threshold?"
    definition_period = MONTH


class jobseeker_support__below_income_threshold(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = "Income is below Job Seeker Support threshold?"
    definition_period = MONTH


class sole_parent_support__below_income_threshold(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = "Income is below Sole Parent Support threshold?"
    definition_period = MONTH


class community_services_card__below_income_threshold(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = "Income is below Community Services Card threshold?"
    definition_period = MONTH
