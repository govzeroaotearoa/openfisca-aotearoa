"""TODO: Add missing doctring."""

from openfisca_core.periods import MONTH
from openfisca_core.variables import Variable

from openfisca_aotearoa.entities import Person


class weekly_compensation__loss_of_earnings_payable(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Engaged in full-time study or training, does not include full-time study or training in living or social skills"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104891.html"
