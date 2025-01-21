--% index/fmus
        <Sidebar 
          active_classname={openSidebar ? 'sidebar-layout active' : 'sidebar-layout'}
          is_active={openSidebar}
          togglerMenu={()=>{
            setOpenSidebar(!openSidebar);
          }}
          color={color} 
          image={hasImage ? image : ""} 
          routes={routes} 
          />
--#


--% /react-light/src/components/Sidebar/Sidebar.js
import React from "react";
import { useLocation, NavLink } from "react-router-dom";

import { Nav } from "react-bootstrap";
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as RiIcons from 'react-icons/ri';

import {Menu1, Menu2, Menu3} from './Menu';
import SubMenu from './SubMenu';
import SidebarToggler from './SidebarToggler';
import './Sidebar.css';

const SidebarBottom = ({
	judul,
	data = Menu3
}) => {
	return (<>
		<h6 className="md:min-w-full text-blueGray-500 text-xs uppercase font-bold block pt-1 pb-4 no-underline">
			{judul}
		</h6>
		{data.map((item, index) => {
			return <SubMenu item={item} key={index} />;
		})}

	</>);
};

__TEMPLATE_MENU_DECLARE

function Sidebar({
	match, 
	// location, 
	history, active_classname, is_active, togglerMenu,
	color, image, routes 
}) {

	const location = useLocation();
	const pathname = location.pathname;

	const activeRoute = (routeName) => {
		// return location.pathname.indexOf(routeName) > -1 ? "active" : "";
		return pathname.indexOf(routeName) > -1 ? "active" : "";
	};

	return (
		<div>
			
			<SidebarToggler 
				active_classname={is_active ? 'sidebar-toggler active' : 'sidebar-toggler'} 
				togglerMenu={togglerMenu} 
				/>

			<div 
				className={`sidebar ` + active_classname} 
				data-image={image} 
				data-color={color}>

				<div
					className="sidebar-background"
					style={{
						backgroundImage: "url(" + image + ")",
					}}
				/>

				<div className="sidebar-wrapper">
					<div className="logo d-flex align-items-center justify-content-start">
						<a
							href="http://fulgent.de?ref=lbd-sidebar"
							className="simple-text logo-mini mx-1"
						>
							<div className="logo-img">
								<img src={require("assets/img/reactlogo.png").default} alt="..."/>
							</div>
						</a>
						<a className="simple-text" href="http://fulgent.de">
							Fulgent
						</a>
					</div>

					{/* <Nav>
						{routes.map((prop, key) => {
							if (!prop.redirect)
								return (
									<li
										className={
											prop.upgrade
												? "active active-pro"
												: activeRoute(prop.layout + prop.path)
										}
										key={key}
									>
										<NavLink
											to={prop.layout + prop.path}
											className="nav-link"
											activeClassName="active"
										>
											<i className={prop.icon} />
											<p>{prop.name}</p>
										</NavLink>
									</li>
								);
							return null;
						})}
					</Nav> */}

<SidebarBottom judul='' data={[
	{title:"Dashboard", path:"dashboard", icon: <AiIcons.AiFillHome />,},
	{title:"Table", path:"table", icon: <AiIcons.AiFillHome />,},
	{title:"Icons", path:"icons", icon: <AiIcons.AiFillHome />,},
	{title:"Typography", path:"typography", icon: <AiIcons.AiFillHome />,},
	{title:"Notifications", path:"notifications", icon: <AiIcons.AiFillHome />,},
]}/>
<hr className="my-4 md:min-w-full" />

__TEMPLATE_MENU_CALL

				</div>
			</div>
		</div>
	);
}

export default Sidebar;
--#
