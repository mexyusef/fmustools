# --% /np/react-antd/components/modules/Task/Task.js

form_model = """
import React, { useEffect, useState } from 'react';

import {
	Button,
	DatePicker,
	Divider,
	Drawer,
	Input, InputNumber ,
	Modal,
	Popover,
	Select,
	Space,
} from 'antd';
import {
	DesktopOutlined,
	DownOutlined, 
	UserOutlined,
	// HomeOutlined,
	// SettingFilled,
	// SmileOutlined,
	FileExcelOutlined,
	FilePdfOutlined,
	ReloadOutlined,
	ReloadFilled, 
	DeleteOutlined,
	DeleteFilled,
} from '@ant-design/icons';

import ToolbarContext from 'context/ToolbarContext';
import TabPage from 'common/TabPage';

import ReadList from './List';
import FormWrapper from './FormWrapper';

const __TEMPLATE_Modelname = () => {
	const { setToolbar } = React.useContext(ToolbarContext);
	const [lokasiTab, setLokasiTab] = useState('top');
	const [drawerVisible, setDrawerVisible] = useState(false);
	// diisi oleh List wkt 'Show'
	const [modal_bomodule_content, set_modal_bomodule_content] = useState({});

	const show_update = (data) => {
		set_modal_bomodule_content(data);
		setDrawerVisible(true);
	}

	let Toolbar = () => (<Space>
		<h1>__TEMPLATE_Modelname</h1>
		<Button type="primary" 
			onClick = {				
				() => {
					set_modal_bomodule_content({});
					setDrawerVisible(true);
				}
			}>Create new</Button>
		{/* <Button type="default" disabled onClick={generateBlotter2}>Blotter Subscription</Button> */}
		{/* <Popover placement="bottom" title={<span>Pilih nasabah dan tanggal Blotter subscription</span>} content={Blotter_Popup} trigger="click"> */}
		{/* <Button disabled type="primary">Blotter Subscription</Button> */}
		{/* </Popover> */}			
	</Space>);

	useEffect(function() {
		setToolbar(<Toolbar />)
	}, []);

	return <>
		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'Create',
						icon: <DesktopOutlined />,
						component: <FormWrapper />
					},
					{
						title: 'Read',
						icon: <DesktopOutlined />,
						component: <ReadList show_update={show_update} />
					},
				]
			} />

		<Drawer
      title="Add Record"
      placement='right'      
      onClose={() => setDrawerVisible(false)}
      visible={drawerVisible}
      width={800}
      // closable={false}
      >

			<FormWrapper
				data_raw={modal_bomodule_content}
				onClose={() => setDrawerVisible(false)}
				/>

		</Drawer>
	
	</>;
};

export default __TEMPLATE_Modelname;
"""
