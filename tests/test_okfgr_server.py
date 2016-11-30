# -*- coding: utf-8 -*-

from .context import okfgr_dm

import json
import unittest


class SendDMRequestToOKFGRServer(unittest.TestCase):
    """Basic test cases."""

    def test_send_csv_to_uep_server(self):
        jsonStr = okfgr_dm.dm_okfgr("/ocpu/library/OBeU/R/ts.obeu", tsdata="Athens_draft_ts", prediction_steps=4)
        dic = json.loads(jsonStr)
        assert "data_year" in dic.keys()
        assert "data" in dic.keys()
        assert "predict_time" in dic.keys()


if __name__ == '__main__':
    unittest.main()