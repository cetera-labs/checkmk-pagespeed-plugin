#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Integer,
    TextAscii,
)

from cmk.gui.plugins.wato import (
    IndividualOrStoredPassword,
    RulespecGroup,
    RulespecSubGroup,
    monitoring_macro_help,
    rulespec_group_registry,
    rulespec_registry,
    HostRulespec,
)

@rulespec_group_registry.register
class RulespecGroupDatasourcePrograms(RulespecGroup):
    @property
    def name(self):
        return "datasource_programs"

    @property
    def title(self):
        return _("Datasource Programs")

    @property
    def help(self):
        return _("Specialized agents, e.g. check via SSH, ESX vSphere, SAP R/3")

def _valuespec_special_agents_pagespeed():
    return Dictionary(
        title=_("Check Google Pagespeed API"),
        help=_("This rule gets performance scores for host from Google PageSpeed Insights"),
        elements=[
          ("timeout",
           Integer(
               title=_("Connect Timeout"),
               help=_("The network timeout in seconds when communicating via HTTP. "
                      "The default is 180 seconds."),
               default_value=180,
               minvalue=1,
               unit=_("seconds")
           )
           ),
          ("api_key",
           TextAscii(
               title=_("API Key for PageSpeed Insights"),
               help=_("https://developers.google.com/speed/docs/insights/v5/get-started#APIKey"),
               allow_empty=False,
           ),
           ),
          ("check_url",
           TextAscii(
               title=_("URL for check"),
               help=_("If field is empty hostname will be used for check"),
               allow_empty=False,
           ),
           ),
          ("ttl",
           Integer(
               title=_("Cache TTL"),
               help=_("Cache time to live in seconds"),
               default_value=3600,
               minvalue=60,
               unit=_("seconds")
           )
           ),
        ],
        optional_keys=[
            "ttl",
        ],
    )

def _factory_default_special_agents_pagespeed():
    return watolib.Rulespec.FACTORY_DEFAULT_UNUSED

rulespec_registry.register(
    HostRulespec(
        factory_default=_factory_default_special_agents_pagespeed(),
        group=RulespecGroupDatasourcePrograms,
        name="special_agents:pagespeed",
        valuespec=_valuespec_special_agents_pagespeed,
    ))