--% getting started
https://ant.design/docs/react/getting-started

```
{
"dependencies": {
    "react-dom": "latest",
    "react": "latest",
    "moment": "latest",
    "antd": "latest"
},
    "keywords": [],
    "name": "antd-reproduction-template",
    "description": ""
}

.App {
    padding: 20px;
}

<div id="root"></div>

import React from "react";
import ReactDOM from "react-dom";
import { Button, DatePicker, version } from "antd";
import "antd/dist/antd.css";
import "./index.css";

ReactDOM.render(
  <div className="App">
    <h1>antd version: {version}</h1>
    <DatePicker />
    <Button type="primary" style={{ marginLeft: 8 }}>
      Primary Button
    </Button>
  </div>,
  document.getElementById("root")
);
```

--#

--% components
https://ant.design/components/overview/
--#

--% components/general: button, icon, typography
https://ant.design/components/button/
https://ant.design/components/icon/
https://ant.design/components/typography/
--#

--% components/layout: divider, grid, layout, space
https://ant.design/components/divider/
https://ant.design/components/grid/
https://ant.design/components/layout/
https://ant.design/components/space/
--#

--% components/navigation: affix, breadcrumb, dropdown, menu, pageheader, pagination, steps
https://ant.design/components/affix/
https://ant.design/components/breadcrumb/
https://ant.design/components/dropdown/
https://ant.design/components/menu/
https://ant.design/components/page-header/
https://ant.design/components/pagination/
https://ant.design/components/steps/
--#

--% components/data entry: autocomplete, cascader, checkbox, datepicker, form, input, inputnumber, mentions, radio, rate, select, slider, switch, timepicker, transfer, treeselect, upload
https://ant.design/components/auto-complete/
https://ant.design/components/cascader/
https://ant.design/components/checkbox/
https://ant.design/components/date-picker/
https://ant.design/components/form/
https://ant.design/components/input/
https://ant.design/components/input-number/
https://ant.design/components/mentions/
https://ant.design/components/radio/
https://ant.design/components/rate/
https://ant.design/components/select/
https://ant.design/components/slider/
https://ant.design/components/switch/
https://ant.design/components/time-picker/
https://ant.design/components/transfer/
https://ant.design/components/tree-select/
https://ant.design/components/upload/
--#

--% components/data display: avatar, badge, calendar, card, carousel, collapse, comment, descriptions, empty, image, list, popover, segmented, statistic, table, tabs, tag, timeline, tooltip, tree
https://ant.design/components/avatar/
https://ant.design/components/badge/
https://ant.design/components/calendar/
https://ant.design/components/card/
https://ant.design/components/carousel/
https://ant.design/components/collapse/
https://ant.design/components/comment/
https://ant.design/components/descriptions/
https://ant.design/components/empty/
https://ant.design/components/image/
https://ant.design/components/list/
https://ant.design/components/popover/
https://ant.design/components/segmented/
https://ant.design/components/statistic/
https://ant.design/components/table/
https://ant.design/components/tabs/
https://ant.design/components/tag/
https://ant.design/components/timeline/
https://ant.design/components/tooltip/
https://ant.design/components/tree/
--#

--% components/feedback: alert, drawer, message, modal, notification, popconfirm, progress, result, skeleton, spin
https://ant.design/components/alert/
https://ant.design/components/drawer/
https://ant.design/components/message/
https://ant.design/components/modal/
https://ant.design/components/notification/
https://ant.design/components/popconfirm/
https://ant.design/components/progress/
https://ant.design/components/result/
https://ant.design/components/skeleton/
https://ant.design/components/spin/
--#

--% components/other: anchor, backtop, configprovider
https://ant.design/components/anchor/
https://ant.design/components/back-top/
https://ant.design/components/config-provider/
--#

--% real project with umi
https://ant.design/docs/react/practical-projects
--#

--% cra, create-react-app
https://ant.design/docs/react/use-with-create-react-app
--#

--% ts, typescript
https://ant.design/docs/react/use-in-typescript
--#
