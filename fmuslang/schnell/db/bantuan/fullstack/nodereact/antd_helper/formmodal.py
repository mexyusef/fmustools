# --% /np/react-antd/components/modules/Task/Modal.js

form_modal = """
import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, 
  Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';


const BoComponentModalDefaultContent = ({
  data_selected,
  data_raw
}) => (<>
      Daftar terselect default isi-selected: {JSON.stringify(data_selected)}
      <hr />
      Isi show (data raw): {JSON.stringify(data_raw)}
  </>
);

const BoComponentModal = ({
  Content,
  modal_title,
  modal_bomodule_visible,
  modal_bomodule_selected,
  modal_bomodule_content,
  set_modal_bomodule,
}) => (<Modal visible={modal_bomodule_visible} title={modal_title}
    onOk={(e) => set_modal_bomodule(false)}
    onCancel={(e) => set_modal_bomodule(false)}
  >

    {<Content
      data_selected={modal_bomodule_selected}
      data_raw={modal_bomodule_content}
    />}

  </Modal>
);

export default {
  BoComponentModalDefaultContent,
  BoComponentModal,
};
"""
