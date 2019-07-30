from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("New Registration"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Mobile User",
              "label": _("New Mobile User"),
              "description": _("Articles which members issue and return"),
            },
            {
              "type": "doctype",
              "name": "Resident Visitation",
              "label": _("New Visitor"),
              "description": _("Articles which members issue and return"),
            }
          ]
      }
  ]
