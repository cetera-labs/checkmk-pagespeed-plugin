#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# 2020 Ivan Bakharev <ivanbakharev@protonmail.com>

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Integer,
    TextAscii,
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)

def _item_spec_pagespeed():
    return TextAscii(title=_("PageSpeed scan checks"))

def _parameter_valuespec_pagespeed():
    return Dictionary(
        elements=[
            ("score",
             Tuple(
                 title=_("Pagespeed scores for levels"),
                 help=_("Put here the scores from 0 to 100 for check level."),
                 elements=[
                    Integer(title=_('Warning below'), default_value=90),
                    Integer(title=_('Critical below'), default_value=50),
                 ]
             )),
        ],
    )

rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="pagespeed",
        group=RulespecGroupCheckParametersApplications,
        item_spec=_item_spec_pagespeed,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_pagespeed,
        title=lambda: _("PageSpeed"),
    )
)

