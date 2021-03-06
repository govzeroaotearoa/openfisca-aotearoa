"""TODO: Add missing doctring."""

from openfisca_core.periods import ETERNITY
from openfisca_core.variables import Variable

from openfisca_aotearoa.entities import Person


class weekly_compensation__lodges_a_claim(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = "A claimant who has cover and who lodges a claim for weekly compensation"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM100910.html"
