# --% /np/react-antd/components/modules/Task/UpdateForm.js
form_items = """
          <Form.Item name='title' label="Title">
            <Input />
          </Form.Item>
          
          <Form.Item name='description' label="Description">
            <Input.TextArea />
          </Form.Item>
          
          <Form.Item name='period_type' label="Period Type">
            <Input />
          </Form.Item>
"""

update_form = """
import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
import moment from 'moment';

const UpdateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit UpdateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  useEffect(() => {
    const {
      date,
      ...bukan_tanggal
    } = initialFormValues

    form_konek_provider.setFieldsValue({
      date: moment(date),
      ...bukan_tanggal
    });

  }, [initialFormValues]);

  return <Form name='update_form' 
      // size='small'
      form={form_konek_provider}
      className='update_form'
    >
      <Row gutter={[8, 16]}>
        <Col span='24'>
          
          {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}

__TEMPLATE_FORM_ITEM_LIST

        </Col>
      </Row>

    </Form>;
}

export default UpdateForm;
"""
