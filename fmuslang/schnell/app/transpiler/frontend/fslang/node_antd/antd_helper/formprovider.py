# --% /np/react-antd/components/modules/Task/FormProvider.js

form_provider = """
import React, { useEffect, useState } from 'react';

import {
  Button,
  Checkbox,
  Form,
  notification,
} from 'antd';

import useAxios from 'utils/useAxios';
import UpdateForm from './UpdateForm';
import CreateForm from './CreateForm';
import PubSub from 'pubsub-js';

const FormProvider = ({
  onClose,
  data_raw = {},
  submit_form = (values) => console.log(`submit FormProvider`),
}) => {

  const updateRecord = useAxios({ method: 'PATCH', });
  const createRecord = useAxios({ method: 'POST', path: '__TEMPLATE_modelname',  });
  const is_updating = Object.keys(data_raw).length > 0;

  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  return <Form.Provider onFormFinish={(name, {values, forms}) => {

    if (is_updating) {
      const { update_form } = forms;
      let updated_values = update_form.getFieldsValue();
      let diffs = {};
      for (let key in updated_values) {
        if (updated_values.hasOwnProperty(key)) {
          if (updated_values[key] !== data_raw[key]) {
            diffs[key] = updated_values[key];
          }
        }      
      }
      console.log(`update diffs: ${JSON.stringify(diffs)}`);
      let values_has_changed = Object.keys(diffs).length > 0;
      if (values_has_changed) {
        updateRecord(
          {
            // url: useUrlBuilder(`bo/bo_marketholiday/${updated_values.id}`),
            path: `__TEMPLATE_modelname/${updated_values.id}`,
            data: diffs
          },

          response => {
            console.log(`sukses updateRecord => ${JSON.stringify(response)}`);
            berhasil(`sukses updateRecord [${JSON.stringify(response)}]`);
            PubSub.publish('<<Update:Record>>', response);
          },

          err => {
            console.log(`gagal updateRecord => ${JSON.stringify(err)}.`);
            gagal(`gagal updateRecord [${JSON.stringify(err)}]`);
          }
        );
      }

    } else {
      const { create_form } = forms;
      let created_values = create_form.getFieldsValue();
      console.log(`created values from onformfinish: ${JSON.stringify(values)} vs getfieldsvalue ${JSON.stringify(created_values)}`);
      createRecord(
        {
          data: created_values
        },

        response => {
          console.log(`sukses createRecord => ${JSON.stringify(response)}`);
          berhasil(`sukses createRecord.`);
          PubSub.publish('<<Create:Record>>', response);
        },

        err => {
          console.log(`gagal createRecord => ${JSON.stringify(err)}.`);
          gagal(`gagal createRecord.`);
        }
      );

    }

    onClose();

  }}>

    {is_updating ? <UpdateForm initialFormValues={data_raw} /> : <CreateForm />}

    <Form name="fundordertabs-form-body" onFinish={(values) => {}}>
      <Form.Item>
        <Button type='primary' htmlType="submit">Submit</Button>
      </Form.Item>
    </Form>

  </Form.Provider>;

}

export default FormProvider;
"""