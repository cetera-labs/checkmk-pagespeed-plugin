#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# 2020 Ivan Bakharev <ivanbakharev@protonmail.com>

register_check_parameters(
    subgroup_applications,
    "pagespeed",
    _("PageSpeed scan checks"),
    Dictionary(
        elements=[
            ("score",
             Tuple(
                 title=_("Pagespeed scores for levels"),
                 help=_("Put here the scores from 0 to 100 for check level."),
                 elements=[
                    Integer(title=_('Warning below'), default_value=90),
                    Integer(title=_('Critical below'), default_value=50),
                 ]
             ),
             ),
        ]
    ),
    None,
    match_type="dict",
)
