"""TODO: Add missing doctring."""

from openfisca_core.periods import MONTH
from openfisca_core.variables import Variable

from openfisca_aotearoa.entities import Person


class acc__is_receiving_compensation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is receiving compensation payment through ACC"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM105404.html#DLM105404"
