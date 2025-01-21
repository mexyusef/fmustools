# --% /np/react-antd/components/modules/Task/List.js

form_list = """
import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';

import {
  // DownOutlined, 
  // UserOutlined,
  // ReloadFilled, 
  // DeleteOutlined,
  // HomeOutlined,
  // SettingFilled,
  // SmileOutlined,
  
  FileAddOutlined,
  FileExcelOutlined,
  FilePdfOutlined,
  ReloadOutlined,
  DeleteFilled,
} from '@ant-design/icons';
import PubSub from 'pubsub-js';

import useAxios from 'utils/useAxios';
import SimpleTable from 'common/Table/SimpleTable';
import JsonData from 'assets/__TEMPLATE_modelname.json';

function column_sorter(a, b, column) {
  console.log(`table sorting: ${column}, pertama ${a[column]}, kedua ${b[column]}.`);
  // return b[column] > a[column]
  // return b[column].localeCompare(a[column])
  // return a[column] - b[column]
  // return a[column] > b[column]
  if (b[column] === null || b[column] === '') // descend
    return -1;
  else if (a[column] === null || a[column] === '')
    return 1;
  else if (typeof(b[column]) === "string")
    // return b[column][0].toLowerCase() > a[column][0].toLowerCase();
    return 0;
      
  return b[column] > a[column];
}

const List = ({
  show_update,
  recordTransformer = record => record,
}) => {

  const resource_path = '__TEMPLATE_modelname';
  const deleteRecord = useAxios({ method: 'DELETE', });
  const [table_data, set_table_data] = useState([]);
  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  const getResourceData = useAxios({ path: resource_path, });  

  const update_table_data = (topic_channel, data) => {
    getResourceData({}, successHandler);
  };

  const successHandler = response => {
    let data = response.result
      .map((record, index) => {
        record.key = index;
        return recordTransformer(record);
      });

    set_table_data(data);
  };

  const wrapAsync = () => {
    PubSub.subscribe('<<Create:Record>>', update_table_data);
    PubSub.subscribe('<<Update:Record>>', update_table_data);
    PubSub.subscribe('<<Delete:Record>>', update_table_data);
  }

  useEffect(() => {
    wrapAsync();
    getResourceData({}, successHandler);
  }, []);

  const handleDelete = record => {
    const key = record.key;
    console.log(`deleting ${key} dari record ${JSON.stringify(record)}.`);
    // const table_data_temp = [...table_data].filter(item => item.key !== key);
    let kunci;
    if (record.hasOwnProperty('id')) {
      kunci = record.id;
    } else {
      console.log(`Did not know how to identify this record to delete: ${JSON.stringify(record)}`);
      return;
    }

    deleteRecord(
      {
        path: `${resource_path}/${kunci}`,
      },
      response => {
        console.log(`berhasil hapus ${kunci}`);
        PubSub.publish('<<Delete:Record>>', response);
        berhasil('Berhasil', `Berhasil hapus id ${kunci}`);
      },
      err => {
        console.log(`gagal hapus ${kunci}`);
        gagal('Gagal hapus...', `Tidak berhasil hapus ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
      }
    );
  }

  const table_header = JsonData.headers.map((column, index) => {

    if (column === "") {

      return {
        title: "Show",
        fixed: 'left',
        width: JsonData.widths.show,
        render: data => <Button onClick={() => {
          console.log(`Show data ${JSON.stringify(data)}`);
          show_update(data);
        }}>Show </Button>,
      };

    } else if (column === "delete") {

      return {
        title: 'Hapus',
        dataIndex: 'operation',
        fixed: 'right',
        width: JsonData.widths.hapus,
        render: (text, record) => table_data.length >= 1 ? (
          <Popconfirm title={`Yakin hapus ${record.id}?`} onConfirm={() => handleDelete(record)}>
            <DeleteFilled style={{ fontSize: '20px', color: '#f25', textAlign: 'center' }} />
          </Popconfirm>
        ) : null,
      };

    } else {

      let noFilter = {
        // kolom biasa, dataIndex sama dg nama kolom
        title: column,
        fixed: index == 1 ? 'left' : null,
        width: index == 1 ? JsonData.widths.id : JsonData.widths.normal,
        dataIndex: (column !== "" && column !== "cb") ? column : '0',
        // defaultSortOrder: 'descend',
        sortDirections: ['descend', 'ascend', 'descend'],
        sorter: (a, b) => column_sorter(a, b, column),
      }

      // let filteredColumn = column.replace('filter#', '')
      // let withFilter = {
      //   // kolom biasa, dataIndex sama dg nama kolom
      //   title: filteredColumn,
      //   fixed: index == 1 ? 'left' : null,
      //   width: index == 1 ? 75 : 150,
      //   dataIndex: (filteredColumn !== "" && filteredColumn !== "cb") ? filteredColumn : '0',
      //   // defaultSortOrder: 'descend',
      //   sortDirections: ['descend', 'ascend', 'descend'],
      //   sorter: (a, b) => column_sorter(a, b, filteredColumn),

      //   filterDropdown: (<div className="custom-filter-dropdown">
      //     <Input
      //       placeholder="Cari nilai..."
      //       value={filterText[index]}
      //       onChange={e => {
      //         let newText = [...filterText]
      //         newText[index] = e.target.value
      //         setFilterText(newText)
      //       }}
      //       onPressEnter={() => filterSearch(filteredColumn, index)}
      //     />
      //     <Button type="primary" onClick={() => filterSearch(filteredColumn, index)}>Cari</Button>
      //   </div>),
      //   filterDropdownVisible: filterVisible[index],
      //   onFilterDropdownVisibleChange: visible => setColumnVisible(visible, index),
      // };

      // let filterCondition = column.startsWith('filter#');
      // return filterCondition ? withFilter : noFilter;

      return noFilter;
    }

  });

  const modalSelectionHandler = (selections) => {
    // set_modal_bomodule_selected(selections);
    // if (selectionCallback !== undefined) {            
    //   // kirim id dari record, bukan index selection
    //   let id_list = []
    //   selections.forEach(index => {
    //     let ketemu = table_data.find(record => record.key == index)                
    //     // if (ketemu.hasOwnProperty('id') && ketemu.hasOwnProperty('id_user'))
    //     //   id_list .push(ketemu.id + "," + ketemu.id_user);
    //     // else if (ketemu.hasOwnProperty('orderno') && ketemu.hasOwnProperty('customerno'))
    //     //   id_list .push(ketemu.orderno + "," + ketemu.customerno);
    //   })
    //   if (id_list.length > 0) {
    //     selectionCallback(id_list);
    //     console.log(`selection ${id_list}`);
    //   }
    // }
    console.log(`SimpleTable selectCallback: ${selections}, ${typeof(selections)}.`);
  }

	return <>

    <SimpleTable 
      header={table_header}
      body={table_data} 
      selectCallback={modalSelectionHandler} />

  </>;
};

export default List;
"""
