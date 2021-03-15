#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

register_rulegroup("datasource_programs",
                   _("Datasource Programs"),
                   _("Specialized agents, e.g. check via SSH, ESX vSphere, SAP R/3"))
group = "datasource_programs"

register_rule(group,
              "special_agents:pagespeed",
              Transform(
                  valuespec=Dictionary(
                      title=_("Check Google Pagespeed API"),
                      help=_("This rule gets performance scores for host from Google PageSpeed Insights"),
                      optional_keys=['timeout', 'check_url', 'api_key'],
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
                  ),
              ),
              factory_default=watolib.Rulespec.FACTORY_DEFAULT_UNUSED,
              match='first')
