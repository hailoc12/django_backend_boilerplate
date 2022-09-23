import pytest 
pytestmark = pytest.mark.django_db
from bot_xsmb.kq_xo_so.analysis import (
    calculate_dau_duoi_giai_dac_biet, 
    calculate_lo_to_kep
)

from bot_xsmb.kq_xo_so.models import (
    get_yesterday_xsmb_result, 
    XoSoMienBac
)

class TestAnalysis():
    def test_calculate_dau_duoi_giai_dac_biet(self):
        yesterday_result = get_yesterday_xsmb_result()
        dau_duoi = calculate_dau_duoi_giai_dac_biet(yesterday_result)
        assert (dau_duoi is not None)

    def test_calculate_lo_to_kep(self):
        yesterday_result = get_yesterday_xsmb_result()
        lo_to_kep = calculate_lo_to_kep(yesterday_result)
        assert(lo_to_kep is not None)
