
# --% /np/react-antd/assets/menu.json
menu_item_template = """
  {
    "label": "__TEMPLATE_Modelname",
    "children": [
      { "label": "Create", "link": "__TEMPLATE_modelname" },
      { "label": "Read", "link": "__TEMPLATE_modelname" },
      { "label": "Update", "link": "__TEMPLATE_modelname" },
      { "label": "Delete", "link": "__TEMPLATE_modelname" }
    ]
  },
"""

menu_json = """[
  {
    "label": "Contoh Menu Lengkap",
    "children": [
      {
        "label": "Master",
        "children": [
          {
            "label": "Sub General",
            "children": [
              {
                "label": "Company"
              },
              {
                "label": "Fund",
                "link": "fund"
              },
              {
                "label": "Master Value",
                "link": "master-value"
              },
              {
                "label": "Activity"
              }
            ]
          },
          {
            "label": "Sub Accounting",
            "children": [
              {
                "label": "Account",
                "link": "account"
              },
              {
                "label": "Company Account Trading"
              }
            ]
          },
          {
            "label": "Sub Customer Service",
            "children": [
              {
                "label": "Black List Name"
              },
              {
                "label": "High Risk Monitoring",
                "link": "highriskmonitoring"
              }
            ]
          },
          {
            "label": "Sub Transaction",
            "children": [
              {
                "label": "AUM",
                "link": "aum"
              },
              {
                "label": "Sector",
                "link": "sector"
              }
            ]
          }
        ]
      },
      {
        "label": "Users",
        "link": "user"
      },
      {
        "label": "Security Setup",
        "link": "securitysetup"
      }
    ]
  },

__TEMPLATE_APP_MENU

  {
    "label": "Dashboard",
    "link": "dashboard"
  }

]
"""
